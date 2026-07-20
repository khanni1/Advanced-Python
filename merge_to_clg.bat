@REM  merge main to other branch

@echo off

set /p branch_name=ENTER BRANCH NAME MAIN - xyz :

@REM set /p ff_option=Merging only if ff is possible (y/n): 
echo.

git checkout "%branch_name%"
git merge main


@REM below keep as it is just displaying no need to alter

echo.
git branch
echo.
git branch -vv

pause
git config --global user.email
git config --global user.name
echo.
pause
git status
echo.
pause
git log --oneline