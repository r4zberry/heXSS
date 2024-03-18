
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

usage: heXSS [-h] [-u DOMAIN] [-i HOSTNAME] [-w WORDLIST] [-n NMAP] [-p PORT] [-o OUTPUT] [-db DATABASE]  
             [--subdomain SUBDOMAIN] [-rf REFLECT] [--fuzz FUZZER]

XSS and Vulnerability Scanner

options:
  -h, --help            show this help message and exit
  -u DOMAIN, --domain DOMAIN
                        Specify a domain name
  -i HOSTNAME, --hostname HOSTNAME
                        Specify a target IP address
  -w WORDLIST, --wordlist WORDLIST
                        Specify a filepath wordlist
  -n NMAP, --nmap NMAP  Scans target IP or domain using nmap
  -p PORT, --port PORT  Specify a port
  -o OUTPUT, --output OUTPUT
                        Outputs result to a file, uses .txt by default
  -db DATABASE, --database DATABASE
                        Specify filepath for Vulnerability database in .json or .yaml
  --subdomain SUBDOMAIN
                        Enumerates subdomains from specified wordlist
  -rf REFLECT, --reflect REFLECT
                        Specify parmeter to test for reflected output
  --fuzz FUZZER         Turns parameter fuzzer on, replace parameter with FUZZ
