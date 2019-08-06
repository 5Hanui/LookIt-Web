import cv2 as cv
import numpy

def text_localization(img):
    resimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    ret, thr = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    height = img.shape[0]
    width = img.shape[1]

    start_row = []
    end_row = []
    start_box = []
    end_box = []

    check = False

    for i in range(height):
        total = 0

        for j in range(width):
            total += thr[i][j]

        total /= width

        if  check == False and total != 255:
            start_row.append(i)
            check = True
    #         cv.line(resimg, (0, i), (width - 1, i), (0, 0, 255), 1)

        if check == True and total == 255:
            end_row.append(i)
            check = False
    #         cv.line(resimg, (0, i), (width - 1, i), (0, 0, 255), 1)

    if len(start_row) > len(end_row):
        del start_row[-1]
    elif len(start_row) < len(end_row):
        del end_row[-1]

    for row in range(len(end_row)):
        split_img = thr[start_row[row]:end_row[row], 0:width].copy()

        split_res = cv.cvtColor(split_img, cv.COLOR_GRAY2BGR)
        height_s = split_img.shape[0]

        check = False

        for i in range(width):
            total = 0

            for j in range(height_s):
                total += split_img[j][i]

            total /= height_s

            if check == False and total != 255:
                start_box.append([start_row[row], i])
                check = True
    #             cv.line(resimg, (i, start_row[row]), (i, end_row[row]), (0,0,255), 1)

            if check == True and total == 255:
                end_box.append([end_row[row], i])
                check = False
    #             cv.line(resimg, (i, start_row[row]), (i, end_row[row]), (0,0,255), 1)

    if len(start_box) > len(end_box):
        del start_box[0]
    elif len(start_box) < len(end_box):
        del end_box[0]

    num = 0
    f_start = []
    f_end = []
    for i in range(len(end_box)):
 ##       if i == 0 :
 ##           continue
        if (num != start_box[i][0]) :
            ##print('box_start:{}, box_end:{}'.format(start_box[i], end_box[i]))
 ##           if i == 1 :
 ##               continue
            if (end_box[i][0] - start_box[i][0]) < 10 :
                continue
            if (end_box[i][1] - start_box[i][1]) < 10 :
                continue
            f_start.append(start_box[i])
            f_end.append(end_box[i])
            num =start_box[i][0]

    
    return f_start, f_end

if __name__ == '__main__':
    print('~')