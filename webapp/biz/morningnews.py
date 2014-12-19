#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

class  MorningNewsResourceAction(object):
    #获取国内当天的财经新闻接口#
    @Router.route(url = r"headline/morningnews", method = Router._GET|Router._POST)
    def china_morningnews_action(self,req):
        print


    #查询国内当天的财经新闻信息#
    def china_morningnews_resource(self):
        session = Session('master')
        logger.info('查询国内当天的财经新闻信息...！')
