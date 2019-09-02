a = ['A','B','C']
# 출력결과 : A|B|C
# 조인 // 리스트나 문자열은 시퀀스 타입
tmp = '|'.join(a)
print(tmp)
# 분해
print(tmp.split('|')) # 다시 리스틀 바뀜...