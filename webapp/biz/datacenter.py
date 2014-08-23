#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

class  DataCenterResourceAction(object):

    #获取数据数据中心的交易情绪指标接口#
    @Router.route(url = r"datacenter/tradeactivity", method = Router._GET|Router._POST)
    def tradeactivity_action(self,req):
        resource_entity = self.tradeactivity_resource()
        currentdate = []
        currentvalue = []
        for current_dict in  resource_entity:
            for (key,value) in current_dict.iteritems():
                if('STARTDATE'==key):
                    currentdate.append(value)
                elif('CURRENTVALUE'==key):
                    currentvalue.append(value)
        resource_entity = {'currentdate':currentdate,'currentvalue':currentvalue}
        return req.ok(resource_entity)

    #数据中心交易情绪查询操作方法#
    def tradeactivity_resource(self):
        session = Session('master')
        logger.info('数据中心交易情绪查询查询...！')
        sql = " SELECT " \
              " CONCAT(SUBSTRING(DATACENTER.STARTDATE,1,10),'-',SUBSTRING(DATACENTER.ENDDATE,1,10)) AS STARTDATE," \
              " DATACENTER.CURRENTVALUE AS CURRENTVALUE " \
              " FROM " \
              " DATACENTER_TRADEACTIVITY DATACENTER " \
              " WHERE 1 = 1 ORDER BY DATACENTER.STARTDATE DESC LIMIT 0,20"
        print(sql)
        resources = session.select_result(sql)
        return resources


    #获取数据中心市场交易活跃度指标接口#
    @Router.route(url = r"datacenter/marketsentiment", method = Router._GET|Router._POST)
    def marketsentiment_action(self,req):
         current_resource = self.marketsentiment_resource()
         currentdate = []
         currentvalue = []
         for current_dict in current_resource:
             for (key,value) in current_dict.iteritems():
                 if('CURRENTDATE'==key):
                     currentdate.append(value)
                 elif('CURRENTVALUE'==key):
                     currentvalue.append(value)
         currentdata ={'currentdate':currentdate,'currentvalue':currentvalue}
         return req.ok(currentdata)


    #数据中心市场交易活跃度查询方法#
    def marketsentiment_resource(self):
        session = Session('master')
        logger.info('数据中心市场交易活跃度查询...！')
        sql = "SELECT SUBSTRING(DATACENTER.CURRENTDATE,1,10) AS CURRENTDATE," \
              " DATACENTER.CURRENTVALUE AS CURRENTVALUE" \
              " FROM " \
              " DATACENTER_MARKETSENTIMENT DATACENTER" \
              " WHERE 1 = 1 " \
              " ORDER BY DATACENTER.CURRENTDATE DESC LIMIT 0,15"
        result = session.select_result(sql);
        return result



    #获取数据中心板块涨跌幅度指标接口#
    @Router.route(url = r"datacenter/plateconcept", method = Router._GET|Router._POST)
    def plateconcept_action(self,req):
        current_resource = self.plateconcept_resource()
        current_platename=[]
        current_risedecline = []
        for current_dict in current_resource:
             for (key,value) in current_dict.iteritems():
                 if('PLATENAME'==key):
                     current_platename.append(value)
                 elif('RISEDECLINE'==key):
                     current_risedecline.append(value*100)
        currentdata ={'platename':current_platename,'risedecline':current_risedecline}
        return req.ok(currentdata)


    #数据中心热门板块查询#
    def plateconcept_resource(self):
        session = Session('master')
        logger.info('数据中心热门板块查询...！')
        sql = " SELECT DATACENTER.PLATENAME AS PLATENAME," \
              " DATACENTER.RISEDECLINE AS RISEDECLINE," \
              " DATACENTER.CURRENTMONEY AS CURRENTMONEY" \
              " FROM " \
              " DATACENTER_PLATECONCEPT_RESOURCE_TABLE DATACENTER " \
              " WHERE 1 = 1 " \
              " ORDER BY DATACENTER.RISEDECLINE DESC,DATACENTER.CURRENTMONEY DESC LIMIT 0,15"
        result = session.select_result(sql)
        return result


    #数据中心期指期货多空双方持仓统计
    @Router.route(url = r"datacenter/stockfuture", method = Router._GET|Router._POST)
    def stockfuture_action(self,req):
        current_bull_resource = self.stockfuture_resource('BULL')
        current_bear_resource = self.stockfuture_resource('BEAR')
        currentdata ={'bear':current_bear_resource['TOTALVALUE'],'bull':current_bull_resource['TOTALVALUE']}
        return req.ok(currentdata)



    #数据中心期指期货多空双方持仓查询#
    def stockfuture_resource(self,dataflag):
        session = Session('master')
        logger.info('数据中心期指期货多空双方持仓查询...！')
        sql = "SELECT SUM(TOTALVALUE) AS TOTALVALUE " \
              "FROM DATACENTER_STOCKFUTURE_RESOURCE_TABLE DATACENTER " \
              "WHERE 1=1 AND DATACENTER.DATAFLAG ='%s'"%dataflag
        result = session.select_resultone(sql)
        return result
      
      
    #国家黄金外汇储备经济指标#
    @Router.route(url = r"datacenter/forexgold", method = Router._GET|Router._POST) 
    def forexgold_action(self,req):
        current_resource = self.forexgold_resource()
        #当前时间#
        currentdate = []
        #当前时间外汇值#
        forexdata = []
        #当前时间黄金储备量#
        golddata = []
        for current_dict in current_resource:
            for (key,value) in current_dict.iteritems():
                if('CURRENTDATE'==key):
                    currentdate.append(value)
                elif('FOREXSTORA'==key):
                    forexdata.append(value)
                elif('GOLDSTORA'==key):
                    golddata.append(value)
        currentdata ={'currentdate':currentdate,'forexdata':forexdata,'golddata':golddata}
        return req.ok(currentdata)
    
    #国家黄金外汇储备查询#
    def forexgold_resource(self):
        session = Session('master')
        logger.info('国家黄金外汇储备查询...！')
        sql = " SELECT  SUBSTRING(DATACENTER.CURRENTDATE,1,10) AS CURRENTDATE," \
              " DATACENTER.FOREXSTORA AS FOREXSTORA, " \
              " DATACENTER.GOLDSTORA AS GOLDSTORA " \
              " FROM " \
              " DATACENTER_GOLDFOREX_RESOURCE_TABLE DATACENTER " \
              " WHERE  1 = 1 ORDER BY DATACENTER.CURRENTDATE DESC LIMIT 0,25"
        result = session.select_result(sql)
        return result
     
    #波罗地海航运干货指数#
    @Router.route(url = r"datacenter/bulkcargotrans", method = Router._GET|Router._POST)
    def bulkcargotrans_action(self,req):
        current_resource = self.bulkcargotrans_resource()
        currenttime= []
        indexvalue = []
        for current_dict in current_resource:
            for (key,value) in current_dict.iteritems():
                if('CURRENTTIME'==key):
                    currenttime.append(value)
                elif('INDEXVALUE'==key):
                    indexvalue.append(value)
        currentdata ={'currenttime':currenttime,'indexvalue':indexvalue}
        return req.ok(currentdata)
                    
    #波罗地海航运干货指数查询#
    def bulkcargotrans_resource(self):
        session = Session('master')
        logger.info('波罗地海航运干货指数查询...！')
        sql = " SELECT SUBSTRING(DATACENTER.CURRENTTIME,1,10) AS CURRENTTIME," \
              " DATACENTER.INDEXVALUE AS INDEXVALUE " \
              " FROM  DATACENTER_BULKCARGOTRANS_RESOURCE_TABLE DATACENTER  " \
              " WHERE 1=1 " \
              " ORDER BY DATACENTER.CURRENTTIME DESC LIMIT 0,25"
        result = session.select_result(sql)
        return result

    #股票账户信息指标信息查询接口#
    @Router.route(url = r"datacenter/stockaccount", method = Router._GET|Router._POST)
    def stockaccount_action(self,req):
        current_resource = self.stockfuture_resource()
        currentdate=[]
        finaleffaccnum=[]
        addaccnum=[]
        addshaccnum=[]
        addszaccnum=[]
        finalaccnum=[]
        finalszsleepnum=[]
        finalshsleepnum=[]
        finalsleepnum=[]
        for current_dict in current_resource:
            for (key,value) in current_dict:
                if('STARTDATE'==key):
                    currentdate.append(value)
                elif('ADDSUMACCNUM'==key):
                    addaccnum.append(value)
                elif('FINALSUMEFFACCNUM'==key):
                    finaleffaccnum.append(value)
                elif('ADDSHACCNUM'==key):
                    addshaccnum.append(value)
                elif('ADDSZACCNUM'==key):
                    addszaccnum.append(value)
                elif('FINALSUMACCNUM'==key):
                    finalaccnum.append(value)
                elif('FINALSUMSLEEPACCNUM'==key):
                    finalsleepnum.append(value)
                elif('FINALSZSLEEPACCNUM'==key):
                    finalszsleepnum.append(value)
                elif('FINALSHSLEEPACCNUM'==key):
                    finalshsleepnum.append(value)
        currentdata ={'currentdate':currentdate,'finaleffaccnum':finaleffaccnum,
                      'addaccnum':addaccnum,'addshaccnum':addshaccnum
                     'addszaccnum':addszaccnum,'finalaccnum':finalaccnum
                     'finalszsleepnum':finalszsleepnum,'finalshsleepnum':finalshsleepnum
                     'finalsleepnum':finalsleepnum}
        return req.ok(currentdata)

    #股票账户信息指标信息查询#
    def stockaccount_resource(self):
        session = Session('master')
        logger.info('股票账户信息指标信息查询...！')
        sql=" SELECT " \
            " CONCAT(SUBSTRING(DATACENTER.STARTDATE,1,10),'-',SUBSTRING(DATACENTER.ENDDATE,1,10)) AS STARTDATE, " \
            " DATACENTER.FINALSHEFFACCNUM AS FINALSHEFFACCNUM, " \
            " DATACENTER.FINALSZEFFACCNUM AS FINALSZEFFACCNUM, " \
            " DATACENTER.FINALSUMEFFACCNUM AS FINALSUMEFFACCNUM," \
            " DATACENTER.ADDSHACCNUM AS ADDSHACCNUM, " \
            " DATACENTER.ADDSZACCNUM AS ADDSZACCNUM, " \
            " DATACENTER.ADDSUMACCNUM AS ADDSUMACCNUM, " \
            " DATACENTER.FINALSHACCNUM AS FINALSHACCNUM, " \
            " DATACENTER.FINALSZACCNUM AS FINALSZACCNUM, " \
            " DATACENTER.FINALSUMACCNUM AS FINALSUMACCNUM, " \
            " DATACENTER.FINALSZSLEEPACCNUM AS FINALSZSLEEPACCNUM," \
            " DATACENTER.FINALSHSLEEPACCNUM AS FINALSHSLEEPACCNUM, " \
            " DATACENTER.FINALSUMSLEEPACCNUM AS FINALSUMSLEEPACCNUM " \
            "FROM " \
            "DATACENTER_STOCKACCOUNT_RESOURCE_TABLE DATACENTER " \
            "WHERE " \
            "1 = 1 ORDER BY DATACENTER.STARTDATE DESC LIMIT 0,25"
        result = session.select_result(sql)
        return result