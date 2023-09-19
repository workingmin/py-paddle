#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#
#   https://github.com/PaddlePaddle/PaddleHub/tree/develop/modules/audio/tts/fastspeech2_baker
#

import sys
import os
import paddle
import paddlehub as hub

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<sentence>")
        sys.exit(1)

    sentence = sys.argv[1]
    sentences = []
    sentences.append(sentence)
    device = 'cpu'
    if paddle.get_device().startswith('gpu'):
        device = 'gpu'
    build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')
    if not os.path.exists(build_dir):
        os.mkdir(build_dir)

    model = hub.Module(name='fastspeech2_baker', version='1.0.0', output_dir=build_dir)
    wav_files =  model.generate(sentences=sentences, device=device)
    print(wav_files[0])
