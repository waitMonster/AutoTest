# _*_coding:utf-8_*_
'''
Created on 2017年05月31日

@author: wangzhen
'''
import urllib,urllib2,hashlib,json,unittest
import request
import sys
from xlrd import *
reload(sys)
sys.setdefaultencoding("utf-8")
from _tkinter import create

class TestInfo():
    def __init__(self):
        self.request = request.Httpcommon()
        self.sheetbooknamePath = "演示账套"
        self.appName = "accounting"

    def TestEnvi(self):
        #domain = "https://www.fxiaoke.com"
        domain = "https://www.ceshi112.com"
        return  domain

    def login(self):
        url = "https://www.fxiaoke.com/FHH/EM0HXUL/Authorize/PersonalLogin"
        data = '{"PhoneNumber":"13520133129","InternationalAreaCode":"+86","Password":"a123456","PersistenceHint":true,"CliendId":"undefined","ImgCode":""}'
        print self.request.request("POST",url,data=data)

    def getaccountbookId(self):
        self.request = request.Httpcommon()
        domain = self.domainUrl()
        accountbookDict = {}
        url = domain + "chanjet/"+self.appName+"/restlet/v2/web/accountbook/FindAll"

        reslut = json.loads(self.request.request("GET", url, data=None))


        if "resultObj" in str(reslut):
            for i in range(len(reslut["resultObj"])):
                bookName = str(reslut["resultObj"][i]["bookName"])
                bookId = str(reslut["resultObj"][i]["id"])
                accountbookDict[bookName] = {}
                accountbookDict[bookName]["bookId"] = bookId

        else:
            print "获取账套信息失败", reslut
        return accountbookDict[self.sheetbooknamePath]["bookId"]



#获取所有科目字典,格式 {"subjectNo":{"subjectID","100010002","subjectDir":"1","subjectName":"库存现金"}
    def getBalanceInitList(self):
        self.request = request.Httpcommon()
        domain = self.domainUrl()
        subjectDict = {}
        accountbookId = self.getaccountbookId()
        url = domain+"chanjet/"+self.appName+"/restlet/v2/web/balance/GetBalanceInitList?ACCOUNTBOOK="+str(accountbookId)
        result = json.loads(self.request.request("GET", url, data=None))
        if 'resultObj' in str(result):
            for i in range(len(result["resultObj"])):
                subjectName=str(result["resultObj"][i]["subjectText"])
                subjectId=result["resultObj"][i]["id"]
                subjectDir = result["resultObj"][i]["dir"]
                subjectLeaf = result["resultObj"][i]["subjectLeaf"]
                subjectNo = result["resultObj"][i]["subjectNo"]
                subjectDict[subjectNo] = {}
                subjectDict[subjectNo]["subjectId"] = subjectId
                subjectDict[subjectNo]["subjectDir"] = subjectDir
                subjectDict[subjectNo]["subjectName"] = subjectName
            return subjectDict

        else:
            print "getBalanceInitListERROR",result
            return 1







if __name__ == "__main__":
    p = TestInfo()
    print p.login()