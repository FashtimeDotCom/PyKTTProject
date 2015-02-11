#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

class ThemeCompanyResourceAction():

    #获取当天的财经评论接口--查询当天股票评论#
    @Router.route(url = r"themecompany/dailythemesnews", method = Router._GET|Router._POST)
    def daily_news_themes_action(self,req):
        start=req.json_args.get("start")
        limit=req.json_args.get("limit")
        count = self.daily_news_themes_count()
        data = self.daily_news_themes_data(start,limit)
        currentdata = {'data':data,'count':count['COUNTS']}
        return req.ok(currentdata)

    def daily_news_themes_data(self,start,limit):
        session = Session('master')
        SQL = " SELECT THEMENEWS.KEYID,THEMENEWS.LINKURL," \
              " SUBSTRING(THEMENEWS.PUBDATE,1,16) AS PUBDATE," \
              " THEMENEWS.TITLE FROM" \
              " STOCK_POOL_THEME_NEWS_TABLE THEMENEWS" \
              " WHERE 1 = 1" \
              " LIMIT %s,%s"%(start,limit)
        logger.info('查询当天股票板块信息接口...！SQL:'+SQL)
        result = session.select_result(SQL)
        return result


    def daily_news_themes_count(self):
        session = Session('master')
        SQL =" SELECT COUNT(*) AS COUNTS FROM STOCK_POOL_THEME_NEWS_TABLE THEMENEWS" \
             " WHERE 1 = 1"
        result = session.select_resultone(SQL)
        return result