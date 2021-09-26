#!/bin/bash
# script to set up a new user in Kali
# Adds a new user, changes their shell to ZSH, and adds them to sudoers

if [ "$1" == "" ] 
then 
echo "./newuser.sh <username>"

else
USER=$1; sudo adduser $USER && sudo chsh -s /usr/bin/zsh $USER  && sudo usermod -aG sudo $USER
fi
