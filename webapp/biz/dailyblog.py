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
        currentresource = self.byresourcetype_resource(bzfl,start,limit)
        count = self.byresourcetype_count(bzfl,start,limit)
        currentdata = []
        for current_diect in currentresource:
            bzname = None
            bzintroduce =None
            bzfl =None
            srcname =None
            id =None
            createdate =None
            population =None
            for (key,value) in current_diect.iteritems():
                if('BZNAME'== key):
                  bzname = value
                elif('BZINTRODUCE'==key):
                  bzintroduce =value
                elif('BZFL'==key):
                  bzfl = value
                elif('SRCNAME' == key):
                  srcname =value
                elif('ID'==key):
                  id =value
                elif('CREATEDATE'==key):
                  createdate =value
                elif('POPULATION'==key):
                   population =value
            currentdata.append({'bzname':bzname,'bzintroduce':bzintroduce,
                                'bzfl':bzfl,'srcname':srcname,'id':id,
                                'createdate':createdate,'population':population})
        return req.ok({'data':currentdata,'count':count})

    def byresourcetype_resource(self,bzfl,start,limit):
        session = Session('master')
        logger.info('查询财经作者列表信息...！')
        SQL = " SELECT A.BZ_NAME AS BZNAME, A.BZ_INTRODUCE AS BZINTRODUCE, A.BZ_FL AS BZFL," \
              " A.SRC_NAME AS SRCNAME, A.ID AS ID, A.CREATEDATE AS CREATEDATE, " \
              " A.POPULATION_FLAG /(SELECT MAX(RESOURCE.POPULATION_FLAG) FROM" \
              " DAILYBLOG_AUTHOR_RESOURCE_TABLE RESOURCE)* 100 AS POPULATION" \
              " FROM DAILYBLOG_AUTHOR_RESOURCE_TABLE A WHERE 1 = 1" \
              " AND A.BZ_FL=%s LIMIT %s,%s"%(bzfl,start,limit)
        resources = session.select_result(SQL)
        return resources

    def byresourcetype_count(self,bzfl,start,limit):
        session = Session('master')
        logger.info('查询财经作者列表信息...！')
        SQL = " SELECT COUNT(ID) " \
              " FROM DAILYBLOG_AUTHOR_RESOURCE_TABLE A WHERE 1 = 1" \
              " AND A.BZ_FL=%s LIMIT %s,%s"%(bzfl,start,limit)
        resources = session.select_resultone(SQL)
        return resources