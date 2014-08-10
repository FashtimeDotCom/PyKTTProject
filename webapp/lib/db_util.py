# coding: utf-8

import redis, MySQLdb
from DBUtils import PooledDB
from c import confs


redis_pools = {}
mysql_pool = {}


def get_redis(dbid):
    conf = confs.redis[dbid]
    pool = redis_pools.get(dbid)
    if not pool:
        conf.setdefault('max_connections', 8)
        pool = redis.ConnectionPool(**conf)
        redis_pools[dbid] = pool
    return redis.Redis(connection_pool=pool)


def get_mysql(dbid):
    conf = confs.mysql[dbid]
    pool = mysql_pool.get(dbid)
    if not pool:
        conf.setdefault('maxcached', 30)
        pool = PooledDB.PooledDB(MySQLdb, **conf)
        mysql_pool['dbid'] = pool
    return pool.connection()

def orm(**conf):
    def wrap(entity):
        entity.table = conf['table']
        entity.params = conf['params']
        def wrap_args(*args, **kwargs):
            return entity(*args, **kwargs)
        return wrap_args
    return wrap

class Session(object):
    def __init__(self, dbid):
        self.con = get_mysql(dbid)
        self.close = self.con.close

    def __enter__(self, dbid):
        return Session(dbid)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()

    def __del__(self):
        self.con.close()


    def select(self, E, d):
        ret = []
        sql = "SELECT %s FROM %s "
        elf = E()
        sql %= (elf.params, elf.table)
        if d:
            where = 'WHERE '
            for k in d.keys():
                where += k + '=%s AND '
            where = where.strip('AND ')
            sql += where
        try:
            cursor = self.con.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(sql, tuple(d.values()))
            res = cursor.fetchall()
            if isinstance(elf, dict):
                return res
            else:
                for row in res:
                    e = E()
                    for k, v in row.iteritems():
                        e.__setattr__(k, v)
                    ret.append(e)
                return ret
        except Exception, e:
            raise e









