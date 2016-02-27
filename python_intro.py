print('Hello, Django girls!')
name = 'Sonja'
if name == 'Ola' :
	print('Hej Ola!')
elif name == 'Sonja':
	print('Hej Sonja!')
else:
	print('Hej nieznajoma!')
volume = 33
if volume < 20:
	print("Prawie nic nie slychac.")
elif 20 <= volume < 40:
	print("O, muzyka leci w tle.")
elif 40 <= volume < 60:
	print("Idelanie, moge uslyszec wszytskie detale")
elif 60 <= volume < 80:
	print("Dobre na imprezy")
elif 80 <= volume < 100:
	print("Troszeczke za glosno!")
else:
	print("Ojoj! Moje uszy! :(")
def hej():
	print('Hej!')
	print('jak się masz?')

hej()
def hej(imie):
	if imie == "Ola":
		print("Hej Ola!")
	elif imie == 'Sonja':
		print('Hej Sonja!')
	else:
		print('Hej nieznajoma!')

hej("Sonja")
def hej(imie):
	print('Hej ' + imie + "!")

hej("Rachel")
dziewczyny = ['Madzia', 'Ania', 'Ola', 'Kama']
for imie in dziewczyny:
	hej(imie)
	print('Kolejna dziewczyna')
