#!/bin/bash

# Update & upgrade system
apt update && apt upgrade -y

apt install git -y           
pip install -U pip    

# Clone the repo 
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Eldorado-k/Auto-Fil
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Auto-Fil
fi

# Upgrade pip and install requirements
cd /Auto-Fil
pip install -U -r requirements.txt --force-reinstall

# Start bot
echo "Starting Bot....✨"
python3 bot.py

