# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This gypi file defines the patterns used for determining whether a
# file is excluded from the build on a given platform.

{
  'target_conditions': [
    ['OS!="win"', {
      'sources/': [ ['exclude', '_win(_browsertest|_unittest)?\\.(h|cc)$'],
                    ['exclude', '(^|/)win/'],
                    ['exclude', '(^|/)win_[^/]*\\.(h|cc)$'] ],
    }],
    ['OS!="mac"', {
      'sources/': [ ['exclude', '_(cocoa|mac)(_unittest)?\\.(h|cc|mm?)$'],
                    ['exclude', '(^|/)(cocoa|mac)/'] ],
    }],
    ['OS!="linux"', {
      'sources/': [
        ['exclude', '_linux(_unittest)?\\.(h|cc)$'],
        ['exclude', '(^|/)linux/'],
      ],
    }],
    ['OS=="win"', {
      'sources/': [
        ['exclude', '_posix(_unittest)?\\.(h|cc)$'],
        ['exclude', '(^|/)posix/'],
      ],
    }],
  ]
}
