#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

class  DailyBlogResourceAction(object):

    #通过blog日子类型查询相应的日志列表#
    @Router.route(url = r"dailyblog/byresourcetype", method = Router._GET|Router._POST)
    def byresourcetype_action(self,req):
        print ''


    def byresourcetype_resource(self):
        session = Session('master')
        logger.info('数据中心交易情绪查询查询...！')
        SQL = ""
        resources = session.select_result(SQL)
        return resources