#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

class  MorningNewsResourceAction(object):
    #获取当日头条新闻信息接口#
    @Router.route(url = r"headline/morningnews", method = Router._GET|Router._POST)
    def headline_morningnews_action(self,req):
        print  req


    #查询当日头条新闻信息#
    def headline_morningnews_resource(self):
        session = Session('master')
        logger.info('查询当日头条新闻信息...！')
