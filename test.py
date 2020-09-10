#!/usr/bin/env python3

import re 


def version_change(text):
	version = "1.1"
	pattern = r'"version": ("\d+\.\d+(-commit\d+)")'
	old_version = re.sub(r'\\g<1>',version,text)
	new_version = text.replace(old_version,version,1)
	
	return(new_version)
print(version_change('"version": "1.0-commit0"'))
