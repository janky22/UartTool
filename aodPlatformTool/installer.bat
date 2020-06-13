pyinstaller -F -w -i ioc1.ico -n aodPlatformTool seleniun.py
if not exist  dist\ioc1.ico (
    xcopy ioc1.ico dist
)
rmdir /s /q __pycache__
rmdir /s /q build
