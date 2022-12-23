import asyncio
from psycopg2 import pool

from timeit import timeit


class QueryProcessor:
    def __init__(self, user='postgres', password='postgres', host='localhost', dbname='accesscontrolsystem'):
        # 创建连接池
        self.conn_pool = pool.ThreadedConnectionPool(
            minconn=4, maxconn=20, host=host, dbname=dbname, user=user, password=password)

    async def run_query(self, query):
        # 从连接池中获取一个连接
        conn = self.conn_pool.getconn()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        # 将连接放回连接池中
        self.conn_pool.putconn(conn)
        return result


async def process_query(query):
    # 接收单独的SQL查询语句并返回相应的结果
    return await query_processor.run_query(query)


@timeit
def test():
    queries = ["SELECT * FROM course", "SELECT * FROM dept", "SELECT * FROM sc", "SELECT * FROM student"]
    for query in queries:
        results = asyncio.run(process_query(query))
        print(f"Query: {query}")
        print(f"Result: {results}")


query_processor = QueryProcessor(dbname='test')
test()
