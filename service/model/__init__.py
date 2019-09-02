import pymysql as sql

def selectLogin(uid, upw):
    db_session = None
    row = None
    try:
        db_session = sql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='python_db',
                            charset='utf8',
                            cursorclass=sql.cursors.DictCursor)
        print("디비접속성공")
        with db_session.cursor() as cursor:
            sql_str = "SELECT * FROM users WHERE uid=%s AND upw=%s;"
            cursor.execute(sql_str, (uid, upw))  # 튜플이 1개일 경우 ('m',
            row = cursor.fetchone() #row는 회원정보
    except Exception as e:
        print(e)
    finally:
        if db_session: #비번틀렸을 때 db_session은 None이 되므로 확인하기
            db_session.close()
            print("디비접속해제성공")
    #쿼리결과인 회원정보리턴
    return row




# 코드를 테스트할 때는 원하지 않을 때 작동되지 않도록
# 처리구문필요
# if __name__ == '__main__':

   


    
