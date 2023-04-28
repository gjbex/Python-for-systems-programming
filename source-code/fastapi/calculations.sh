#!/usr/bin/env bash

# start the server with
# uvivorn  calculator::app  --reload
#

source ~/.mamba_init.sh
mamba activate python_for_systems_programming

HOST=127.0.0.1:8000

echo "push 5"
curl --silent "http://$HOST/push/5"
echo ""

echo "push 7"
curl --silent "http://$HOST/push/7"
echo ""

echo "perform addition"
curl --silent "http://$HOST/compute/add" | json_pp
echo ""
