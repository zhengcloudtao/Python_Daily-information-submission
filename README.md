# Python_Daily-information-submission
Python_每日信息报送
# 每日信息报送

## 一、获取route、JSESSIONID、lt、pwdDefaultEncryptSalt

###  "url": "https://authserver.szpt.edu.cn/authserver/login?service=https://ehall.szpt.edu.cn:443/login?service=https://ehall.szpt.edu.cn/new/index.html"

###  "method": "GET"

### Response:Cookie里获取route、JSESSIONID,页面元素的lt、pwdDefaultEncryptSalt

## 二、pwdDefaultEncryptSalt作为key加密密码

### encrypt.js

### method:encryptAES(密码,key)

## 三、登录

###  "url":"https://authserver.szpt.edu.cn/authserver/login?service=https://ehall.szpt.edu.cn:443/publicappinternet/sys/szptpubxsjkxxbs/*default/index.do"

###  "method":"POST"

### "body":"username="+学号+"&password="+加密后的密文+"&lt="+前面获取的lt+"&dllt=userNamePasswordLogin&execution=e1s1&_eventId=submit&rmShown=1"

### "header[Cookie]":"route="+route+"; JSESSIONID="+JESSIONID

### code==200,频繁登录需要验证码或信息错误；code==302,正常登录,

### Response:页面，获取ST-前缀密文，:Cookie里获取CASTGC

## 四、校验ST

### "url": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/*default/index.do?ticket="+ST

### "method": "GET"

### Response:Cookie里获取MOD_AUTH_CAS

- 如果为空，二次请求

	- "url": "https://authserver.szpt.edu.cn/authserver/login?service=https%3A%2F%2Fehall.szpt.edu.cn%3A443%2Fpublicappinternet%2Fsys%2Fszptpubxsjkxxbs%2F*default%2Findex.do"
	- "method": "GET"
	-  "header[Cookie]": "CASTGC="+CASTGC+"; route="+route+"; JSESSIONID="+JESSIONID
	- Response:页面，获取ST-前缀密文
	- 获取到ST再次校验ST直到校验成功

- 如果不为空，校验成功，ST可用

## 四、获取_WEU-1

### "url":"https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/*default/index.do"

###  "method":"GET"

### "header[Cookie]":"MOD_AUTH_CAS=MOD_AUTH_ST-前缀密文

### Response:Cookie里获取route、两个_WEU中长的

## 五、获取_WEU-2

### "url":"https://ehall.szpt.edu.cn/publicappinternet/sys/itpub/MobileCommon/getMenuInfo.do"

### "method":"POST"

### "body":"data={"APPID":"5812981499622390","APPNAME":"szptpubxsjkxxbs"}"

### "header[Cookie]":"route="+route+"; _WEU="+WEU+"; MOD_AUTH_CAS=MOD_AUTH_ST-前缀密文

### Response:Cookie里获取_WEU

## 六、获取route

### "url": "https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/mrxxbs/getReportConfig.do"

### "method": "POST"

### "header[Cookie]": "_WEU=" + WEU + "; MOD_AUTH_CAS=MOD_AUTH_" + ST

### Response:Cookie里获取route

## 七、提交表

### "url":"https://ehall.szpt.edu.cn/publicappinternet/sys/szptpubxsjkxxbs/mrxxbs/saveReportInfo.do"

### "method":"POST"

### "body":"formData="自己的信息(每天的REPORT_DATE不一样)”，

### "header[Cookie]":"route="+route+"; _WEU="+长WEU+";MOD_AUTH_CAS=MOD_AUTH_ST-前缀密文

### success_Response:{"datas":1,"code":"0"}

