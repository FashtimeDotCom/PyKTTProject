#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

#财经评论服务层#
class  CommentsResourceAction(object):

    #获取当天的财经评论接口--查询当天股票评论#
    @Router.route(url = r"morningnews/dailystockcomments", method = Router._GET|Router._POST)
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
        SQL = "SELECT  COMMENTSSTOCK.KEYID AS KEYID ," \
              " COMMENTSSTOCK.TITLE AS TITLE , " \
              " COMMENTSSTOCK.DESCRIPTCONTEXT AS DESCRIPTCONTEXT , " \
              " COMMENTSSTOCK.LINKURL AS LINKURL, " \
              " SUBSTRING(COMMENTSSTOCK.PUBDATE,1,16) AS PUBDATE " \
              " FROM  COMMENTS_STOCK_RESOURCE_TABLE  COMMENTSSTOCK " \
              " WHERE 1=1 " \
              " AND   COMMENTSSTOCK.DESCRIPTCONTEXT !='' " \
              " ORDER BY  COMMENTSSTOCK.PUBDATE DESC " \
              " LIMIT %s,%s"%(start,limit)
        logger.info('查询财经新闻详情通用查询接口...！SQL:'+SQL)
        result = session.select_result(SQL)
        return result


    #查询当天股票评论总条数查询接口#
    def daily_stock_comments_count(self):
        session = Session('master')
        SQL =" SELECT COUNT(*) FROM  COMMENTS_STOCK_RESOURCE_TABLE  COMMENTSSTOCK " \
             " WHERE 1=1 AND   COMMENTSSTOCK.DESCRIPTCONTEXT !='' "
        result = session.select_resultone(SQL)
        return result

