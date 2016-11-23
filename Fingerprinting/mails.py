"""Made by Antoni Cobos to github.com/Edelark/SecurityTools V1.0 (only source
   files in txt)"""
import re
def find_mail(source, destination):
    """[EN] This function find emails in a document and put all finded emails
    into other file. -> (source,destination)
    [ES] Esta función recibe un archivo donde buscará los emails y un fichero
    destino donde almacenarlos. -> (origen,destino)"""
    try:
        manf = open(source, 'r')
        file_exit = open(destination, 'a+')
        for line in manf:
            string_a = line.strip()
            emails = re.findall('\S+@\S+', string_a)
            for email in emails:
                file_exit.write(email+'\n')
        manf.close()
        file_exit.close()
        print("DONE")
    except ValueError:
        print("The file ", source, " could not be opened...")
