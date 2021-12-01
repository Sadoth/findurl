#!/usr/bin/python3

import requests 
import argparse

import re
import sys
  
"""
find url on a text
"""
def find_url(string):
    regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = re.findall(regex,string)      
    return urls

def  main() : 
    """
    Custom parser to display usages on error
    """
    class CustomParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)
    
    parser = CustomParser()
    parser.add_argument('file', help='file to analyse')
    args = parser.parse_args()
    data = open(args.file).read()
    print(find_url(data))
    
if __name__ == "__main__":
    main()
