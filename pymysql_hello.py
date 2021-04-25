import pymysql


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306,user='root',password='383240gyz',db='bycicle',charset='utf8')
    print(conn)
    try:
        with conn.cursor() as cursor: # 上下文语法否则需要    # cursor.close()
            cursor.execute('''drop table if exists pymysql''')
            cursor.execute(''' create table pymysql (a int,b int)''')
            cursor.execute('''insert into pymysql(a,b) values(1,1) ''')
        conn.commit()
    except pymysql.MySQLError as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
