#!/usr/bin/env python3

import sys
import re

def version_change(input_file,version):
	with open(input_file, 'r') as f:
		filedata = f.read()
		f.close()
	pattern = r'"version": ("\d+\.\d+(-commit\d+)")'
	new_version = re.sub(r'\\g<1>',version,filedata)
	print(new_version)
	with open(input_file, 'w') as f:
		f.write(new_version)
	f.close()

version_change(sys.argv[1],sys.argv[2])
