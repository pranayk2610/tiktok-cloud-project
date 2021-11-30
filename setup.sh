rm -r venv

pipx install virtualenv

virtualenv venv 

source venv/bin/activate

pip3 install -r requirements.txt 