#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import json
from paddlenlp import Taskflow

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <inout.json>")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as f:
            obj = json.loads(f.read())

        image_url = obj.get('image_url')
        schema = obj.get('schema')
        ie = Taskflow("information_extraction", schema=schema, model="uie-x-base", layout_analysis=True)
        print(ie({"doc": image_url}))
    except Exception as e:
        print("failure. " + str(e))
