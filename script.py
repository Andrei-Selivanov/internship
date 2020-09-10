#!/usr/bin/env python3

import json
import sys
import re

def version_change(input_file,version):
	with open(input_file, 'r') as f:
		filedata = json.load(f)
	f.close()
	filedata['version'] = version
	with open(input_file, 'w') as f:
		json.dump(filedata,f, sort_keys=True, indent=2)
	f.close()

version_change(sys.argv[1],sys.argv[2])
