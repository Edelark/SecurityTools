# -*- coding: utf-8 -*-


"Made by EnriqueMoran to github.com/Edelark/SecurityTools V1.0 "


import random
import math

class PasswordGenerator():
	""" [EN] This class contains the necessary methods for password generation.
	[ES] Esta clase contiene los métodos necesarios para la generacion de contraseñas."""

	__author__ = "EnriqueMoran"

	def __init__(self, letters, numbers, characters, length): 		# Declaration of variables and data used to generate the password
		self.letters = letters
		self.numbers = numbers
		self.characters = characters
		self.length = length			


	def __randomIndex(self, array): 		# Generates a random number between 0 and the array's length that will be use as index for random characters.
		return random.randint(0, len(array)-1)


	def __randomizeArray(self, array): 		#Randomizes the elements of the array.
		return ''.join(random.sample(array,len(array)))


	def weak(self, length):
		""" [EN] Returns a password wich contains only letters, its default length is declared on __init__. 
		[ES] Devuelve una contraseña que contiene sólo letras. La longitud por defecto está declarada en __init__. """
		password = ""
		for i in range(length):
			rand = self.__randomIndex(letters)
			password += letters[rand]
		return password


	def medium(self, length):
		""" [EN] Returns a password wich contains as much letters as numbers. 
		[ES] Devuelve una contraseña que contiene tantas letras como números. """
		halfLength = math.floor(length / 2) 		
		password = ""
		for i in range(int(halfLength)+(length % 2)): 		# Generates half of length as letters
			rand = self.__randomIndex(letters)
			password += letters[rand]
		for i in range(int(halfLength)): 		# Generates the other half of length as numbers
			rand = self.__randomIndex(numbers)
			password += numbers[rand]
		return self.__randomizeArray(password) 		# Mixes two halves


	def strong(self, length):
		""" [EN] Returns a password wich contains letters, numbers and ASCII characters. 
		[ES] Devuelve una contraseña que contiene letras, números y carácteres ASCII. """
		thirdLength = math.floor(length/3)
		password = ""
		for i in range(int(thirdLength) + (length % 3)): 		# Generates third of length as letters
			rand = self.__randomIndex(letters)
			password += letters[rand]
		for i in range(int(thirdLength)): 		# Generates third of length as numbers
			rand = self.__randomIndex(numbers)
			password += numbers[rand]
		for i in range(int(thirdLength)): 		# Generates third of length as ASCII characters
			rand = self.__randomIndex(characters)
			password += characters[rand]		
		return self.__randomizeArray(password) 		# Mixes thirds


if __name__ == "__main__": 		# Initializes PasswordGenerator class
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	characters = ["!", "@", "#", "$", "%", "&", "(", ")", "=", "?", "¿", "¡", ":", ";", "-", "_", "^", "*"]
	length = 8			# Default and minimum length
	generator = PasswordGenerator(letters, numbers, characters, length)

def generate(mode, length = generator.length):
	""" [EN] Generates a password with default length is 8. Mode 0 -> weak, mode 1 -> medium, mode 2 -> strong.
		[ES] Genera una contraseña con una longitud por defecto de 8 caracteres. 
		Modo 0 -> weak (débil), modo 1 -> medium (medio), modo 2 -> strong (fuerte). """		
	if mode == 0:
		print("Password generated: " + generator.weak(length))
	elif mode == 1:
		print("Password generated: " + generator.medium(length))
	elif mode == 2:
		print("Password generated: " + generator.strong(length))
	else:
		print("Mode must be between 0 and 2.")


def settings(): # Not working
	""" [EN] Use your own parameters and lists by adding their items using commas. 
	Example for letter list: a,b,c,d,e.
		[ES] Configura los parámetros y las listas añadiendo sus componentes mediante comas. 
		Ejemplo para lista de letras: a,b,c,d,e."""	
	letters = input("List of letters (separated by comma): ")
	try:
		letterList = []
		for letter in letters:
			letterList.append(letter)
	except:
		print("Incorrect values on list of letters.")

	numbers = input("List of numbers (separated by comma): ")
	try:
		numberList = []
		for number in numbers:
			numberList.append(number)
	except:
		print("Incorrect values on list of number.")

	characters = input("List of characters (separated by comma): ")
	try:
		characterList = []
		for character in characters:
			characterList.append(character)
	except:
		print("Incorrect values on list of character.")

	try:
		newLength = int(input("Length: "))
	except:
		print("Incorrect value for length.")

	try:
		generator = PasswordGenerator(letterList, numberList, characterList, newLength)
	except:
		print("Error creating generator.")


