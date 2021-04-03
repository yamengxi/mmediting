import os
import os.path as osp

import cv2


def mywrite(path, img):
    # import pdb
    # pdb.set_trace()
    os.makedirs(osp.dirname(path), exist_ok=True)
    cv2.imwrite(path, img)

def generate_dataset(from_dir, to_dir):
    for mid_dir in os.listdir(from_dir):
        for video_name in os.listdir(osp.join(from_dir, mid_dir)):
            video = cv2.VideoCapture(osp.join(from_dir, mid_dir, video_name))
            rval, frame = video.read()
            cnt = 0
            while rval:
                mywrite(osp.join(to_dir, mid_dir, osp.splitext(video_name)[0] + str(cnt).zfill(6) + '.png'), frame)
                if cnt % 100 == 0:
                    print('Processing ' + osp.join(to_dir, mid_dir, osp.splitext(video_name)[0] + str(cnt).zfill(6) + '.png'))
                rval, frame = video.read()
                cnt += 1


from_dir='/data/yamengxi/public_datasets'
to_dir='/data/dataset/VIRAT_test'

generate_dataset(from_dir, to_dir)









