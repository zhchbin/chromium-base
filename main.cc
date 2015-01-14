// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "base/at_exit.h"
#include "base/location.h"
#include "base/message_loop/message_loop.h"
#include "base/run_loop.h"
#include "base/strings/string_number_conversions.h"
#include "base/files/file_util.h"
#include "base/time/time.h"
#include "base/logging.h"

int main(int argc, char* argv[]) {
  base::AtExitManager exit_manager;
  if (argc <= 1) {
    LOG(INFO) << argv[0] << ": missing operand";
    return -1;
  }

  int duration_seconds = 0;
  if (!base::StringToInt(argv[1], &duration_seconds) ||
      duration_seconds < 0) {
    LOG(INFO) << argv[0] << ": invalid time interval '" << argv[1] << "'";
    return -1;
  }

  base::TimeDelta duration = base::TimeDelta::FromSeconds(duration_seconds);
  base::MessageLoop main_loop;
  base::RunLoop run_loop;
  main_loop.PostDelayedTask(FROM_HERE, run_loop.QuitClosure(), duration);
  run_loop.Run();

  return 0;
}
