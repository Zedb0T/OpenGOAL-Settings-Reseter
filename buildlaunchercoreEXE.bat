
set mypath=%~dp0
pyinstaller --onefile openGOALModLauncher.py --noconsole --icon resources\appicon.ico --add-data "joshvaccum.PNG;." --add-data "mod launcher splash 1.png;."
move "%mypath%dist\openGOALModLauncher.exe" "%mypath%/"
RENAME "%mypath%\openGOALModLauncher.exe" "openGOALModLauncher.exe"
@RD /S /Q "%mypath%/build"
@RD /S /Q "%mypath%/dist"
DEL /S /Q "%mypath%/openGOALModLauncher.spec"
