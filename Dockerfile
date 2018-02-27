FROM fedora:25

RUN dnf install -y gcc-c++
RUN dnf install -y ninja-build

RUN mkdir -p /workspace/ISIS3_cmake && mkdir -p /workspace/ISIS3_cmake@tmp

ENTRYPOINT [ "/bin/bash", "-c", "--" ]
