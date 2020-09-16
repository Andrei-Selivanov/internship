#!/usr/bin/env python3

import sys
import json

def name_search(content, name, version):
	for i in content.values():
		if type(i) is dict:
			name_search(i,name,version)
		else:
			for k in i:
				if k["name"] == name:
					k["version"] = version
					break	

def version_change(input_file,name, version):
	with open(input_file, 'r') as f:
		content = json.load(f)
	f.close()
	name_search(content,name,version)			
	with open (input_file, 'w') as f:
		json.dump(content, f , sort_keys = True, indent = 2)
	f.close()

version_change(sys.argv[1], sys.argv[2],sys.argv[3])
