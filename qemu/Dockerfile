FROM docker.io/library/alpine:latest

RUN apk add qemu-system-i386 && \
    mkdir /image

ENTRYPOINT ["qemu-system-i386"]
