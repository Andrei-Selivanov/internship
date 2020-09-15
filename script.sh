#!/bin/bash

cd internship/
sudo git fetch origin
sudo git add version.json
sudo git commit -am "update version"
sudo git pull https://github.com/Andrei-Selivanov/internship
sudo git reset --merge
sudo git add version.json
sudo git commit -am "update version"
sudo git push https://github.com/Andrei-Selivanov/internship
#sudo exec < 0 github_nickname
#sudo exec < 0 github_pass
cd ..
