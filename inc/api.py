import requests
import re

def getIP():
    url = "http://10.10.244.11/"
    res = requests.get(url = url, proxies={})
    res.encoding = 'gbk'
    ip = re.search("v46ip=\'([^\']*)\'", res.text).group(1)
    return ip

def checkIP(ip):
    url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=checkScanIP&wlanuserip=%s" % (ip)
    res = requests.get(url = url, proxies={})
    status = re.search('\"result\":\"([^\"]*)\"', res.text).group(1)
    if (status == 'ok'):
        account = re.search('\"account\":\"([^\"]*)\"', res.text).group(1)
        return account
    else:
        return False

def checkNetworked():
    url = "https://www.baidu.com" 
    try:
        res = requests.get(url = url,verify=False, proxies={},timeout=3,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61"})
        print("[Internet Connected]:code="+str(res.status_code))
        return True
    except requests.exceptions.Timeout:
        print("[Error]:Internet seems not to be connected...")
        return False
    else:
        return False

def login1(username, password):
    url = "https://p.njupt.edu.cn:802/eportal/portal/login?user_account=&user_password="
    data = {"DDDDD": ",0,%s" % username, "upass": password}
    res=requests.post(url = url, data = data, proxies={})
    return res.text

def login2(username, password):
    url = "http://192.168.168.168/"
    data = {"DDDDD": username, "upass": password, "0MKKey": ""}
    requests.post(url = url, data = data, proxies={})

def login3(username, password):
    #print(login1('101001978006600','123456'))
    url = f"https://p.njupt.edu.cn:802/eportal/portal/login?user_account={username}&user_password={password}" 
    data = {"DDDDD": ",0,%s" % "101001978006600", "upass": "123456"}
    res=requests.post(url = url,  proxies={})
    print("[%s]:" % url + res.text)

def login(username, password):
    login1(username, password)
    login2(username, password)
    login3(username, password)

def loginOutAccount(account):
    url = "http://10.10.244.11:801/eportal/?c=IsOnline&a=logout&account=%s" % account
    requests.get(url = url, proxies={})

def loginOutIP(ip):
    url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=Logout&wlanuserip=%s" % ip
    requests.get(url = url, proxies={})

def loginOutMyself():
    while checkIP(getIP()):
        loginOutAccount(checkIP(getIP()))
        # loginOutIP(getIP())



#http://10.10.244.240:8080/Self/dashboard/tooffline?t=0.5944617235591221&sessionid=5205