#!/bin/bash
# script to set up a new user in Kali
# creates user, changes their shell to zsh, and adds them to sudoers

if [ "$#" -ne 1 ] 
    then 
        echo "usage: ./newuser.sh <username>"
else

    sudo adduser $1 && sudo chsh -s /usr/bin/zsh $1; sudo usermod -aG sudo $1

fi
