
# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green} ===== Development Server ===== ${reset}"
# cd authentication_service

sleep 2
echo "${green}>>> activate the Virtual Environment ${reset}"
source $(pipenv --venv)/bin/activate

sleep 2
echo "${green}>>> starting Server (Authentication Service Server) ${reset}"
uvicorn main:app --port 8002 --reload