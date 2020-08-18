#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import re
import requests
import execjs
import datetime
import time
import urllib.parse
#############################################################包
ticks = time.time()
print("当前时间戳为:")
s=str(round(ticks, 3))
s1=s[0:10]
s2=s[11:14]
print(s1+s2)
print(
datetime.datetime.now().year,
datetime.datetime.now().month,
datetime.datetime.now().day)
year=datetime.datetime.now().year
month=datetime.datetime.now().month
day=datetime.datetime.now().day
if(month<10):
    month='0'+str(month)
if(day<10):
    day='0'+str(day)
#############################################################日期
print("程序开启")
APPID = "5812981499622390"     #APPID默认
# sid="8888888"
# #学号
# spass="999999999"
# #密码
#ff='{"USER_NAME":"名字","DEPT_CODE":"319","DEPT_NAME":"人工智能学院","XB":"男","SJHM":"888888888","SFYFS":"4","JTCYJKQK_DISPLAY":"无以上情况","JCGYQFKZDDQGWRY":"0","JTCYJKQK":"0","STJKZK":"1","JZSJHM":"888888888","JTZZDQ_DISPLAY":"8888区","JCGYSHQZBL_DISPLAY":"未接触过","JCGYSHQZBL":"0","HJSFLX":"0","XZZSF_DISPLAY":"广东省","SFZZSXDWSS_DISPLAY":"","SFWZZGRZ_DISPLAY":"否","SFZZCJSX":"0","SFYFX":"3","SSFJH":"每个人不同","FDYSJHM":"88888","CQWYQFKZDDQ":"0","HJSFLX_DISPLAY":"否","SFYFS_DISPLAY":"从未离深","JCGYQFKZDDQGWRY_DISPLAY":"否","XZZSF":"440000","BZRSJHM":"888888","SFJFFH":"0","SFWZXS":"1","SFJSJJGC_DISPLAY":"否","SFJSJJGC":"0","FDYXM":"88888","SFZZCJSX_DISPLAY":"否","JTZZSF":"440000","SFYFX_DISPLAY":"未确定返校时间","SFJFFH_DISPLAY":"否","SSXQ_DISPLAY":888888","NL":"19","STJKZK_DISPLAY":"健康","SSXQ":"4","STYXZK_DISPLAY":"","DWDZ":"8888","JG":"88888","BZRXM":"88888","XZZXXDZ":"888888","XZZDQ":"440304","STYCZK_DISPLAY":"","XZZCS_DISPLAY":"8888","SFJSJTGC":"0","JTZZSF_DISPLAY":"广东省","JTZZXXDZ":"8888888","XZZDQ_DISPLAY":"88888","SSFJH_DISPLAY":"210","FHTJGJ_DISPLAY":"","OPERATE_DATE":"2020-07-14 14:39:49","BJ":"19软件1","SSLD":"408","SSLD_DISPLAY":"88888","SFWZXS_DISPLAY":"是","USER_ID":"888888","XZZCS":"440300","CQWYQFKZDDQ_DISPLAY":"否","SFWZZGRZ":"0","JTZZCS_DISPLAY":"88888","OPERATE_USER":"88888","JTZZCS":"440300","REPORT_DATE":"'+str(year)+'-'+str(month)+'-'+str(day)+'","SXFS_DISPLAY":"","SFJSJTGC_DISPLAY":"否","JTZZDQ":"440304","WID":"","ZSDZ":"","SXFS":"","SFZZSXDWSS":"","FSSJ":"","FXSJ":"","FHTJGJ":"","QTXYSMDJWQK":"","SSSQ":"","XSQBDSJ":"","JSJJGCJTSJ":"","JSJTGCJTSJ":"","JSJJJTGCYY":"","STYCZK":"","STYXZK":"","QYTZWTW":"","QYTWSTW":"","DTZSTW":""}'
## 提交的表单，表单自己抓包获取
############################################################或是通过数组来实现多人打卡
id = ['88888888', '88888888','88888888']
#学号数组
pword = ['88888888', '88888888', '88888888']
#对应的密码数组
ff = ['{"USER_NAME":"名字","DEPT_CODE":"319","DEPT_NAME":"人工智能学院","XB":"男","SJHM":"888888888","SFYFS":"4","JTCYJKQK_DISPLAY":"无以上情况","JCGYQFKZDDQGWRY":"0","JTCYJKQK":"0","STJKZK":"1","JZSJHM":"888888888","JTZZDQ_DISPLAY":"8888区","JCGYSHQZBL_DISPLAY":"未接触过","JCGYSHQZBL":"0","HJSFLX":"0","XZZSF_DISPLAY":"广东省","SFZZSXDWSS_DISPLAY":"","SFWZZGRZ_DISPLAY":"否","SFZZCJSX":"0","SFYFX":"3","SSFJH":"每个人不同","FDYSJHM":"88888","CQWYQFKZDDQ":"0","HJSFLX_DISPLAY":"否","SFYFS_DISPLAY":"从未离深","JCGYQFKZDDQGWRY_DISPLAY":"否","XZZSF":"440000","BZRSJHM":"888888","SFJFFH":"0","SFWZXS":"1","SFJSJJGC_DISPLAY":"否","SFJSJJGC":"0","FDYXM":"88888","SFZZCJSX_DISPLAY":"否","JTZZSF":"440000","SFYFX_DISPLAY":"未确定返校时间","SFJFFH_DISPLAY":"否","SSXQ_DISPLAY":888888","NL":"19","STJKZK_DISPLAY":"健康","SSXQ":"4","STYXZK_DISPLAY":"","DWDZ":"8888","JG":"88888","BZRXM":"88888","XZZXXDZ":"888888","XZZDQ":"440304","STYCZK_DISPLAY":"","XZZCS_DISPLAY":"8888","SFJSJTGC":"0","JTZZSF_DISPLAY":"广东省","JTZZXXDZ":"8888888","XZZDQ_DISPLAY":"88888","SSFJH_DISPLAY":"210","FHTJGJ_DISPLAY":"","OPERATE_DATE":"2020-07-14 14:39:49","BJ":"19软件1","SSLD":"408","SSLD_DISPLAY":"88888","SFWZXS_DISPLAY":"是","USER_ID":"888888","XZZCS":"440300","CQWYQFKZDDQ_DISPLAY":"否","SFWZZGRZ":"0","JTZZCS_DISPLAY":"88888","OPERATE_USER":"88888","JTZZCS":"440300","REPORT_DATE":"'+str(year)+'-'+str(month)+'-'+str(day)+'","SXFS_DISPLAY":"","SFJSJTGC_DISPLAY":"否","JTZZDQ":"440304","WID":"","ZSDZ":"","SXFS":"","SFZZSXDWSS":"","FSSJ":"","FXSJ":"","FHTJGJ":"","QTXYSMDJWQK":"","SSSQ":"","XSQBDSJ":"","JSJJGCJTSJ":"","JSJTGCJTSJ":"","JSJJJTGCYY":"","STYCZK":"","STYXZK":"","QYTZWTW":"","QYTWSTW":"","DTZSTW":""}',
      '{"USER_NAME":"名字","DEODE":"319","DEPT_NAME":"人工智能学院","XB":"男","SJHM":"88888888","SFYFS":"4","JTCYJKQK_DISPLAY":"无以上情况","JCGYQFKZDDQGWRY":"0","JTCYJKQK":"0","STJKZK":"1","JZSJHM":"8888888","JTZZDQ_DISPLAY":"88888","JCGYSHQZBL_DISPLAY":"未接触过","JCGYSHQZBL":"0","HJSFLX":"0","XZZSF_DISPLAY":"广东省","SFZZSXDWSS_DISPLAY":"","SFWZZGRZ_DISPLAY":"否","SFZZCJSX":"0","SFYFX":"3","SSFJH":"每个人不同","FDYSJHM":"888888","CQWYQFKZDDQ":"0","HJSFLX_DISPLAY":"否","SFYFS_DISPLAY":"从未离深","JCGYQFKZDDQGWRY_DISPLAY":"否","XZZSF":"440000","BZRSJHM":"88888","SFJFFH":"0","SFWZXS":"1","SFJSJJGC_DISPLAY":"否","SFJSJJGC":"0","FDYXM":"88888","SFZZCJSX_DISPLAY":"否","JTZZSF":"440000","SFYFX_DISPLAY":"未确定返校时间","SFJFFH_DISPLAY":"否","SSXQ_DISPLAY":"88888","NL":"20","STJKZK_DISPLAY":"健康","SSXQ":"4","STYXZK_DISPLAY":"","DWDZ":"888888","JG":"88888","BZRXM":"88888","XZZXXDZ":"8888","XZZDQ":"440303","STYCZK_DISPLAY":"","XZZCS_DISPLAY":"88888","SFJSJTGC":"0","JTZZSF_DISPLAY":"广东省","JTZZXXDZ":"8888","XZZDQ_DISPLAY":"88888","SSFJH_DISPLAY":"208","FHTJGJ_DISPLAY":"","OPERATE_DATE":"2020-07-14 18:10:31","BJ":"19软件1","SSLD":"408","SSLD_DISPLAY":"88888","SFWZXS_DISPLAY":"是","USER_ID":"88888","XZZCS":"440300","CQWYQFKZDDQ_DISPLAY":"否","SFWZZGRZ":"0","JTZZCS_DISPLAY":"88888","OPERATE_USER":"888888","JTZZCS":"440300","REPORT_DATE":"'+str(year)+'-'+str(month)+'-'+str(day)+'","SXFS_DISPLAY":"","SFJSJTGC_DISPLAY":"否","JTZZDQ":"440303","WID":"","ZSDZ":"","SXFS":"","SFZZSXDWSS":"","FSSJ":"","FXSJ":"","FHTJGJ":"","QTXYSMDJWQK":"","SSSQ":"","XSQBDSJ":"","JSJJGCJTSJ":"","JSJTGCJTSJ":"","JSJJJTGCYY":"","STYCZK":"","STYXZK":"","QYTZWTW":"","QYTWSTW":"","DTZSTW":""}',
      '{"USER_NAME":"名字","DEPT_CODE":"319","DEPT_NAME":"人工智能学院","XB":"男","SJHM":"8888888","SFYFS":"4","JTCYJKQK_DISPLAY":"无以上情况","JCGYQFKZDDQGWRY":"0","JTCYJKQK":"0","STJKZK":"1","JZSJHM":"888888","JTZZDQ_DISPLAY":"88888区","JCGYSHQZBL_DISPLAY":"未接触过","JCGYSHQZBL":"0","HJSFLX":"0","XZZSF_DISPLAY":"广东省","SFZZSXDWSS_DISPLAY":"","SFWZZGRZ_DISPLAY":"否","SFZZCJSX":"0","SFYFX":"3","SSFJH":"每个人不同","FDYSJHM":"88888","CQWYQFKZDDQ":"0","HJSFLX_DISPLAY":"否","SFYFS_DISPLAY":"从未离深","JCGYQFKZDDQGWRY_DISPLAY":"否","XZZSF":"440000","BZRSJHM":"88888888","SFJFFH":"0","SFWZXS":"1","SFJSJJGC_DISPLAY":"否","SFJSJJGC":"0","FDYXM":"888888","SFZZCJSX_DISPLAY":"否","JTZZSF":"440000","SFYFX_DISPLAY":"未确定返校时间","SFJFFH_DISPLAY":"否","SSXQ_DISPLAY":"8888888","NL":"21","STJKZK_DISPLAY":"健康","SSXQ":"1","STYXZK_DISPLAY":"","DWDZ":"888888","JG":"8888","BZRXM":"8888","XZZXXDZ":"88888","XZZDQ":"440303","STYCZK_DISPLAY":"","XZZCS_DISPLAY":"88888","SFJSJTGC":"0","JTZZSF_DISPLAY":"广东省","JTZZXXDZ":"8888","XZZDQ_DISPLAY":"88888","SSFJH_DISPLAY":"1105","FHTJGJ_DISPLAY":"","OPERATE_DATE":"2020-08-17 13:23:47","BJ":"888888","SSLD":"103","SSLD_DISPLAY":"888888","SFWZXS_DISPLAY":"是","USER_ID":"188888","XZZCS":"440300","CQWYQFKZDDQ_DISPLAY":"否","SFWZZGRZ":"0","JTZZCS_DISPLAY":"88888","OPERATE_USER":"88888","JTZZCS":"440300","REPORT_DATE":"'+str(year)+'-'+str(month)+'-'+str(day)+'","SXFS_DISPLAY":"","SFJSJTGC_DISPLAY":"否","JTZZDQ":"440303","WID":"","ZSDZ":"","SXFS":"","SFZZSXDWSS":"","FSSJ":"","FXSJ":"","FHTJGJ":"","QTXYSMDJWQK":"","SSSQ":"","XSQBDSJ":"","JSJJGCJTSJ":"","JSJTGCJTSJ":"","JSJJJTGCYY":"","STYCZK":"","STYXZK":"","QYTZWTW":"","QYTWSTW":"","DTZSTW":""}']
#表单数组，表单自己抓包获取
n=0
while n <=2:
 print("#############################################################第"+str(n)+"个#############################################################")
 #############################################################一、获取route、JSESSIONID、lt、pwdDefaultEncryptSalt
 print("一、获取route、JSESSIONID、lt、pwdDefaultEncryptSalt")
 url = "https://getman.cn/api/request"
 data = {
    "url": "https://authserver.szpt.edu.cn/authserver/login?service=https://ehall.szpt.edu.cn:443/login?service=https://ehall.szpt.edu.cn/new/index.html",
    "method": "GET",
    "body": "",
    "header[Host]":"authserver.szpt.edu.cn",
    "header[Connection]":"keep-alive",
    "header[Cache-Control]":"max-age=0",
    "header[Upgrade-Insecure-Requests]":'1',
    "header[User-Agent]":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59",
    "header[Accept]":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "header[Sec-Fetch-Site]":"same-site",
    "header[Sec-Fetch-Mode]":"navigate",
    "header[Sec-Fetch-User]":"?1",
    "header[Sec-Fetch-Dest]":"document",
    "header[Referer]":"https://authserver.szpt.edu.cn/authserver/login?service=https%3A%2F%2Fehall.szpt.edu.cn%3A443%2Fpublicappinternet%2Fsys%2Fszptpubxsjkxxbs%2F*default%2Findex.do",
    "header[Accept-Encoding]":"gzip, deflate, br",
    "header[Accept-Language]":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",

 }
 res = requests.post(url=url, data=data)

 print(res.text)
 s = res.text
 ####################
 # a = r'route=(.*?),JSESSIONID='
 # slotList = re.findall(a, s)
 # route = slotList[0]
 # print('route="'+route+'"')
 ####################
 b = r'JSESSIONID=(.*?);'
 slotList = re.findall(b, s)
 JESSIONID = slotList[0]
 print('JESSIONID="'+JESSIONID+'"')
 ####################
 c = r'LT-(.*?)-cas'
 slotList = re.findall(c, s)
 lt = "LT-" + slotList[0] + "-cas"
 print('lt="'+lt+'"')
 ####################
 d = r'pwdDefaultEncryptSalt(.*?);'
 slotList = re.findall(d, s)
 pwd = slotList[0]
 e = r'"(.*?)\\"'
 slotList = re.findall(e, pwd)
 pwdDefaultEncryptSalt = slotList[0]
 print(pwdDefaultEncryptSalt)
 #print(pwdDefaultEncryptSalt)
 #############################################################



 #############################################################一、获取route、JSESSIONID、lt、pwdDefaultEncryptSalt

 #############################################################判断是否需要验证码，如果ture是需要，false是不需要

 url = "https://getman.cn/api/request"
 data = {
    "url":"https://authserver.szpt.edu.cn/authserver/needCaptcha.html?username="+id[n]+"&pwdEncrypt2=pwdEncryptSalt&_="+s1+s2,
    "method":"GET",
    "body":"",
    "header[Host]":"authserver.szpt.edu.cn",
    "header[Connection]":"keep-alive",
    "header[Accept]": "text/plain, */*; q=0.01",
    "header[User-Agent]":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40",
    "header[X-Requested-With]": "XMLHttpRequest",
    "header[Sec-Fetch-Site]":"same-origin",
    "header[Sec-Fetch-Mode]":"cors",
    "header[Sec-Fetch-Dest]":"empty",
    "header[Referer]":"https://authserver.szpt.edu.cn/authserver/login?service=https%3A%2F%2Fehall.szpt.edu.cn%3A443%2Fpublicappinternet%2Fsys%2Fszptpubxsjkxxbs%2F*default%2Findex.do",
    "header[Accept-Encoding]":"gzip, deflate, br",
    "header[Accept-Language]":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "header[Cookie]":"JSESSIONID="+JESSIONID,
 }

 res = requests.post(url=url,data=data)

 print(res.text)
 s = res.text
  ####################
 a = r'"body":"(.*?)"'
 slotList = re.findall(a, s)
 body = slotList[0]
 print('body="'+body+'"')
 #############################################################

 #############################################################二、通过pwdDefaultEncryptSalt作为key加密密码
 print("二、pwdDefaultEncryptSalt作为key加密密码")
 def get_des_psswd(data, key):
    jsstr = get_js()
    ctx = execjs.compile(jsstr) #加载JS文件
    return (ctx.call('encryptAES', data, key))  #调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数



 def get_js():
    f = open("encrypt.js", 'r', encoding='utf-8') # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr+line
        line = f.readline()
    return htmlstr


 password=get_des_psswd(pword[n], pwdDefaultEncryptSalt)
 print(password)
 #############################################################
 #############################################################转码，顺便把最后一个等号删除
 p=password.rstrip('=')
 print(p)
 ##转码##
 str = p
 # 先进行gb2312编码
 str = str.encode('gb2312')
 password = urllib.parse.quote(str)
 print( password)
 #############################################################
 #############################################################三、登录
 print("三、登录")
 print(id[n],pword[n])
 url = "https://getman.cn/api/request"
 data = {
    "url":"https://authserver.szpt.edu.cn/authserver/login?service=https%3A%2F%2Fehall.szpt.edu.cn%3A443%2Fpublicappinternet%2Fsys%2Fszptpubxsjkxxbs%2F*default%2Findex.do",
    "method":"POST",
    "body":"username="+id[n]+"&password="+password+"&lt="+lt+"&dllt=userNamePasswordLogin&execution=e1s1&_eventId=submit&rmShown=1",
    "header[Host]":"authserver.szpt.edu.cn",
    "header[Connection]":"keep-alive",
    "header[Content-Length]":"278",
    "header[Cache-Control]":"max-age=0",
    "header[Upgrade-Insecure-Requests]":'1',
    "header[Origin]":"https://authserver.szpt.edu.cn",
    "header[Content-Type]":"application/x-www-form-urlencoded",
    "header[User-Agent]":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61",
    "header[Accept]":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "header[Sec-Fetch-Site]":"same-origin",
    "header[Sec-Fetch-Mode]":"navigate",
    "header[Sec-Fetch-User]":"?1",
    "header[Sec-Fetch-Dest]":"document",
    "header[Referer]":"https://authserver.szpt.edu.cn/authserver/login?service=https%3A%2F%2Fehall.szpt.edu.cn%3A443%2Fpublicappinternet%2Fsys%2Fszptpubxsjkxxbs%2F*default%2Findex.do",
    "header[Accept-Encoding]":"gzip, deflate, br",
    "header[Accept-Language]":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "header[Cookie]":"JSESSIONID="+JESSIONID,
 }

 res = requests.post(url=url,data=data)

 print(res.text)
 s = res.text
 # print(s)

 f = r'code":(.*?),'
 slotList = re.findall(f, res.text)
 code = slotList[0]
 #############################################################
 if code=='200':
    print("登录失败，200错误，频繁登录，请稍后重试，ST获取失败")
    n+=1
    # s = s.encode('utf-8').decode("unicode_escape")
    # print(s)
    g = r'auth_error(.*?)<'
    slotList = re.findall(g, s)
    g1 = slotList[0] + "<"
    i = r'>(.*?)<'
    slotList = re.findall(i, g1)
    error = slotList[0]
    error = error.encode('utf-8').decode("unicode_escape")
    print(error)
 if code =='302':
    print("登录成功")
    f = r'ST-(.*?)-cas'
    slotList = re.findall(f, res.text)
    ST = "ST-"+slotList[0]+"-cas"
    print(ST)
    g = r'TGT-(.*?)-cas'
    slotList = re.findall(g, res.text)
    TGT = "TGT-" + slotList[0] + "-cas"
    print(TGT)
    #############################################################四、校验ST
    print("四、校验ST")
    url = "https://getman.cn/api/request"
    data = {
    "url": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/*default/index.do?ticket="+ST,
    "method": "GET",
    "body": "",
    "header[Host]":"ehall.szpt.edu.cn",
    "header[Connection]":"keep-alive",
    "header[Cache-Control]":"max-age=0",
    "header[Upgrade-Insecure-Requests]":'1',
    "header[User-Agent]":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64",
    "header[Accept]":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "header[Sec-Fetch-Site]":"same-site",
    "header[Sec-Fetch-Mode]":"navigate",
    "header[Sec-Fetch-User]":"?1",
    "header[Sec-Fetch-Dest]":"document",
    "header[Referer]":"https://authserver.szpt.edu.cn/authserver/login?",
    "header[Accept-Encoding]":"gzip, deflate, br",
    "header[Accept-Language]":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
     }
    res = requests.post(url=url, data=data)
    print(res.text)
    f = r'MOD_AUTH_CAS=(.*?);'
    slotList = re.findall(f, res.text)
    code = slotList[0]
    #############################################################
    if code is None or code == '':
        print("MOD空,失效重新获取")
        #############################################################二次获取ST，一般来说获取第二就好
        print("二次请求获取ST")
        url = "https://getman.cn/api/request"
        data = {
            "url": "https://authserver.szpt.edu.cn/authserver/login?service=https%3A%2F%2Fehall.szpt.edu.cn%3A443%2Fpublicappinternet%2Fsys%2Fszptpubxsjkxxbs%2F*default%2Findex.do",
            "method": "GET",
            "body": "",
            "header[Host]": "authserver.szpt.edu.cn",
            "header[Connection]": "keep-alive",
            "header[Cache-Control]": "max-age=0",
            "header[Upgrade-Insecure-Requests]": "1",
            "header[User-Agent]": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64",
            "header[Accept]": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "header[Sec-Fetch-Site]": "same-site",
            "header[Sec-Fetch-Mode]": "navigate",
            "header[Sec-Fetch-User]": "?1",
            "header[Sec-Fetch-Dest]": "document",
            "header[Referer]": "https://authserver.szpt.edu.cn/authserver/login?service=https%3A%2F%2Fehall.szpt.edu.cn%3A443%2Fpublicappinternet%2Fsys%2Fszptpubxsjkxxbs%2F*default%2Findex.do",
            "header[Accept-Encoding]": "gzip, deflate, br",
            "header[Accept-Language]": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "header[Cookie]": "CASTGC="+TGT+"; JSESSIONID="+JESSIONID
        }
        res = requests.post(url=url, data=data)
        print(res.text)
        f = r'ST-(.*?)-cas'
        slotList = re.findall(f, res.text)
        ST = "ST-" + slotList[0] + "-cas"
        print(ST)
    else:
        print("不为空，校验成功")
    #############################################################

    #############################################################四、校验ST
    print("二次校验ST")
    url = "https://getman.cn/api/request"
    data = {
    "url": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/*default/index.do?ticket="+ST,
    "method": "GET",
    "body": "",
    "header[Host]":"ehall.szpt.edu.cn",
    "header[Connection]":"keep-alive",
    "header[Cache-Control]":"max-age=0",
    "header[Upgrade-Insecure-Requests]":'1',
    "header[User-Agent]":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64",
    "header[Accept]":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "header[Sec-Fetch-Site]":"same-site",
    "header[Sec-Fetch-Mode]":"navigate",
    "header[Sec-Fetch-User]":"?1",
    "header[Sec-Fetch-Dest]":"document",
    "header[Referer]":"https://authserver.szpt.edu.cn/authserver/login?",
    "header[Accept-Encoding]":"gzip, deflate, br",
    "header[Accept-Language]":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
     }
    res = requests.post(url=url, data=data)
    print(res.text)
    f = r'MOD_AUTH_CAS=(.*?);'
    slotList = re.findall(f, res.text)
    code = slotList[0]
    if code is None or code == '':
        print("MOD空,失效重新获取")
    else:
        print("不为空,校验成功")
        print(code)
        f = r'ST-(.*?)-cas'
        slotList = re.findall(f, res.text)
        ST = "ST-" + slotList[0] + "-cas"
        print(ST)
    #############################################################

    #############################################################五、获取_WEU-1
    print("五、获取_WEU-1")
    url = "https://getman.cn/api/request"
    data = {
            "url": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/*default/index.do",
            "method": "GET",
            "body": "",
            "header[Host]": "ehall.szpt.edu.cn",
            "header[Connection]": "keep-alive",
            "header[Cache-Control]": "max-age=0",
            "header[Upgrade-Insecure-Requests]": "1",
            "header[User-Agent]": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61",
            "header[Accept]": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "header[Sec-Fetch-Site]": "same-site",
            "header[Sec-Fetch-Mode]": "navigate",
            "header[Sec-Fetch-User]": "?1",
            "header[Sec-Fetch-Dest]": "document",
            "header[Referer]": "https://authserver.szpt.edu.cn/authserver/login?service=https%3A%2F%2Fehall.szpt.edu.cn%3A443%2Fpublicappinternet%2Fsys%2Fszptpubxsjkxxbs%2F*default%2Findex.do",
            "header[Accept-Encoding]": "gzip, deflate, br",
            "header[Accept-Language]": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "header[Cookie]": "MOD_AUTH_CAS=MOD_AUTH_" +ST
    }
    res = requests.post(url=url, data=data)

    print(res.text)
    s = res.text
    a = r'route=(.*?)"'
    slotList = re.findall(a, s)
    print(slotList[0])
    route = slotList[0]
    b = r'/,_WEU=(.*?);'
    slotList = re.findall(b, s)
    print(slotList[0])
    WEU = slotList[0]
    #############################################################

    #############################################################六、获取_WEU-2
    print("六、_WEU-2")
    url = "https://getman.cn/api/request"
    data = {
            "url": "https://ehall.szpt.edu.cn/publicappinternet/sys/itpub/MobileCommon/getMenuInfo.do",
            "method": "POST",
            "body": 'data={"APPID":' + APPID + ',"APPNAME":"szptpubxsjkxxbs"}',
            "header[Host]": "ehall.szpt.edu.cn",
            "header[Connection]": "keep-alive",
            'header[Content-Length]': '87',
            "header[Accept]": "application/json, text/plain, */*",
            "header[User-Agent]": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61",
            "header[Content-Type]": "application/x-www-form-urlencoded",
            "header[Origin]": "https://ehall.szpt.edu.cn",
            "header[Sec-Fetch-Site]": "same-origin",
            "header[Sec-Fetch-Mode]": "cors",
            "header[Sec-Fetch-Dest]": "empty",
            "header[Referer]": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/*default/index.do",
            "header[Accept-Encoding]": "gzip, deflate, br",
            "header[Accept-Language]": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "header[Cookie]": "route=" + route + "; _WEU=" + WEU + "; MOD_AUTH_CAS=MOD_AUTH_" + ST,
     }
    res = requests.post(url=url, data=data)

    print(res.text)
    s = res.text
    a = r'_WEU=(.*?);'
    slotList = re.findall(a, s)
    print(slotList[0])
    WEU = slotList[0]
    #############################################################
    #############################################################七、获取route
    print("七、获取route")
    url = "https://getman.cn/api/request"
    data = {
            "url": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/mrxxbs/getReportConfig.do",
            "method": "POST",
            "body": '',
            "header[Host]": "ehall.szpt.edu.cn",
            "header[Connection]": "keep-alive",
            'header[Content-Length]': '0',
            "header[Accept]": "application/json, text/javascript, */*; q=0.01",
            "header[User-Agent]": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64",
            "header[X-Requested-With]": "XMLHttpRequest",
            "header[Origin]": "https://ehall.szpt.edu.cn",
            "header[Sec-Fetch-Site]": "same-origin",
            "header[Sec-Fetch-Mode]": "cors",
            "header[Sec-Fetch-Dest]": "empty",
            "header[Referer]": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/*default/index.do",
            "header[Accept-Encoding]": "gzip, deflate, br",
            "header[Accept-Language]": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "header[Cookie]": "_WEU=" + WEU + "; MOD_AUTH_CAS=MOD_AUTH_" + ST,
    }
    res = requests.post(url=url, data=data)
    print(res.text)
    s = res.text
    a = r'route=(.*?)"'
    slotList = re.findall(a, s)
    print(slotList[0])
    route = slotList[0]

    #############################################################
    #############################################################八、提交表
    print("八、提交表")
    print("ff:",ff[n])
    print("route:",route)
    print("_WEU:",WEU)
    print("ST:",ST)
    url = "https://getman.cn/api/request"
    data = {
            "url": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/mrxxbs/saveReportInfo.do",
            "method": "POST",
            "body": "formData=" + ff[n],
            "header[Host]": "ehall.szpt.edu.cn",
            "header[Connection]": "keep-alive",
            'header[Content-Length]': '3523',
            "header[Accept]": "application/json, text/plain, */*",
            "header[User-Agent]": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61",
            "header[Content-Type]": "application/x-www-form-urlencoded",
            "header[Origin]": "https://ehall.szpt.edu.cn",
            "header[Sec-Fetch-Site]": "same-origin",
            "header[Sec-Fetch-Mode]": "cors",
            "header[Sec-Fetch-Dest]": "empty",
            "header[Referer]": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/*default/index.do",
            "header[Accept-Encoding]": "gzip, deflate, br",
            "header[Accept-Language]": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "header[Cookie]": "route=" + route + "; _WEU=" + WEU + ";MOD_AUTH_CAS=MOD_AUTH_" + ST,
    }
    res = requests.post(url=url, data=data)

    print(res.text)
    s = res.text
    a = r'body":"{(.*?)}'
    slotList = re.findall(a, s)
    print(slotList[0])
    ###################################################
    #成功获取返回{"datas":1,"code":"0"}
    n+=1
    #发邮件
    if(slotList[0]=='200'):
      smtp = "smtp.qq.com"
      sender = '888888888@qq.com'#发送的邮箱
      receiver = '99999999@qq.com'#接受的邮箱
      pwd = '0000000000'      # 授权密码
      title = "每日信息报送失败"
      contents = slotList[0]
      try:
        ldqplxo = MIMEText(contents, 'plain', 'utf-8')
        ldqplxo['From'] = Header(sender, 'utf-8')
        ldqplxo['To'] = Header(receiver, 'utf-8')
        ldqplxo['Subject'] = Header(title, 'utf-8')
        mbdrewr = smtplib.SMTP_SSL(smtp, 465)
        mbdrewr.login(sender, pwd)
        mbdrewr.sendmail(sender, receiver, ldqplxo.as_string())
        mbdrewr.quit()
      except Exception as e:
        print('错误>>>', e)
    else:
     smtp = "smtp.qq.com"

     sender = '188888888@qq.com'#发送邮箱
     receiver = '99999999@qq.com'#接受邮箱
     pwd = 'nrdpluccibqbhibe'     # 授权密码
     # pwd = 'yesejybhflnaigfh'
     title = "每日信息报送成功"
     contents = slotList[0]

     try:
         ldqplxo = MIMEText(contents, 'plain', 'utf-8')
         ldqplxo['From'] = Header(sender, 'utf-8')
         ldqplxo['To'] = Header(receiver, 'utf-8')
         ldqplxo['Subject'] = Header(title, 'utf-8')
         mbdrewr = smtplib.SMTP_SSL(smtp, 465)
         mbdrewr.login(sender, pwd)
         mbdrewr.sendmail(sender, receiver, ldqplxo.as_string())
         mbdrewr.quit()
     except Exception as e:
        print('错误>>>', e)


