#!/bin/bash
dd if=/dev/zero of=test.log bs=1024 count=102400
for i in {1..50}; do dd if=/dev/zero bs=1024 count=102400 of=temp$i.log; done
