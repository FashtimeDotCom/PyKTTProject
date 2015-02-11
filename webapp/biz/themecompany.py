#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

class ThemeCompanyResourceAction():

    #获取当天的财经评论接口--查询当天股票评论#
    @Router.route(url = r"themecompany/dailythemesnews", method = Router._GET|Router._POST)
    def daily_news_themes_action(self,req):
        print ''



    def daily_news_themes_count(self):
        print ''