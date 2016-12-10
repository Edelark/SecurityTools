# -*- coding: utf-8 -*-


import PyPDF2
import os

class decryptor():
    """ [EN] This class contains the necessary methods for DPF decrypt.
    [ES] Esta clase contiene los métodos necesarios para desencriptar PDF.
    Dictionary format (.txt):
    word1
    word2
    word3
    word4
    ..."""

    __author__ = "EnriqueMoran"

    def __init__(self, dictionariesPath, targetPath):
        self.dictionariesPath = dictionariesPath
        self.targetPath = targetPath


    def tryDictionary(self, dictionary):
        """ [EN] Test each password from dictionary.
        [ES] Prueba cada palabra del diccionario dado."""
        pdf = PyPDF2.PdfFileReader(open(self.targetPath, 'rb'))    # Open target PDF                
        file = open(self.dictionariesPath + '\\' + dictionary, "r", encoding="utf8", errors='ignore')    # Open dictionary
        temp = file.read().splitlines() # Split lines, avoiding '\n' on passwords

        password = False # Password not found
        cont = 0

        print("\n--- Testing passwords from: " + dictionary)

        for word in temp:
            passwd = word.rstrip() 
            cont += 1
            if cont % 10000 == 0 and cont != 0:     # Show current password each 10000
                print(str(cont) + " passwords tested. Current password: " + passwd)            
            try:
                if pdf.decrypt(passwd):     # If password is found, stop the script
                    print("\nPassword found: " + passwd)   
                    password = True                 
                    break
                    return password
            except UnicodeEncodeError as error:
                print("Error on password: " + passwd + " Info: " + str(error))
                pass    
        print("\nTested all "+ str(cont) + " words from dictionary: " + dictionary + ". Last password tested: " + passwd)
        if not password:
            print("Password not found.")    
        return password     


if __name__ == "__main__":  # Initializes decryptor class
    decryptor = decryptor('DictionariesPath','TargetPath')    # Replace params with your paths!



def decrypt(dictionariesPath, targetPath):
        """ [EN] Try each dicctionary stored on path.
        [ES] Prueba los diccionarios que se encuentran en el directorio."""
        try:
            password = "Password wasn't found in any dictionary."
            decryptor.dictionariesPath = dictionariesPath
            decryptor.targetPath = targetPath
            for file in os.listdir(dictionariesPath):
                if file.endswith(".txt"):
                    if decryptor.tryDictionary(file):
                        password = "Password was found in : " + file
                        return None     # Stop looking in the rest of dictionaries.
            return password
        except:
            return ("Error. Insert dictionaries path and target's. Remind to use double slash (\)" )
