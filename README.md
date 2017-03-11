# SecurityTools
Collections of security tools made by Seville DotNetClub

Folders:

      SecurityTools
          ┣━━━Fingerprinting
          ┃      ┗━━━━mails.py
          ┣━━━Passwords
          ┃      ┣━━━passwordGenerator.py
          ┃      ┗━━━━PDFdecryptor.py
          ┗━━Pentesting
      
All .py files are documented in two lenguajes, you can use help() method to see that.


## Passwords
Collection of password related methods such as random password generator, PDF decrypter and dicctionaries maker.

### passwordGenerator.py
Available methods:
 - **generate(mode, length):** Returns a password based on inserted mode and length. Mode 0 -> weak password with only letters,
 Mode 1 -> medium safe level password with numbers and letters, Mode 2 -> strong and safe password with numbers, letters and others ASCII characters. Default length is 8 characters. Example of use: *generate(2)* will return *"Password generated: tja9h!=8"* and *generate(0,5)*  will return *"Password generated: ixwep"*.
 
 - **settings():** Configure class most relevant parameters. List of letters, numbers, characters and default length can be edited.

### PDFdecryptor.py
Available methods:
 - **decrypt(dictionariesPath, targetPath):** Returns PDF password from a set of dictionaries given as folder. Version 1.0 works on UTF-8 encoded PDF and .txt file dictionaries. 
Example of use:
<pre>
decrypt("C:\\Users\\Enrique\\Desktop\\test\\dictionaries", "C:\\Users\\Enrique\\Desktop\\test\\encryptedPDF.pdf")
--- Testing passwords from: dictionary1.txt
10000 passwords tested. Current password: amnesty
--- Testing passwords from: dictionary2.txt
Password found: surculous
Tested all 579 words from dictionary: dictionary2.txt. Last password tested: surculous
</pre>

## Fingerpronting
Collection of tools to extract information from various sources.

### mails.py
Available methods:
 - **find_mail(source,destination): ** This function find emails in a document and put all finded emails
    into other file. -> (source,destination)
