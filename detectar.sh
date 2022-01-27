#!/bin/bash
#Autor: fitorec <http://fitorec.wordpress.com/>
#Descripción: Detecta a los hosts conectados en nuestra red
#Requiere: nmap
#
#Atención: Lo único q requiere configurar es la interfaz en donde se desea escuchar
INTER='wlo1'

#hackers: 
#		Lo interesante de este script(para mi) fue la conversión de la mascara de red a su cantidad de bits
#		p.e. convertir 255.255.255.0  a /24, considerando que la red podría estar segmentada.
#		solución: en lo personal desconozco de algún programa que te haga tal acción en GNU/Linux, sin mas implemente 
#		un algoritmo d conversión de entera a binaria, la mascara de red 255.255.255.0 sera 8+8+8+0=14
#
#		Para mayor info: "How to Convert From Base 10 to Base K"
#			http://www.cs.umd.edu/class/sum2003/cmsc311/Notes/Data/toBaseK.html
#
#		Usted puede obtener una explicación mas detallada en la teoría de el segmentado de redes:
#		wikipedia - "Subnetwork"
#			http://en.wikipedia.org/wiki/Subnetwork


# Esta función devuelve la mascara de red en formato de numero de bits
function mask2bits {
	m=`ifconfig $INTER | awk '{print $4}' | grep -o -E '([0-9]{1,3}\.){3}[0-9]+'`
	#Número de bits
	nbits=0
	#Iteramos entre los 4 fragmentos de la mascara de red
	for i in {1..4}
	do
		#extraemos el valor(en decimal) del fragmento i-enésimo 
		v=`echo $m | cut -d'.' -f$i`
		#simple implementación algorítmica(ver sección hackers)
		while [ $v -ge 1 ]; do
			let nbits=nbits+$v%2
			let v=v/2
		done
	done
	echo $nbits
}

#
MASK=`mask2bits`

#Atrapamos la IP, con una la expresión regular
IP=`ifconfig $INTER | grep -o -E '([0-9]{1,3}\.){3}[1-9]+' | head -1`

#Ejecutamos el nmap para detectar a los hosts conectados en nuestra red(posibles intrusos)
#Cachando sólo las IPs de los hosts conectados(para mostrarlos en el conky)
#
nmap -sP $IP/$MASK  | grep -o -E '([0-9]{1,3}\.){3}[0-9]+'
