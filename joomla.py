#!/usr/bin/python
from __future__ import print_function
import requests
import sys
import re
import argparse

try:
	# Python 2.6-2.7 
	from HTMLParser import HTMLParser
except ImportError:
	# Python 3
	from html.parser import HTMLParser

def extract_token(resp):
	match = re.search(r'name="([a-f0-9]{32})" value="1"', resp.text, re.S)	
	if match is None:
		print("[!] Cannot find CSRF token")
		return None
	match2 = re.search("regist", resp.text)	
	if match2 is None:
		print("[!] Cannot find registration")
		return None
	return match.group(1)

def parse_options():	
	parser = argparse.ArgumentParser(description='Joomla Exploit')
	parser.add_argument('url', help='Base URL for Joomla site')
	return parser.parse_args()

def pwn_joomla(options):
	sess = requests.Session()
	print("[-] Joomla Exploit Test")
	resp = sess.get(options.url + "/index.php/component/users/?view=login")	
	token = extract_token(resp)
	if not token:
		return False
	return True

def main():	
	options = parse_options()
	
	if pwn_joomla(options):
		print("[+] SUCCESS:", options.url)
	else:
		print("[!] FAILURE")

if __name__ == "__main__":
	sys.exit(main())

