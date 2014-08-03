from db_util import orm

"""配置orm映射关系"""
@orm(table="whkt_resource_table", params="ID, CREATEDATE, IMAGEURL, TITLE")
class Resource(dict):
    """继承dict，返回就是按照字典列表，也可以不继承dict,返回就是按照对象的列表"""
    pass
