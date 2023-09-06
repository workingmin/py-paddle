#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#
#   https://github.com/PaddlePaddle/PaddleHub/tree/develop/modules/audio/asr/deepspeech2_librispeech
#

import sys
import paddle
import paddlehub as hub

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<wav-file>")
        exit(1)

    wav_file = sys.argv[1]
    model = hub.Module(name='deepspeech2_librispeech', version='1.0.0')
    device = 'cpu'
    if paddle.get_device().startswith('gpu'):
        device = 'gpu'
    
    text = model.speech_recognize(wav_file, device=device)
    print(text)