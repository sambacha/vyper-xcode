FROM python:3.7-slim as base

#ENV PYTHON_VERSION=3.7.10
ARG BUILD_DATE
ENV BUILD_DATE=${BUILD_DATE}
ARG VCS_REF
ENV VCS_REF=${VCS_REF}

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=true

ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1 \
    PYTHONFAULTHANDLER 1 

FROM base AS vyper

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

#ENV VYPER_REF='0.2.11'
# Using "test" optional to include test dependencies in built docker-image
RUN pip install . && \
    apt-get purge -y -qq --auto-remove apt-utils gcc libc6-dev libc-dev libssl-dev

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

ENTRYPOINT ["/usr/local/bin/vyper"]
# Specify label-schema specific arguments and labels.

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Vyper" \
      org.label-schema.description="Vyper is an experimental programming language" \
      org.label-schema.url="https://vyper.readthedocs.io/en/latest/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/vyperlang/vyper.git" \
      org.label-schema.vendor="Vyper Team" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"
