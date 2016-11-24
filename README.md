# SecurityTools
Collections of security tools made by Seville DotNetClub

Folders:

      SecurityTools
          ┣━━━Fingerprinting
                 ┗━━━━mails.py
          ┣━━━Passwords
          ┗━━Pentesting
      
All .py files are documented in two lenguajes, you can use help() method to see that.


## Passwords

Collection of password related methods such as random password generator, PDF decrypter and dicctionaries maker.
Available methods:
 - **generate(mode, length):** Returns a password based on inserted mode and length. Mode 0 -> weak password with only letters,
 Mode 1 -> medium safe level password with numbers and letters, Mode 2 -> strong and safe password with numbers, letters and others ASCII characters. Default length is 8 characters. Example of use: *generate(2)* will return *"Password generated: tja9h!=8"* and *generate(0,5)*  will return *"Password generated: ixwep"*.
 
 - **settings():** Configure class most relevant parameters. List of letters, numbers, characters and default length can be edited.
