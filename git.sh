
#!/bin/bash

echo "Start"

git init &&
git remote add origin git@github.com:Tristan1649/Restaraunt.git
git checkout -b chingiz
git add . &&
git commit -m "all" &&
git push origin chingiz

echo "Finish"
