#!/usr/bin/env bash

workdir=$(cd $(dirname $0);pwd)
cd $workdir

py=`which python3.8`
virtualenv --python=$py venv

source venv/bin/activate
bash ../../init_hub.sh

python -m pip install typeguard==2.13.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
hub install fastspeech2_baker