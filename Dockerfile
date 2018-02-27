FROM fedora:25

RUN dnf install -y gcc-c++
RUN dnf install -y ninja-build
