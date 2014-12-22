#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

#财经评论服务层#
class  CommentsResourceAction(object):

    #获取当天的财经评论接口--查询当天股票评论#
    @Router.route(url = r"comments/dailystock", method = Router._GET|Router._POST)
    def daily_stock_comments_action(self,req):
        start=req.json_args.get("start")
        limit=req.json_args.get("limit")
        count = self.daily_stock_comments_count()
        data = self.daily_stock_comments_data(start,limit)
        currentdata = {'data':data,'count':count['COUNTS']}
        return req.ok(currentdata)


    #查询当天股票评论详情通用查询接口#
    def daily_stock_comments_data(self,start,limit):
        session = Session('master')
        SQL = "SELECT  COMMENTSSTOCK.KEYID AS keyId ," \
              " COMMENTSSTOCK.TITLE AS title , " \
              " COMMENTSSTOCK.DESCRIPTCONTEXT AS descriptContext , " \
              " COMMENTSSTOCK.LINKURL AS linkUrl, " \
              " SUBSTRING(COMMENTSSTOCK.PUBDATE,1,16) AS pubDate " \
              " FROM  COMMENTS_STOCK_RESOURCE_TABLE  COMMENTSSTOCK " \
              " WHERE 1=1 " \
              " AND   COMMENTSSTOCK.DESCRIPTCONTEXT !='' " \
              " ORDER BY  COMMENTSSTOCK.PUBDATE DESC " \
              " LIMIT %s,%s"%(start,limit)
        logger.info('查询当天股票评论详情通用查询接口...！SQL:'+SQL)
        result = session.select_result(SQL)
        return result


    #查询当天股票评论总条数查询接口#
    def daily_stock_comments_count(self):
        session = Session('master')
        SQL =" SELECT COUNT(*) FROM  COMMENTS_STOCK_RESOURCE_TABLE  COMMENTSSTOCK " \
             " WHERE 1=1 AND   COMMENTSSTOCK.DESCRIPTCONTEXT !='' "
        result = session.select_resultone(SQL)
        return result


    #获取当天的财经评论接口--查询当天外汇评论#
    @Router.route(url = r"comments/dailyfinance", method = Router._GET|Router._POST)
    def daily_finance_comments_action(self,req):
        start=req.json_args.get("start")
        limit=req.json_args.get("limit")
        count = self.daily_finance_comments_count()
        data = self.daily_finance_comments_data(start,limit)
        currentdata = {'data':data,'count':count['COUNTS']}
        return req.ok(currentdata)

    #查询当天外汇评论详情通用查询接口#
    def daily_finance_comments_data(self,start,limit):
        session = Session('master')
        SQL = " SELECT  COMMENTSFINANCE.KEYID AS keyId , " \
              " COMMENTSFINANCE.TITLE AS title , " \
              " COMMENTSFINANCE.DESCRIPTCONTEXT AS descriptContext ," \
              " COMMENTSFINANCE.LINKURL AS linkUrl, " \
              " SUBSTRING(COMMENTSFINANCE.PUBDATE,1,16) AS pubDate " \
              " FROM  COMMENTS_FINANCE_RESOURCE_TABLE  COMMENTSFINANCE" \
              " WHERE 1=1 " \
              " AND COMMENTSFINANCE.DESCRIPTCONTEXT !='' " \
              " AND   COMMENTSFINANCE.COMMENTFLAG = 'FINANCE' " \
              " ORDER BY  COMMENTSFINANCE.PUBDATE DESC " \
              " LIMIT %s,%s"%(start,limit)
        logger.info('查询当天外汇评论详情通用查询接口...！SQL:'+SQL)
        result = session.select_result(SQL)
        return result

    #查询当天外汇评论总条数查询接口#
    def daily_finance_comments_count(self):
        session = Session('master')
        SQL =" SELECT  COUNT(*) " \
             " FROM  COMMENTS_FINANCE_RESOURCE_TABLE  COMMENTSFINANCE " \
             " WHERE 1=1" \
             " AND   COMMENTSFINANCE.DESCRIPTCONTEXT !=''" \
             " AND   COMMENTSFINANCE.COMMENTFLAG = 'FINANCE'"
        result = session.select_resultone(SQL)
        return result