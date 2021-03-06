#!/usr/bin/env python3

import sys
import json

def version_change(input_file, version):
	with open(input_file, 'r') as f:
		content = json.load(f)
	f.close()
	content["version"] = version
	with open (input_file, 'w') as f:
		json.dump(content, f , sort_keys = True, indent = 2)
	f.close()

version_change(sys.argv[1], sys.argv[2])
