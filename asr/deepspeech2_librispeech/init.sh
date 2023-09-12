#!/usr/bin/env bash

workdir=$(cd $(dirname $0);pwd)
cd $workdir

py=`which python3.8`
virtualenv --python=$py venv

source venv/bin/activate
bash ../../init_hub.sh

cd dependencies/swig
bash setup.sh

cd $workdir
python -m pip install soundfile==0.12.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install loguru==0.7.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install yacs==0.1.8 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install jsonlines==4.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install resampy==0.4.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install soxbindings==1.2.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install kaldiio==2.18.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install typeguard==2.13.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install editdistance==0.6.2 -i https://pypi.tuna.tsinghua.edu.cn/simple

hub install deepspeech2_librispeech 
hub_module_home=$(python -c "from paddlehub.env import MODULE_HOME; print(MODULE_HOME)")
wget -c -P $hub_module_home/deepspeech2_librispeech/assets/data/lm https://deepspeech.bj.bcebos.com/en_lm/common_crawl_00.prune01111.trie.klm