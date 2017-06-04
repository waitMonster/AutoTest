#!/usr/bin/python
#coding:utf8
import request

class UserLogin():
    def __init__(self):
        self.request = request.Httpcommon()

    def getEnterpriseList(self):
        url = 'https://www.fxiaoke.com/FHH/EM0HXUL/Authorize/PersonalLogin'
        data = '{"PhoneNumber":"13520133129","InternationalAreaCode":"+86","Password":"glow3182","PersistenceHint":true,"ClientId":"undefined","ImgCode":""}'
        print self.request.request("POST",url,data)



if __name__ =="__main__":
    p = UserLogin()
    print p.getEnterpriseList()
