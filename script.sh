#!/bin/bash

cd internship/
#git fetch origin
git pull git@github.com:Andrei-Selivanov/internship.git
git add version.json
git commit -am "update version"
git push git@github.com:Andrei-Selivanov/internship.git
cd ..
