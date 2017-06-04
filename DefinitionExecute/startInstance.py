#!/usr/bin/python
#conding:utf8

from SetUp import request,TestInfo
import json

class StartInstance():
    def __init__(self):
        self.request = request.Httpcommon()
        self.domain = TestInfo.TestInfo.TestEnvi()
#查询自动化使用的客户是否存在，如果没有，新建一个客户，发起用于发起流程
    def addCustomer(self,customerName=None):
        #获取我负责的FilterMainId
        url_GetUserTable = self.domain+"/FHH/EM1HEBL/UserTable/GetUserTable"
        data_GetUserTable='{"TableName":"customer","IsLoadManagement":true}'
        result_GetUserTable = self.request.request("POST",url_GetUserTable,data=data_GetUserTable)
        fiterMainId =  json.loads(result_GetUserTable)["Value"]["FilterMains"][1]["FilterMainID"]
        #获取我负责的客户下所有客户信息
        url_GetCustomerList = self.domain+'/FHH/EM1HCRM/Customer/GetCustomerList'
        data_GetCustomerList = '{"QueryInfo":{"FilterMainID":"%s"},"pageSize":20,"pageNumber":1}' % fiterMainId
        result_GetCustomerList = json.loads(self.request.request("POST",url_GetCustomerList,data=data_GetCustomerList))
        flag = 0
        for i in range(result_GetCustomerList["Value"]["CustomerList"]):
            if customerName == result_GetCustomerList["Value"]["CustomerList"][i]["CustomerID"]:
                flag = 1
                return result_GetCustomerList["Value"]["CustomerList"][i]["CustomerID"]

        if flag ==0:
            url_addCustomer = self.domain+"/FHH/EM1HCRM/Customer/AddCustomer"
            data_addCustomer = str(open('addCustomer.json').read())
            result_addCustomer = self.request.request("POST",url_addCustomer,data= data_addCustomer)
            return json.loads(result_addCustomer)["Value"]["CustomerID"]


#获取业务流程，如果没有，新建一个业务流程


#发起流程实例
    def startInstance(self):
        customerName="xxx"
        customerID = self.addCustomer(customerName=customerName)
