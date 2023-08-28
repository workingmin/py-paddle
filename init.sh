#!/use/bin/env bash

bash venv.sh
if test -z "$(which nvcc)"; then
    is_gpu=false
else
    is_gpu=true
fi

source venv/bin/activate
if $is_gpu; then
    pip install paddlepaddle-gpu==2.4.2.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
    pip install -r requirements.gpu.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
else
    pip install -r requirements.cpu.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
fi
