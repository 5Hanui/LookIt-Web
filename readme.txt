# 개요
 - 본 서비스는 flask로 개발이 끝난 상황에서 
 - 디자인을 받아서 입히는 과정을 구현한 것 //https://startbootstrap.com/template-overviews/sb-admin-2/
    //다운받아서 practice\flask_cms\service\static 에 복사-> 다 정적데이터들임., html들은 templates폴더에다 옮기기.
 - 페이지 분할 처리법, 세션, 라이프사이클 등
   부속 기능을 확인


# 구조
LookIt-Web
    └ service           : 서비스 핵심 구현 패키지
        └ templates     : html 위치한곳
            └ mod       : 공용 html 파일
            └ pages     : 페이지당 콘텐츠가 실제 구현되는 파일
            *.html      : 페이지 자체 파일(구조가 구현된), 홈, 로그인, ...
        └ static        : 정적데이터 위치한곳
        └ DL            : 딥러닝 모델 패키지 구현
            └ mod       : 딥러닝모델 파일 위치한 곳
        └ __init__.py   : service 패키지 구현부분
    └ run.py            : 시작점
    └ readme.py         : 서비스 설명