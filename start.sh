#!/bin/bash

echo "pod started"

if [[ $PUBLIC_KEY ]]
then
    mkdir -p ~/.ssh
    chmod 700 ~/.ssh
    cd ~/.ssh
    echo $PUBLIC_KEY >> authorized_keys
    chmod 700 -R ~/.ssh
    cd /
    service ssh start
fi
cd /rag_localgpt_01
nohup python ./run_localGPT_API.py &
nohup python ./localGPTUI/localGPTUI.py
# python ingest.py (--device_type cpu)
# python run_localGPT.py --show_sources (--device_type cpu/mps --use_history)
sleep infinityß