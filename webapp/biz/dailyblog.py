#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

class  DailyBlogResourceAction(object):

    #通过blog日子类型查询相应的日志列表#
    @Router.route(url = r"dailyblog/byresourcetype", method = Router._GET|Router._POST)
    def byresourcetype_action(self,req):
        start=req.json_args.get("start")
        limit=req.json_args.get("limit")
        bzfl =req.json_args.get("bzfl")
        bzname =req.json_args.get("bzname").strip()
        data = self.byresourcetype_resource(bzfl,start,limit,bzname)
        count = self.byresourcetype_count(bzfl,bzname)
        logger.info(count['COUNTS'])
        currentdata = {'data':data,'count':count['COUNTS']}
        return req.ok(currentdata)

    def byresourcetype_resource(self,bzfl,start,limit,bzname):
        session = Session('master')
        SQL =None
        SQL = " SELECT A.BZ_NAME AS bzname, A.BZ_INTRODUCE AS bzintroduce, A.BZ_FL AS bzfl," \
              " A.SRC_NAME AS srcname, A.ID AS id " \
              " FROM DAILYBLOG_AUTHOR_RESOURCE_TABLE A WHERE 1 = 1" \
              " AND A.BZ_FL=%s "%(bzfl)
        if(''!=bzname):
           SQL +="AND A.BZ_NAME LIKE %"+bzname+"%"
        SQL += " ORDER BY  POPULATION DESC  LIMIT %s,%s"%(start,limit)
        logger.info('查询财经作者列表信息...！'+SQL)
        resources = session.select_result(SQL)
        return resources

    def byresourcetype_count(self,bzfl,bzname):
        session = Session('master')
        SQL = " SELECT COUNT(ID) AS COUNTS " \
              " FROM DAILYBLOG_AUTHOR_RESOURCE_TABLE A WHERE 1 = 1" \
              " AND A.BZ_FL=%s "%(bzfl)
        if(''!=bzname):
           SQL +="AND A.BZ_NAME LIKE %"+bzname+"%"
        logger.info('查询财经作者列表信息...！'+SQL)
        resources = session.select_resultone(SQL)
        return resources