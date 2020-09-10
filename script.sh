
#-
#  name: Clone GitHub repo
#  hosts: localhost
#  vars:
BRANCH="https://github.com/prosto-artem/internship"
#DIRECTORY="GitHub_repo/"
VERSION="1.0-commit1"

 # tasks:
#sudo mkdir $DIRECTORY     
#cd $DIRECTORY
sudo git init
sudo git clone ${BRANCH}
sudo sed -i -e s@$(jq .version intership/version.json)@${VERSION}@g internship/version.json
#sudo git remote add origin ${BRANCH}
#sudo git remote -v
#sudo git commit -m "Commit version" intership/version.json
sudo git push -f origin master intership/version.json   
cd ..
#sudo rm -rf {{ directory }}

