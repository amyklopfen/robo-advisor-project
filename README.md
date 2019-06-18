# robo-advisor-project
robo advisor project

#repo set up

create a new repository with a README and a .gitignore

clone repository from GitHub.com and download to desktop

create a file named requirements.txt and save the following information in the file: 
requests
python-dotenv

#set up virtual environment

in gitbash, navigate to the file directory and set up a virtual environment using the following commands: 
conda create -n stocks-env python=3.7 
conda activate stocks-env

Then install packages for the app using the following commands: 
pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)




