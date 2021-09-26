FROM docker.io/library/alpine:latest

RUN apk add qemu-system-i386 && \
    adduser -S sledreguy && \
    adduser sledreguy qemu && \
    adduser sledreguy kvm && \
    mkdir /image && \
    chown -R sledreguy:qemu /image

USER sledreguy

ENTRYPOINT ["qemu-system-i386"]
