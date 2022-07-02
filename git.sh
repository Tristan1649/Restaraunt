
#!/bin/bash

echo "Start"


git init
git add --all
git commit -a -m 'first commit'
git remote add origin git@github.com:Tristan1649/Restaraunt.git
git pull --rebase origin master
git push origin master

echo "Finish"