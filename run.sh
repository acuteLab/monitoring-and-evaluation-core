
# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green} ===== Development Server ===== ${reset}"

cd authentication_service

sleep 2
echo "${green}>>> activate the .venv.${reset}"
source $(pipenv --venv)/bin/activate

sleep 2
echo "${green}>>> starting Project ${reset}"
uvicorn main:app --port 8002 --reload

sleep 2
cd ..
echo "${green}>>> Creating New Tab for starting Another Service ${reset}"
gnome-terminal --tab
sleep 2

cd project_m_n_e_service
echo "${green}>>> activate the .venv.${reset}"
source $(pipenv --venv)/bin/activate

sleep 2
echo "${green}>>> Running Another Service (Project_m_n_e_service) ${reset}"
python manage.py runserver 
