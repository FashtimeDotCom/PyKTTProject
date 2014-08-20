#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log
from entity import resModel

logger = Log().getLog()

class  DataCenterResourceAction(object):

    """获取数据数据中心的交易情绪指标接口"""
    @Router.route(url = r"datacenter/tradeactivity", method = Router._GET|Router._POST)
    def tradeactivity_action(self,req):
        resource_entity = self.tradeactivity_resource()
        current_date = []
        current_value = []
        for current_dict in  resource_entity:
            current_dict['STARTDATE'] = current_dict['STARTDATE'].strftime('%Y-%m-%d')
            current_dict['ENDDATE'] = current_dict['ENDDATE'].strftime('%Y-%m-%d')
            current_date.append(current_dict['STARTDATE']+'至'+current_dict['ENDDATE'])
            current_value.append(current_dict['CURRENTVALUE'])
        resource_entity = {'currentdate':current_date,'currentvalue':current_value}
        return req.ok(resource_entity)

    #数据中心交易情绪查询操作方法#
    def tradeactivity_resource(self):
        session = Session('master')
        logger.info('数据中心交易情绪查询查询...！')
        resources = session.select(resModel.TradeActivity,{})
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












