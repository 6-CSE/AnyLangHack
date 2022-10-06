@echo off
echo Hello
cd c:\
cd /d "%USERPROFILE%\Desktop"
set "myserialnumber="

for /f "skip=1 delims=" %%a in ('"wmic bios get serialnumber"') do (
    for /f "delims=" %%b in ("%%a") do if not defined myserialnumber set "myserialnumber=%%~nb"
)

echo PC Serial Number: "%myserialnumber%"
echo Getting Software List Please wait this may take sometime ...

wmic /output:%myserialnumber%.csv product get Name,Version,ProductID,InstallDate,PackageName /format:csv

echo Done a csv file is generated with %myserialnumber%.csv on your desktop

pause
