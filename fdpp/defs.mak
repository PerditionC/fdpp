# XCPU=86
# XCPU=186
XCPU=386

# XFAT=16
XFAT=32

PREFIX ?= /usr/local
DATADIR ?= $(PREFIX)/share
LIBDIR ?= $(PREFIX)/lib
INCLUDEDIR ?= $(PREFIX)/include
PKGCONFIGDIR ?= $(LIBDIR)/pkgconfig

DIRSEP = /
RM = rm -f
SHELL = /usr/bin/env bash
