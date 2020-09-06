@echo off
CALL merge_submodules.cmd
git add . 
git commit -m "fuck" 
git push origin master
cd ..