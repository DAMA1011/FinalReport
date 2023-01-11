import psycopg2


def get_conn():
    return psycopg2.connect(host='127.0.0.1',
                           user='postgres',
                           password='123456',
                           database='test',
                           charset='utf8')


def query_data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor(psycopg2.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()


def inser_or_update__data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()