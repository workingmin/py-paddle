#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#
#   https://github.com/PaddlePaddle/PaddleHub/tree/develop/modules/image/text_to_image/stable_diffusion
#

import sys
import os
import paddle
import paddlehub as hub

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<prompt>")
        exit(1)

    prompt = sys.argv[1]
    module = hub.Module(name='stable_diffusion')
    if paddle.get_device().startswith('gpu'):
        width = 512
        height = 512
    else:
        width = 64
        height = 64

    cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.cache')
    build_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')
    if not os.path.exists(build_dir):
        os.mkdir(build_dir)

    da = module.generate_image(text_prompts=prompt, width_height=[width, height], output_dir=cache_dir)
    da[0].chunks[-1].chunks.plot_image_sprites(skip_empty=True, show_index=True, keep_aspect_ratio=True)
    da[0].chunks[-1].chunks.save_gif(os.path.join(build_dir, str(da[0].id) + '-merged-result.gif'))

    output_png = os.path.join(build_dir, str(da[0].id) + '.png')
    da[0].save_uri_to_file(output_png)
    print("Image save to %s." % output_png)
