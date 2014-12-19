#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

class  MorningNewsResourceAction(object):

    #获取国内当天的财经新闻接口#
    @Router.route(url = r"morningnews/chinanews", method = Router._GET|Router._POST)
    def china_morningnews_action(self,req):
        start=req.json_args.get("start")
        limit=req.json_args.get("limit")
        type = 'CHINA'
        count = self.common_morningnews_count(type)
        data = self.common_morningnews_data(type,start,limit)
        currentdata = {'data':data,'count':count['COUNTS']}
        return req.ok(currentdata)

    #获取国外当天的财经新闻接口#
    @Router.route(url = r"morningnews/europenews", method = Router._GET|Router._POST)
    def europe_morningnews_action(self,req):
        start=req.json_args.get("start")
        limit=req.json_args.get("limit")
        type = 'EUROPE'
        count = self.common_morningnews_count(type)
        data = self.common_morningnews_data(type,start,limit)
        currentdata = {'data':data,'count':count['COUNTS']}
        return req.ok(currentdata)

    #获取股票当天的财经新闻接口#
    @Router.route(url = r"morningnews/stocknews", method = Router._GET|Router._POST)
    def stock_morningnews_action(self,req):
        start=req.json_args.get("start")
        limit=req.json_args.get("limit")
        type = 'STOCK'
        count = self.common_morningnews_count(type)
        data = self.common_morningnews_data(type,start,limit)
        currentdata = {'data':data,'count':count['COUNTS']}
        return req.ok(currentdata)

    #查询财经新闻详情通用查询接口#
    def common_morningnews_data(self,type,start,limit):
        session = Session('master')
        logger.info('查询国内当天的财经新闻信息...！')
        SQL = " SELECT NEWS.TITLE AS TITLE, NEWS.IMAGEURL AS IMAGEURL, " \
              " SUBSTRING(NEWS.PUBDATE,1,16) AS PUBDATE, " \
              " NEWS.LINKURL AS LINKURL , " \
              " NEWS.DESCRIPTCONTEXT AS DESCRIPTCONTEXT " \
              " FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  NEWS  " \
              " WHERE  1=1  AND  NEWS.NEWSFLAG = '%s' " \
              " ORDER BY  NEWS.PUBDATE DESC  " \
              " LIMIT %s,%s"%(type,start,limit)
        result = session.select_result(SQL)
        return result


    #查询财经新闻总条数查询接口#
    def common_morningnews_count(self,type):
        session = Session('master')
        SQL = " SELECT COUNT(*) AS COUNTS FROM  MORNING_FINANCENEWS_RESOURCE_TABLE  NEWS  " \
              " WHERE  1=1  " \
              " AND  NEWS.NEWSFLAG = '%s' "%type
        result = session.select_resultone(SQL)
        return result
