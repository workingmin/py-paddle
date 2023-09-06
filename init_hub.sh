#!/usr/bin/env bash

if test -z "$(which nvcc)"; then
    is_gpu=false
else
    is_gpu=true
fi

if $is_gpu; then
    python -m pip install paddlepaddle-gpu==2.4.2.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
else
    python -m pip install paddlepaddle==2.4.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
fi

python -m pip install setuptools==58.3.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install protobuf==3.20.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install paddlenlp==2.5.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install paddlehub==2.3.1 -i https://pypi.tuna.tsinghua.edu.cn/simple