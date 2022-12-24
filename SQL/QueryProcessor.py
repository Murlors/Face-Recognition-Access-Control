from SQL.ConnectionPool import ConnectionPool


class QueryProcessor:
    def __init__(self):
        # 与连接池连接
        self.conn_pool = ConnectionPool().conn_pool

    async def run_query(self, sql):
        # 从连接池中获取一个连接
        conn = self.conn_pool.getconn()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        # 将连接放回连接池中
        self.conn_pool.putconn(conn)
        return result


async def process_query(query):
    # 接收单独的SQL查询语句并返回相应的结果
    return await query_processor.run_query(query)


query_processor = QueryProcessor()

# @timeit
# def test():
#     queries = ["SELECT * FROM course", "SELECT * FROM dept", "SELECT * FROM sc", "SELECT * FROM student"]
#     for query in queries:
#         results = asyncio.run(process_query(query))
#         print(f"Query: {query}")
#         print(f"Result: {results}")
#
# if __name__ == '__main__':
#     start = time.time()
#     for i in range(100):
#         test()
#     end = time.time()
#     print(f"Time: {end - start}")
