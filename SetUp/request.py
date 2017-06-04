# -*- coding:utf-8 -*-


import urllib2
import hashlib
import time
import urllib
import json
import cookielib


class Httpcommon():


    def __init__(self):
        self.username = "12311011106"
        self.password = hashlib.md5("111111").hexdigest()
        self.token = self.logincia()
        self.cookie = "PHPSESSID=eejh6bi3g77tv2v02ts4p522l5; guid=99179b3d-be89-9024-0478-215c5c504e6e; mirrorId=0000; FSAuthXG=o060JEXqN040000pjG7KqZz9UR2EuIqnFIjtzG13zIVQWLoXn4At3aiziQfAXoVOJzwt6hWnMsS24ff5; fs_token=Cs5aDpWmOsCjPZPYOIqqPMHcBM4sD6GjCZLYC39ZDZ8tOp4v; FSAuthX=0G60s8eAQm400018ECkYFctzaZq1C4dMk31AjMaW9QEpo5ZYdSdMOvREDOZSDYNc7PRct5QIQ7oYedoEXSDMWufzkkQxh6Px5ycr4dIXP1UfQk9e9UN7U8mYov1tmN8xPryr9ME1AYZD3pkLXqy4DkgECtfnGhrupBguJEhOFpTb3CB9U6Fj8WFyNpKJnTLPgg5W36ajg0fRgvnIUfFXEqrD9mVk42azGU6ulHzsXwzWg3dSEMRqQFxrOKzV1o4nDHavC30wOYvTrC4I3; FSAuthXC=0G60s8eAQm400018ECkYFctzaZq1C4dMk31AjMaW9QEpo5ZYdSdMOvREDOZSDYNc7PRct5QIQ7oYedoEXSDMWufzkkQxh6Px5ycr4dIXP1UfQk9e9UN7U8mYov1tmN8xPryr9ME1AYZD3pkLXqy4DkgECtfnGhrupBguJEhOFpTb3CB9U6Fj8WFyNpKJnTLPgg5W36ajg0fRgvnIUfFXEqrD9mVk42azGU6ulHzsXwzWg3dSEMRqQFxrOKzV1o4nDHavC30wOYvTrC4I3; sso_token=19246563-ead4-452e-8b3f-5be4d3e006a4; RouteUp=; Hm_lvt_06d5233541e92feb3cc8980700b1efa6=1496197382; Hm_lpvt_06d5233541e92feb3cc8980700b1efa6=1496284135; _ga=GA1.2.839825985.1496197381; _gid=GA1.2.861933822.1496284137; Hm_lvt_3e726ab9f3eb0d06b86d6f5d0a31fad4=1496197383; Hm_lpvt_3e726ab9f3eb0d06b86d6f5d0a31fad4=1496284137; enterprise=54931; JSESSIONID=4B7E8BC9EFFA7E8E8D753CB1592575A7; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215c5c503f044c2-02e9f90c64b722-30637509-2073600-15c5c503f059fd%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D"

    def request(self, method, url, data):
        try:
            rq = urllib2.Request(url)
            #rq.add_header("Token", self.token)
            #rq.add_header("Device-Searal", "59")
            #rq.add_header("Device-Name", ':7-433d06bb')
            rq.add_header("accept", 'application/json')
            rq.add_header("Cookie",self.cookie)
            #rq.add_header("Cookie","guid=d6a35b26-363a-7827-e51f-915c5c1ad9a9; mirrorId=0000; Hm_lvt_06d5233541e92feb3cc8980700b1efa6=1496193883; Hm_lpvt_06d5233541e92feb3cc8980700b1efa6=1496221319; FSAuthXG=o060JEXqN040000pjG7KqZz9UR2EuIqnFIjtzG13zIVQWLoXn4At3aiziQfAXoVOJzwt6hWnMsS24ff5; fs_token=CZ5cOM8tDc8jE6HcE2qqOM4vBJWpCp8jE3GsEJ1ZOZGtCJ0q; FSAuthX=0G60s8eAQm40000XPSB37yzgSsZz89yQHHF52gTeg71hpzt0CydMXdScvJ0JRFy6kYBYXJ0PLD7yXcecpKtQmCDLFjcbgHHsTSMzTNt7L9wyQOs23ak1ypnB2L5aB0Y9poqXMuyF8WjhmVQhzpdoXZXwXAAJ8vanyLhy7BQVG6TsTXeQmORs2zf0Hz6ixKJLSORLk1BqVuZiHS7aiuwHAC1a8peKhh8KBjevNkiCdGXxptE1RKzwHrJNhhu8X5uke1h6QRc4klpsRwBhfE; FSAuthXC=0G60s8eAQm40000XPSB37yzgSsZz89yQHHF52gTeg71hpzt0CydMXdScvJ0JRFy6kYBYXJ0PLD7yXcecpKtQmCDLFjcbgHHsTSMzTNt7L9wyQOs23ak1ypnB2L5aB0Y9poqXMuyF8WjhmVQhzpdoXZXwXAAJ8vanyLhy7BQVG6TsTXeQmORs2zf0Hz6ixKJLSORLk1BqVuZiHS7aiuwHAC1a8peKhh8KBjevNkiCdGXxptE1RKzwHrJNhhu8X5uke1h6QRc4klpsRwBhfE; sso_token=a903288c-3669-49ed-9b82-af0775f35489; RouteUp=Search; Hm_lvt_3e726ab9f3eb0d06b86d6f5d0a31fad4=1496193881; Hm_lpvt_3e726ab9f3eb0d06b86d6f5d0a31fad4=1496280628; _ga=GA1.2.2029508432.1496193881; _gid=GA1.2.403185852.1496280630; enterprise=fktest; JSESSIONID=B65AD37E6E8F80E070084E2E52F726DF; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215c5c1ad2b354e-0c0149f03eff05-30637509-2073600-15c5c1ad2b42c8%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D")
            rq.add_header("Content-Type", "application/json;charset=utf-8")
            rq.get_method = lambda: method
            content = urllib2.urlopen(rq, data).read()
            return content
        except Exception, e:
            return e.read()

    def request1(self, method, url, data):
        try:
            rq = urllib2.Request(url)
            #            rq.add_header("Token",self.token)
            rq.add_header("Cookie", self.Cookie)
            rq.add_header("Content-Type", "application/json;charset=utf-8")
            # rq.add_header("Accept-Encoding", "gzip,deflate,sdch")
            rq.get_method = lambda: method
            content = urllib2.urlopen(rq, data).read()
            return content
        except Exception, e:
            return e.read()

    def request_delete(self, url, data):
        rq = urllib2.Request(url, data=data)
        #        rq.add_header("Token",self.token)
        rq.add_header("Cookie", self.Cookie)
        rq.add_header("Accept", "application/javascript, application/json")
        rq.add_header("Accept-Encoding", "gzip,deflate,sdch")
        rq.add_header("Accept-Language", "zh-CN,zh;q=0.8")
        rq.add_header("Connection", "keep-alive")
        rq.add_header("Content-Length", "2")
        rq.add_header("Content-Type", "application/json;charset=utf-8")
        rq.get_method = lambda: 'DELETE'  # or 'DELETE or PUT or ...
        responseinfo = urllib2.urlopen(rq).read()
        return responseinfo

    def request_put(self, url, data):
        rq = urllib2.Request(url, data=data)
        rq.add_header("Cookie", self.Cookie)
        rq.add_header("Accept", "application/javascript, application/json")
        rq.add_header('Accept-Encoding', 'gzip,deflate,sdch')
        rq.add_header("Content-Type", "application/json;charset=utf-8")
        rq.get_method = lambda: 'put'  # or 'DELETE or PUT or ...
        responseinfo = urllib2.urlopen(rq.data).read()
        #        responseinfo = urllib2.urlopen(rq).read()
        return responseinfo

    def post(self, url, data):  # http post+referer请求方式
        import urllib
        rq = urllib2.Request(url)
        # rq.add_header("Token","2a8a2e33-b775-456e-a050-0ef8d6c420a9")
        # rq.add_header("Device-Searal","7")
        # rq.add_header("Device-Name","7-433d06bb");
        # rq.add_header("Device-Type","Android")
        # rq.add_header('cookie',self.Cookie)
        # rq.add_header("Content-Type","application/json")
        content = urllib2.urlopen(rq, data=urllib.urlencode(data)).read()
        return content

    def get(self, url):
        start_time = time.time()
        rq = urllib2.Request(url)
        rq.add_header("Token", "da350393-157b-4abd-ab8f-04fe538d24be")
        rq.add_header("Device-Searal", "7")
        rq.add_header("Device-Name", "7-433d06bb");
        rq.add_header("Device-Type", "Android")
        rq.add_header("Content-Type", "application/json")
        content = urllib2.urlopen(rq)
        cont = content.read()
        return cont
        timer = time.time() - start_time
        return timer

    def get_data(self, url, param):
        rq = urllib2.Request(url)
        rq.add_header('cookie', self.Cookie)
        content = urllib2.urlopen(rq, data=param)
        cont = content.read()
        return cont

    def put(self, url, param):
        rq = urllib2.Request(url, data=param)
        rq.add_header("Cookie", self.Cookie)
        rq.add_header("Device-Searal", "7")
        rq.add_header("Device-Name", "7-433d06bb");
        rq.add_header("Device-Type", "Android")
        rq.add_header("Content-Type", "application/json")
        rq.get_method = lambda: 'PUT'
        content = urllib2.urlopen(rq)
        http_recode = content.code
        cont = content.read()
        return cont, http_recode

    def multipart(self, url, files):
        try:
            register_openers()
            datagen, headers = multipart_encode({"Filedata": open(files, "rb")})

            rq = urllib2.Request(url, datagen, headers)
            rq.add_header("Token", self.token)
            rq.add_header("Device-Searal", "121212")
            rq.add_header("Device-Name", "11212")
            rq.add_header("Device-Type", "Android")
            rq.add_header("Content-Type", "multipart/form-data")
            rq.add_header("Content-Transfer-Encoding", "binary")
            rq.add_header("Content-Type", "application/octet-stream")
            requestInfo = urllib2.urlopen(rq)
            print  requestInfo.read()
        except Exception, e:
            print e.read()

    def chanjet_request_urlencode(self, method, url, data):

        try:
            rq = urllib2.Request(url)
            # rq.add_header("Token",self.token)
            # rq.add_header("Device-Searal", "121212")
            # rq.add_header("Device-Name", "11212")
            # rq.add_header("Device-Type", "Android")
            rq.add_header("Content-Type", "application/x-www-form-urlencoded")
            rq.get_method = lambda: method
            content = urllib2.urlopen(rq, data=urllib.urlencode(data)).read()
            return content
        except Exception, e:
            return e.read()

    def chanjet_request(self, method, url, data):
        try:
            rq = urllib2.Request(url)
            # rq.add_header("Token",self.token)
            # rq.add_header("Device-Searal", "121212")
            # rq.add_header("Device-Name", "11212")
            # rq.add_header("Device-Type", "Android")
            rq.add_header("Content-Type", "application/x-www-form-urlencoded")
            rq.get_method = lambda: method
            content = urllib2.urlopen(rq, data).read()
            return content
        except Exception, e:
            return e.read()



    def logincia(self, var="access_token"):
        url = "http://cia.csp.chanapp.com/internal_api/client_authentication_with_userInfo"
        param = 'client_id=accounting&client_secret=uoi6dd&auth_username=%s&password=%s' % (
        self.username, self.password)
        rq = urllib2.Request(url)
        # content = urllib2.urlopen(rq, data=param).read().split(',')[0].split(':')[1].replace('"','')
        content = urllib2.urlopen(rq, data=param).read()
        if "access_token" not in json.loads(content).keys():
            print "用户名密码错误"
        else:
            return json.loads(content)[var]


if __name__ == "__main__":
    test = Httpcommon()
    #print test.logincia()