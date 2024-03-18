import argparse, ipaddress, requests
import os, re
import nmap
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style 
import json
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import wfuzz, ssl
import importlib
#requries libucrl4 for wfuzz to not error on ssl

ascii =""" 


░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░        
░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓███████▓▒░  
                Vulnerability Scanner 
                Version: 0.12
                Author: R4zberry                                                               
                                                        """

wordlist = ''
def app():
    print(ascii)
    parser = argparse.ArgumentParser(prog='heXSS',description="XSS and Vulnerability Scanner")
    parser.add_argument('-u', '--domain', help="Specify a domain name" , dest="domain")
    parser.add_argument('-i', '--hostname', help="Specify a target IP address" , dest="hostname" )
    parser.add_argument('-w', '--wordlist', help="Specify a filepath wordlist" , dest="wordlist")
    parser.add_argument('-n', '--nmap', help="Scans target IP or domain using nmap" , dest="nmap")
    parser.add_argument('-p', '--port', help="Specify a port" , dest="port")
    parser.add_argument('-o', '--output', help="Outputs result to a file, uses .txt by default" , dest="output")
    parser.add_argument('-db', '--database', help="Specify filepath for Vulnerability database in .json or .yaml" , dest="database")
    # parser.add_argument('-v', '--vulnerability',help="Scans target IP or domain for vulnerabilities" , dest="vulnscan")
    parser.add_argument( '--subdomain',help="Enumerates subdomains from specified wordlist" , dest="subdomain")
    parser.add_argument( '-rf','--reflect',help="Specify parmeter to test for reflected output" , dest="reflect" )
    parser.add_argument( '--fuzz',help="Turns parameter fuzzer on, replace parameter with FUZZ" , dest="fuzzer", default=True)
    args = parser.parse_args()

    if  not args.domain and not args.hostname and not args.nmap and not args.reflect:
        parser.error("Please specify a domain.")
    if args.domain:
        #sends http request to domain and returns
        #parameters from the response by default 
        #parses response for anything that comes after "/(word)?" using regex
        #parses response for anything inside the double quotes in action=""
        #parses response for anything inside the double quotes in href=""
        


        print('Target: ' + Fore.MAGENTA + args.domain)
        response = requests.get(args.domain)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # parameters = soup.find_all("/.?")
            # endpoints = soup.find_all("href=[a-zA-Z]") + soup.findAll("action=[a-z]")
            print( Fore.YELLOW + 'Endpoints in form data:')
            for endpoint in soup.findAll('form'):
                endpoints = endpoint.get('action')
                print(Fore.GREEN + endpoints)
            print(Fore.YELLOW +'Parameters in webpage:')
            for parameter in soup.findAll('a'):
                parameters = parameter.get('href')
                print(Fore.GREEN + parameters )
            
            # for endpoint in endpoints:
            #     print(endpoint.text)
                
    if args.hostname:
        print(args.hostname)
        response = requests.get(args.domain)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # parameters = soup.find_all("/.?")
            # endpoints = soup.find_all("href=[a-zA-Z]") + soup.findAll("action=[a-z]")
            print( Fore.YELLOW + 'Endpoints in form data:')
            for endpoint in soup.findAll('form'):
                print(Fore.GREEN + endpoint.get('action'))
            print(Fore.YELLOW +'Parameters in webpage:')
            for parameter in soup.findAll('a'):
                print(Fore.GREEN +  parameter.get('href'))
            # parameters = soup.findAll("/(.+?)?")
            # endpoints = soup.findAll("href=(.+?)") + soup.findAll("action=(.+?)")
            # print(soup + parameters + endpoints)
            
    if args.wordlist:
        if os.path.exists(args.wordlist):
            dict={}
            with open(args.wordlist) as  f:
                for line in f:
                    dict = line.split()




           #match os get requests with user input
            #to find wordlist.

    if  args.nmap:
        ip = args.nmap
        nm = nmap.PortScanner()
        nm.scan(ip, '1-200', '-sV -sS')
        results = nm[ip]['tcp'].keys()
        print(results)

    if args.nmap and args.port:
        ip = args.nmap
        nm.scan(ip, args.port, '-sV -sS' )
        results = nm[ip].keys()
        state = nm[ip].state()
        print(results)
    if  args.nmap and args.output:
        file = args.output
        ip = args.nmap
        nm = nmap.PortScanner()
        nm.scan(ip, '1-200', '-sV -sS')
        results = nm[ip].keys()
        f = open(file, "a")
        results = str(results)
        f.write(results)

    if args.nmap and args.port and args.output:
        nm.scan(ip, args.port, '-sV -sS' )
        results = nm.scan(ip, args.port, '-sV -sS' ) 
        print(nm[ip].keys())
        state = nm[ip].state()
        f = open(file, "a")
        f.write(results)

        
#TO-DO: add a way to make scan results more readable 
#could possibly just parse json 

        #use python nmap to scan top 1000 ports
        #using syn packets and return services + vulnerabilities

        #takes up to 4 digit integer and appends it as port to hostname
    
    #     #takes string and places it in curl request 
    #     #returns search data as response 
    if args.domain and args.output:
        path = args.output
        f = open(path , "a")
        f.write("Parameters: " + "\n")
        for parameter in parameters:
            f.write(parameters+ "\n")
        f.write("Endpoints: "+ "\n")
        for endpoint in endpoints:
            f.write(endpoints + "\n")
        f.close()

    #     #writes data to filename.txt 
    #     #in the directory 

    # if args.database:
    #     file = Path(args.database)
    #     # db_path = input("Choose a filename for database file: ")
    #     # if os.exists(db_path):
    #     with open(args.database) as database:
    #         db_contents = database.read()
    #         print(db_contents)


    #     #matches os get request with user inputted path
    #     #to find database JSON or YAML
    # if args.hostname and args.scan:
    #     #perform vuln scan using nmap + database
    # if args.domain and args.scan:
    #      #searches for dns records for ip if domain specified
    #     #if there is none it quits and errors
    # if args.scan and args.database:
    #     ##matches os get request with user inputted path
    #     #to find database JSON or YAML
    #     #uses database file for nmap scan 
    if args.subdomain and args.wordlist:
        subdomain= ''
        for subdomain in f:
            url = f"https://{subdomain}.{args.subdomain}"
            try:
                requests.get(url)
                print(f'[*]{url}')
            except requests.ConnectionError:
                pass
    if args.domain and args.subdomain and args.wordlist and args.output:
        subdomain = '' 
        for subdomain in f:
            file = open(args.output,"a")
            url = f"https://{subdomain}.{args.subdomain}"
            try:
                requests.get(url)
                f.write(f'[*]{url}')
            except requests.ConnectionError:
                pass
    #     #takes domain and appends wordlist selection to the beginning with '.'
    #if args.fuzzer:
        
    #     #takes the url and replaces *hexss* with wordlist selection
    #***consider using urllib and parse instead of wfuzz to fuzz URL parameters ***
    if args.fuzzer and args.wordlist:
        for r in wfuzz.fuzz(url=args.fuzzer, hc=[404], payloads=[("file",dict(fn=args.wordlist))]):
            print(r)
    if args.fuzzer and args.wordlist and args.output:
        for r in wfuzz.fuzz(url=args.fuzzer, hc=[404], payloads=[("file",dict(fn=args.wordlist))]):
            f = open(args.output,"a")
            f.write(r)
        # data = re.compile(r'*(.*)*')
        # fuzz = data.finditer(args.domain)
        # for fuzz in fuzz:
        #     print(fuzz)
#*ADDED*: add Wfuzz, urlparse  0.12 otw

#test parameters for reflected input by importing url parse 
#sending requests with test payload 'hexss' and parsing the
#response for 'hexss'. if it matches, display parameter + hexss
# to user
    if args.reflect:
        response = requests.get(args.reflect , params='hexss')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            reflection = soup.findAll('hexss')
            print(reflection, response.text)
            #this feature needs to be tested.
            #try it on a vulnerable application to see if it will reflect input
            #if it works, it will be in v0.13




#subdomain and fuzzer ready to be tested. 0.12 almost completed
#may switch to requests instead of wfuzz 





        



                                                                        


if __name__ == "__main__":
   
    app()
   