@echo off

set /p branch_name=ENTER BRANCH NAME TO MERGE INTO MAIN:

set /p ff_option=Merging only if ff is possible (y/n) or just press enter: 
echo.

if /I "%ff_option%"=="n" (
    git merge "%branch_name%"
) else (
    git merge --ff-only "%branch_name%"
)

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