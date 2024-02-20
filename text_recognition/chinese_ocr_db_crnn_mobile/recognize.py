#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#
#   https://github.com/PaddlePaddle/PaddleHub/tree/develop/modules/image/text_recognition/chinese_ocr_db_crnn_mobile
#

import sys
import paddlehub as hub

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<image-file>")
        sys.exit(1)
    
    image_file = sys.argv[1]
    
    ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")
    result = ocr.recognize_text(paths=[image_file])
    if len(result) > 0 and result[0].get('data') is not None:
        data = result[0].get('data')
        print(data)
        # text = '\n'.join([ x.get('text') for x in data ])
    # print(text)
