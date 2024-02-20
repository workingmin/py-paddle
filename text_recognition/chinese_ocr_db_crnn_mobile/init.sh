#!/usr/bin/env bash

workdir=$(cd $(dirname $0);pwd)
cd $workdir

py=`which python3.8`
virtualenv --python=$py venv

source venv/bin/activate
bash ../../init_hub.sh

cd $workdir
pip install shapely pyclipper

hub install chinese_ocr_db_crnn_mobile
