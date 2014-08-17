from db_util import orm


@orm(table="whkt_resource_table", params="ID, CREATEDATE, IMAGEURL, TITLE")
class Resource(dict):
    pass


@orm(table="datacenter_tradeactivity",params="STARTDATE,ENDDATE,CURRENTVALUE")
class TradeActivity(dict):
    pass