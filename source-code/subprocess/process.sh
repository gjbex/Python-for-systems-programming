#!/usr/bin/env bash

for i in {1..4}
do
    (>&2 echo "### info: $i in progress...")
    sleep 5
    echo "item $i: $((i**2))"
done
