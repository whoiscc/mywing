# 依赖文件列表
certifi-2019.6.16-py2.py3-none-any.whl
chardet-3.0.4-py2.py3-none-any.whl
Django-2.2.2-py3-none-any.whl
django_cors_headers-2.5.1-py2.py3-none-any.whl
idna-2.8-py2.py3-none-any.whl
pytz-2019.1-py2.py3-none-any.whl
requests-2.22.0-py2.py3-none-any.whl
sqlparse-0.3.0-py2.py3-none-any.whl
urllib3-1.25.3-py2.py3-none-any.whl
请将以上文件放在whls文件夹中，压缩包可以从 https://mywing.ddltech.top/whls.zip 下载

# 构建
`bash help.sh build`
Windows下请确保安装了最新的Docker for windows，并执行：
`docker build -t mywing/server-container:1.0 .`
