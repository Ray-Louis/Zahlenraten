print("Herzlich willkommen beim Zahlen erraten, rate eine Zahl von 1 bis 50:  ")
from random import randint
ratezahl=randint(1,50)

zahl=int(input("Zahl:  "))


if zahl < ratezahl:
	print("zu klein!")
	
if zahl> ratezahl:
	print("zu groß!")
if zahl==ratezahl:
	print("super du hast gewonnen!")
	print("1Versuch")
	input()
	exit()
zahl=int(input("Zahl:  "))
if zahl==ratezahl:
	print("super du hast gewonnen!")
	print("2Versuche")
	input()
	exit()

if zahl < ratezahl:
	print("zu klein!")
	
if zahl> ratezahl:
	print("zu groß!")
zahl=int(input("Zahl:  "))
if zahl==ratezahl:
	print("super du hast gewonnen!")
	print("3 versuche")
	input()
	exit()
if zahl < ratezahl:
	print("zu klein!")
	
if zahl> ratezahl:
	print("zu groß!")
zahl=int(input("Zahl:  "))
if zahl==ratezahl:
	print("super du hast gewonnen!")
	print("4 Versuche")
	input()
	exit()
if zahl < ratezahl:
	print("zu klein!")
	
if zahl> ratezahl:
	print("zu groß!")
zahl=int(input("Zahl:  "))
if zahl==ratezahl:
	print("super du hast gewonnen!")
	print("5 versuche")
	input()
	exit()
if zahl < ratezahl:
	print("zu klein!")
	
if zahl> ratezahl:
	print("zu groß!")
zahl=int(input("Zahl:  "))
if zahl==ratezahl:
	print("super du hast gewonnen!")
	print("6 versuche")
	input()
	exit()
print("Du hast verloren")
print("Die Zahl war: ")
print(ratezahl)
input(exit)