#!/bin/bash
virtualenv venv
if [ $? -eq 0 ]; then
   echo OK
else
   printf "Error: Install virtualenv first: pip3 install virtualenv"
   exit
fi
source venv/bin/activate
pip3 install -r requirements.txt
printf "Succsess! Now you can run app by yourself. Activate venv and go ahead:\nsource venv/bin/activate\n./run.sh\n"
./run.sh
