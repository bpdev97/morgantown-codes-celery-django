FROM alpine:latest
LABEL maintainer="Brandon Phillips and Elliott Lannello"
LABEL Description="Python 3 Django Dev Image for Morgantown Codes Celery Django"

RUN apk update && apk add bash \
        gcc \
        make \
        libc-dev \
        musl-dev \
        linux-headers \
        pcre-dev \
        vim \
        python3 \
        python3-dev \
        python-dev \
        libxml2-dev \
        libxslt-dev \
	    libffi \
	    libffi-dev \
        zlib-dev \
        py-pip


ADD app/requirements.txt /requirements.txt

# Install requirements
RUN pip3 install -r /requirements.txt

# Start Django Dev Server
WORKDIR "/app"
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
