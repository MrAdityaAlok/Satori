FROM scratch AS ctx
COPY build_files /
COPY sys_files /sys_files

FROM quay.io/fedora/fedora-bootc:43

ARG VARIANT
ENV VARIANT=$VARIANT

RUN --mount=type=bind,from=ctx,source=/,target=/ctx \
    --mount=type=cache,dst=/var/cache \
    --mount=type=cache,dst=/var/log \
    --mount=type=tmpfs,dst=/tmp \
    /ctx/build.sh

#For testing:
# RUN mkdir -p /var/spool/mail && \
#     useradd -m -G wheel -s /bin/bash satori && \
#     echo 'satori:satori' | chpasswd

RUN bootc container lint
