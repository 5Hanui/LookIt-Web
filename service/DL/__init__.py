import numpy as np
import cv2 as cv, os
from service.text_localization import text_localization
from keras.models import load_model
# import matplotlib.pyplot as plt
# from keras.preprocessing import image

answer = [[],[],[],[],[]]
def deep_machine(img) :
    model1 = load_model('./service/DL/model/CNN_colab_m1.h5')
    model2 = load_model('./service/DL/model/CNN_colab_m2.h5')
    model3 = load_model('./service/DL/model/CNN_colab_m3.h5')
    model4 = load_model('./service/DL/model/CNN_colab_m4.h5')
    model5 = load_model('./service/DL/model/CNN_colab_m5.h5')
    print(img)
    img = cv.imread(img,0)

    resimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    # ======================================================
    ret, thr = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

    start_box, end_box = text_localization(thr)

    box_list = []

    count = 1
    q_num = 1
    check = 0
    # answer = [[0 for j in range(1)] for i in range(5)]

    # print(answer)
    print(range(len(start_box)))
    for i in range(len(start_box)):
        if len(start_box) != 26 :
            break

        if count % 6 == 4 : #1번 체크
            save_img = img[start_box[i][0]:end_box[i][0], start_box[i][1]:end_box[i][1]].copy()
            save_img = cv.resize(save_img, (64, 64), interpolation=cv.INTER_CUBIC)
            save_img = cv.cvtColor(save_img, cv.COLOR_GRAY2BGR)
        
            cols, rows = save_img.shape[:2]
            M = cv.getRotationMatrix2D((cols/2, rows/2), 180, 1)
            save_img = cv.warpAffine(save_img, M, (cols, rows))
        
            save_img = save_img.reshape(-1, 64, 64, 3)
            save_img = save_img.astype('float32')/ 255

            yhat = model1.predict(save_img)
        
            if yhat[0][0] >= 0.5:
                color = (0, 0, 255)
                prediction = 'check 1'
                check = 1
            
            else :
                color = (255, 0, 0)
                prediction = 'non 1'
            
            # print('  => predict = ', yhat[0][0], ', class = ', prediction)
            
            cv.rectangle(resimg, 
                    (start_box[i][1], start_box[i][0]), 
                    (end_box[i][1], end_box[i][0]), 
                    color)
        
            count = count + 1
            
        elif count % 6 == 5 : #2번 체크
            save_img = img[start_box[i][0]:end_box[i][0], start_box[i][1]:end_box[i][1]].copy()
            save_img = cv.resize(save_img, (64, 64), interpolation=cv.INTER_CUBIC)
            save_img = cv.cvtColor(save_img, cv.COLOR_GRAY2BGR)
        
            cols, rows = save_img.shape[:2]
            M = cv.getRotationMatrix2D((cols/2, rows/2), 180, 1)
            save_img = cv.warpAffine(save_img, M, (cols, rows))
        
            save_img = save_img.reshape(-1, 64, 64, 3)
            save_img = save_img.astype('float32')/ 255

            yhat = model2.predict(save_img)
        
            if yhat[0][0] >= 0.5:
                color = (0, 0, 255)
                prediction = 'check 2'
                check = 2
            
            else :
                color = (255, 0, 0)
                prediction = 'non 2'
            
            # print('  => predict = ', yhat[0][0], ', class = ', prediction)
            
            cv.rectangle(resimg, 
                    (start_box[i][1], start_box[i][0]), 
                    (end_box[i][1], end_box[i][0]), 
                    color)
        
            count = count + 1
            
        elif count % 6 == 0 : #3번 체크
            save_img = img[start_box[i][0]:end_box[i][0], start_box[i][1]:end_box[i][1]].copy()
            save_img = cv.resize(save_img, (64, 64), interpolation=cv.INTER_CUBIC)
            save_img = cv.cvtColor(save_img, cv.COLOR_GRAY2BGR)
        
            cols, rows = save_img.shape[:2]
            M = cv.getRotationMatrix2D((cols/2, rows/2), 180, 1)
            save_img = cv.warpAffine(save_img, M, (cols, rows))
        
            save_img = save_img.reshape(-1, 64, 64, 3)
            save_img = save_img.astype('float32')/ 255

            yhat = model3.predict(save_img)
        
            if yhat[0][0] >= 0.5:
                color = (0, 0, 255)
                prediction = 'check 2'
                check = 3
            
            else :
                color = (255, 0, 0)
                prediction = 'non 2'
            
            # print('  => predict = ', yhat[0][0], ', class = ', prediction)
            
            cv.rectangle(resimg, 
                    (start_box[i][1], start_box[i][0]), 
                    (end_box[i][1], end_box[i][0]), 
                    color)
        
            count = count + 1
            
        elif count % 6 == 1 : #4번 체크
            if i == 0 :
                count = count + 1
                continue
            save_img = img[start_box[i][0]:end_box[i][0], start_box[i][1]:end_box[i][1]].copy()
            save_img = cv.resize(save_img, (64, 64), interpolation=cv.INTER_CUBIC)
            save_img = cv.cvtColor(save_img, cv.COLOR_GRAY2BGR)
        
            cols, rows = save_img.shape[:2]
            M = cv.getRotationMatrix2D((cols/2, rows/2), 180, 1)
            save_img = cv.warpAffine(save_img, M, (cols, rows))
        
            save_img = save_img.reshape(-1, 64, 64, 3)
            save_img = save_img.astype('float32')/ 255

            yhat = model4.predict(save_img)
        
            if yhat[0][0] >= 0.5:
                color = (0, 0, 255)
                prediction = 'check 2'
                check = 4
            
            else :
                color = (255, 0, 0)
                prediction = 'non 2'
            
            # print('  => predict = ', yhat[0][0], ', class = ', prediction)
            
            cv.rectangle(resimg, 
                    (start_box[i][1], start_box[i][0]), 
                    (end_box[i][1], end_box[i][0]), 
                    color)
        
            count = count + 1
            
        elif count % 6 == 2 : #5번 체크
            if i == 1:
                count = count + 1
                continue
            save_img = img[start_box[i][0]:end_box[i][0], start_box[i][1]:end_box[i][1]].copy()
            save_img = cv.resize(save_img, (64, 64), interpolation=cv.INTER_CUBIC)
            save_img = cv.cvtColor(save_img, cv.COLOR_GRAY2BGR)
        
            cols, rows = save_img.shape[:2]
            M = cv.getRotationMatrix2D((cols/2, rows/2), 180, 1)
            save_img = cv.warpAffine(save_img, M, (cols, rows))
        
            save_img = save_img.reshape(-1, 64, 64, 3)
            save_img = save_img.astype('float32')/ 255

            yhat = model5.predict(save_img)
        
            if yhat[0][0] >= 0.5:
                color = (0, 0, 255)
                prediction = 'check 2'
                check = 5
            
            else :
                color = (255, 0, 0)
                prediction = 'non 2'
            
            # print('  => predict = ', yhat[0][0], ', class = ', prediction)
            
            cv.rectangle(resimg, 
                    (start_box[i][1], start_box[i][0]), 
                    (end_box[i][1], end_box[i][0]), 
                    color)
            # print(check)
            answer[q_num].append(check)
            # print(check)
            q_num = q_num + 1
            check = 0
            count = count + 1
            
        elif count % 6 == 3 : #번호
            count = count + 1
    
    cols, rows = resimg.shape[:2]

    M = cv.getRotationMatrix2D((rows/2, cols/2), 180, 1)
    resimg = cv.warpAffine(resimg, M, (rows, cols))

    # cv.imwrite('./text_local_' + str(img) + '.png', resimg)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print(answer)
    return answer
    # print(answer)
    # return answer
path_dir = './service/static/upload'
def dl_folder():
    answer = [[],[],[],[],[]]
# path_dir = './static/upload'
    file_list = os.listdir(path_dir)
    # file_list2 = os.listdir('./')
    # print(file_list2)
    for f in file_list:
        print(f)
        answer +=deep_machine(path_dir+'/'+f)

    print(answer)
# deep_machine('./doc/img1.jpg')