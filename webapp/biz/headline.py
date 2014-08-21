#encoding=utf-8
from util.route import Router
from db_util import Session
from util.tools import Log

logger = Log().getLog()

class  HeadLineResourceAction(object):

    #获取当日头条新闻信息接口#
    @Router.route(url = r"headline/morningnews", method = Router._GET|Router._POST)
    def headline_morningnews_action(self,req):
        currentresource = self.headline_morningnews_resource()
        currentdata = []
        for current_diect in currentresource:
            title =''
            imageUrl =''
            descriptContext =''
            linkUrl =''
            for (key,value) in current_diect.iteritems():
                if('TITLE'==key):
                    title = value
                elif('IMAGEURL'==key):
                    imageUrl = value
                elif('DESCRIPTCONTEXT'==key):
                    descriptContext =str(value)
                elif('LINKURL'==key):
                    linkUrl =value
            currentdata.append({'title':title,'imageUrl':imageUrl,'descriptContext':descriptContext.replace('\t','').replace('\r',''),'linkUrl':linkUrl})
        return req.ok(currentdata)

    #查询当日头条新闻信息#
    def headline_morningnews_resource(self):
        session = Session('master')
        logger.info('查询当日头条新闻信息...！')
        sql = "SELECT HEADLINE.TITLE AS TITLE," \
              " HEADLINE.IMAGEURL AS IMAGEURL," \
              " SUBSTRING(HEADLINE.PUBDATE, 1,10) AS PUBDATE," \
              " HEADLINE.LINKURL AS LINKURL," \
              " HEADLINE.DESCRIPTCONTEXT AS DESCRIPTCONTEXT" \
              " FROM" \
              " HEADLINE_FINANCENEWS_RESOURCE_TABLE HEADLINE" \
              " WHERE 1 = 1" \
              " AND HEADLINE.TITLE !=''" \
              " AND HEADLINE.DESCRIPTCONTEXT !=''" \
              " ORDER BY HEADLINE.PUBDATE DESC LIMIT 0,6"
        print(sql)
        result = session.select_result(sql)
        return result