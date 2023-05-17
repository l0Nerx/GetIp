import socket
import smtplib as smtp
from getpass import getpass
import requests
from requests import get
from pyfiglet import Figlet
import folium
import smtplib
import os
from email.mime.text import MIMEText



def get_ip_by_hostname():
	preview_text = Figlet(font='slant')
	print(preview_text.renderText('getip'))

	try:
		return f"Hostname: {hostname}\nIp: {socket.gethostbyname(hostname)}"
	except socket.gaierror as error:
		return  f"Invalid Hostname {error}"

def main():
	# print(get_ip_by_hostname())
	pass

if __name__ == '__main__':
	main()


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
        
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')
        
        
def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('whois?'))
    ip = input('Please enter a target URL: ')
    
    get_info_by_ip(ip=ip)
    
    
if __name__ == '__main__':
	main()
