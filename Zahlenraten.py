from random import randint

print("Herzlich willkommen beim Zahlenraten")

#Richtige angabe der Zahlen wird überprüft
while True:
	min = int(input("Gib die kleinste Zahl an: "))
	max = int(input("Gib die größte Zahl ein: "))
	if max <= min:
		print("Die erste Zahl muss kleiner sein")
	else:
		break

#Variabeln werden deklariert
versuche = 0
ergebnis = randint(min,max)
zahlen = []

#Das Spiel läuft
while True:
	zahl = int(input("Rate eine Zahl: "))
	#Eingegebene Zahl wird validiert
	if zahl < min or zahl > max:
		print(f"Die eingegebene Zahl ist zu groß/klein. Es muss eine Zahl zwischen {min} und {max} sein")
		continue
	if zahl in zahlen:
		print("Du hast es mit dießer Zahl schon einmal ausprobiert. Versuche es mit einer anderen Zahl")
		continue
	#Eingegebene Zahl wird verarbeitet
	versuche += 1
	zahlen.append(zahl)

	#Eingegebene Zahl wird verglichen
	if zahl < ergebnis:
		print("Die Zahl ist zu klein")
	elif zahl > ergebnis:
		print("Die Zahl ist zu groß")
	else:
		print(f"Du hast mit {versuche} Versuch(en) die richtige Zahl {zahl} erraten.")
		break
		
input()
exit