#!/usr/bin/bash

def parite(d):
	countn = 0
	resultat = []
	for i in d:
		countn = 0
		for j in i:
			if '1' in j:
				countn = countn + 1
		if countn%2==0:
			resultat.append("0"+i)
		else:
			resultat.append("1"+i)
	return resultat

a=[]
for x in range(3):
	b = input("Entrez un nombre: ")
	a.append(b)
print(parite(a))
