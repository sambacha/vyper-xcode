FROM python:3.7-slim

ENV PYTHON_VERSION=3.7.10

ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=true

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Specify label-schema specific arguments and labels.
ARG BUILD_DATE
ENV BUILD_DATE=${BUILD_DATE}
ARG VCS_REF
ENV VCS_REF=${VCS_REF}
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Vyper" \
      org.label-schema.description="Vyper is an experimental programming language" \
      org.label-schema.url="https://vyper.readthedocs.io/en/latest/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/vyperlang/vyper.git" \
      org.label-schema.vendor="Vyper Team" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

# coincurve requires libgmp
RUN apt-get update && apt-get install -y -qq --no-install-recommends \
        apt-utils \
        gcc \
        git \
        libc6-dev \
        libc-dev \
        libssl-dev \
        libgmp-dev \
    && rm -rf /var/lib/apt/lists/*

ADD . /code

WORKDIR /code

# Using "test" optional to include test dependencies in built docker-image
RUN pip install .[test] && \
    apt-get purge -y -qq --auto-remove apt-utils gcc libc6-dev libc-dev libssl-dev

ENTRYPOINT ["/usr/local/bin/vyper"]
