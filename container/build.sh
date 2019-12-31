#!/bin/sh

dir="/tmp/whls"
canBuild=1

check()
{
	if [ ! -e $dir/$1 ]
	then
		echo "$1 not found"
		canBuild=0
	fi
}

check certifi-2019.6.16-py2.py3-none-any.whl
check chardet-3.0.4-py2.py3-none-any.whl
check Django-2.2.2-py3-none-any.whl
check django_cors_headers-2.5.1-py2.py3-none-any.whl
check idna-2.8-py2.py3-none-any.whl
check pytz-2019.1-py2.py3-none-any.whl
check requests-2.22.0-py2.py3-none-any.whl
check sqlparse-0.3.0-py2.py3-none-any.whl
check urllib3-1.25.3-py2.py3-none-any.whl

if [ $canBuild -eq 1 ]
then
	echo "All whl files found, installing..."
else
	echo "The above whl files not found, can not build."
	exit -1
fi

# install
pip install /tmp/whls/sqlparse-0.3.0-py2.py3-none-any.whl \
    && pip install /tmp/whls/pytz-2019.1-py2.py3-none-any.whl \
    && pip install /tmp/whls/Django-2.2.2-py3-none-any.whl \
    && pip install /tmp/whls/django_cors_headers-2.5.1-py2.py3-none-any.whl \
    && pip install /tmp/whls/chardet-3.0.4-py2.py3-none-any.whl \
    && pip install /tmp/whls/idna-2.8-py2.py3-none-any.whl \
    && pip install /tmp/whls/certifi-2019.6.16-py2.py3-none-any.whl \
    && pip install /tmp/whls/urllib3-1.25.3-py2.py3-none-any.whl \
    && pip install /tmp/whls/requests-2.22.0-py2.py3-none-any.whl \

# clean
rm -rf /tmp/whls

# add curl
# sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
#     && apk add curl
