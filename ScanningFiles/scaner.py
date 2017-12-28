#############################################################
#Recibe la ruta de un fichero y lo analiza con un antivirus.#
#############################################################
import requests
import webbrowser
openWeb = False #if True, open the result in a browser, if False, show the results in console
letIn = True #loop var
api = "" #Public API VirusTotal
#### Asking API ###
while(letIn): #ask to the user about his/her API
    print("Please, insert your VIRUSTOTAL API")
    api = input()
    if(len(api) != 64): #filter only valid APIs
        print("Please, insert a valid API, It must have 64 characters")
    else: letIn = False
#------------------
letIn = True
while(letIn):
    ### Asking about the file path ###
    letIn = True
    while(letIn):
        print("Where is the file located?: ")
        path = input() #path is the absolute path to the file.
        containExt = len(path)-path.find(".") #It is a light way to see if the path contain the file extension
        if(containExt != 4):
            print("Please, you must to include the file extension in the path, i.e: hello.txt")
        else:
            letIn = False
    path = path..replace("\\", "/")
    #---------------------------------

    ### Asking about how to show the results ###
    letIn = True
    while(letIn):
        print("Do you want to open the result in the browser? Y/N")
        say = input()
        if(say == "Y" or say == "y"):
            openWeb = True
            letIn = False
        elif(say == "N" or say == "n"):
            letIn = False
            openWeb = False
        else:
            print("Please, type Y or N")
    #--------------------------------------------
            
    ### Sending the file to VirusTotal ###
    params = {'apikey': api} #params to the http petition
    files = {'file': (path, open(path, 'rb'))} # open the file as read-bit
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
    json_response = response.json()
    if(openWeb):
        webbrowser.open(json_response["permalink"])
    else:
        params = {'apikey': api, 'resource': json_response["resource"]}
        headers = {"Accept-Encoding": "gzip, deflate","User-Agent" : "gzip,  My Python requests library example client or username"}
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)
        json_response = response.json()
        print("The file has been analyzed with " + str(json_response["total"]) + " antivirus and they have been found " + str(json_response["positives"]) + " Malwares")
    print("Do you want to analize another file? Y/N")
    say = input()
    if(say == "Y" or say == "y"):
        letIn = True
    elif(say == "N" or say == "n"):
        letIn = False
    else:
        print("Please, type Y or N")
