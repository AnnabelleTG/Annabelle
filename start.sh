#!/bin/bash

cyan="\033[1;36m"
reset="\033[0m"
white="\033[1;97m"
red="\033[1;91m"

echo -e "${white}[ ${red}* ${white}] ${cyan} Installing required packages !!${reset}\n"

packages=(git python)

for pkg in "${packages[@]}" ; do
  if ! hash ${pkg} > /dev/null 2>&1 ; then
    echo -e "\n${white}[ ${red}* ${white}] ${cyan} Installing ${pkg} ${reset}\n"
    apt install "${pkg}" -y || sudo apt install "${pkg}" -y
  fi

done

echo -e "\n${white}[ ${red}* ${white}] ${cyan} Cloning into Annabelle ${reset}\n"
git clone https://github.com/Vaishnavofficial/Annabelle/tree/main/annabelle

echo -e "${white}[ ${red}* ${white}] ${cyan} Instaling pip modules !${reset}\n"
pip install -r ./Annabelle/requirements.txt


clear
echo -e "${white}[ ${red}* ${white}] ${cyan} Starting Annabelle !"

python ./Annabelle/bot.py &
python ./Annabelle/userbot.py &
