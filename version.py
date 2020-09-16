#!/usr/bin/env python3

import sys
import json

def version_change(input_file,name, version):
	with open(input_file, 'r') as f:
		content = json.load(f)
	f.close()
	for i in content["backend_components"]["java"]:
		if i["name"] == name:
			i["version"] = version
			break
	with open (input_file, 'w') as f:
		json.dump(content, f , sort_keys = True, indent = 2)
	f.close()

version_change(sys.argv[1], sys.argv[2],sys.argv[3])
