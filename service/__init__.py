'''
 flask 객체 생성
 기본 환경설정
 환경 변수, 디비 초기화
 라우트(블루 프린트)
 라이프사이클(생애주기)
 필터(세션처리)
'''
from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
# 서버 시작점에서부터 패키 경로를 따진다.
import os # 원래는 맨위
from service.model import selectLogin
# from service.model import insertBbsData, selectBbsList
from service.DL import dl_folder
# from service.model import * 하면 예약어 쓸수가 없음 as불가능

# 플라스크 앱 생성
def createApp():
    app = Flask(__name__)
    # 1. 세션 키 생성 => 통상 값은 해쉬값(중복되지 않는 임의값) 사용
    app.secret_key = 'adfad2321fa34dfasdfadfafdff13131kjjlk12' # 사용자가 많지 않으므로 임의로 사용
    initRoute(app)
    return app

# 라우트 초기화 담당
def initRoute(app):
    # 라우트 설정
    @app.route('/', methods=['GET','POST'])
    def home():
    # ----------
        if request.method == 'GET':
            return render_template('index.html')
        else:
            # 1. 데이터 획득
            files       = request.files.getlist('files')
            nmList = list()
            for file in files: # 파일리스트
                # file : 파일 
                save_path = os.path.join(os.getcwd(),
                                        'service', 'static', 'upload', os.path.basename(file.filename))
                # 모든 파일을 디스크상에 저장
                # f->file로 수정후 ctrl+shift+R
                file.save(save_path)
                nmList.append(save_path)
            # path_dir = './service/static/upload'
            dl_folder()
            #######################################################3
            return render_template('index.html')


    # 로그인
    @app.route('/login', methods=['GET','POST'])
    def login():
        if request.method=='GET':
            # 쿠키를 읽어와서 아이디창에 채운다.
            uid = request.cookies.get('uid')
            if not uid: # 쿠키 없으면
                uid = '' #쿠키는 아이디를 들고 있거나 없거나.
            return render_template('login.html',
                    title='로그인',uid=uid)
        else: 
            # 잘 넘어오는지 체크
            uid = request.form.get('uid')
            upw = request.form.get('upw')
            if not uid or not upw:
                return render_template("alertEx.html", msg='정확하게 입력하세요')
            else:
                row = selectLogin(uid,upw)
                if row: #회원이다
                    session['uid'] = uid
                    session['name'] = row['name'] #row에 조회결과 있음//
                    return redirect(url_for('home')) # url은 직접 하드코딩하지 않는다!! redirect('/')=>XX
                else: #회원아니다
                    return render_template("alertEx.html", msg='회원아님')
    
    # 로그아웃
    @app.route('/logout') 
    def logout():
        # 세션 없이 접근했을 경우 -> 홈페이지로 리다이렉트
        if not 'uid' in session:  # 세션체크
            return redirect(url_for('home'))
        # 세션제거
        if 'uid' in session:
            session.pop('uid', None) #uid를 제거하면서 반환해줌
        if 'name' in session:
            session.pop('name', None)
        # 홈페이지 리다이렉트
        return redirect(url_for('home'))




