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
        sys.exit(1)

    wav_file = sys.argv[1]

    device = 'cpu'
    if paddle.get_device().startswith('gpu'):
        device = 'gpu'
    
    model = hub.Module(name='deepspeech2_librispeech', version='1.0.0')
    text = model.speech_recognize(audio_file=wav_file, device=device)
    print(text)
