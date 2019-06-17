FROM tiangolo/uwsgi-nginx:python3.7-alpine3.9

LABEL maintainer="FinnTenzor <finntenzor@gmail.com>"

COPY ./django_cors_headers-2.5.1-py2.py3-none-any.whl /tmp/django_cors_headers-2.5.1-py2.py3-none-any.whl

RUN pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install /tmp/django_cors_headers-2.5.1-py2.py3-none-any.whl \
    && pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && rm -f /tmp/django_cors_headers-2.5.1-py2.py3-none-any.whl
