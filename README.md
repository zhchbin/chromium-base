# base-minimal

[![Build Status](https://travis-ci.org/zhchbin/chromium-base.svg?branch=master)](https://travis-ci.org/zhchbin/chromium-base)

Trimmed Chromium's base library, just add `base.gyp:base` to your gyp file to use them.

# To build

```bash
$ cd chromium-base
$ gyp --depth=. base.gyp -I src/build/common.gypi
$ ninja -C out/Debug
```
