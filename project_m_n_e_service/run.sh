
# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green} ===== Development Server ===== ${reset}"

# cd project_m_n_e_service
echo "${green}>>> activate the Virtual Environment ${reset}"
source $(pipenv --venv)/bin/activate
sleep 2
echo "${green}>>> Running server (Project_m_n_e_service Server) ${reset}"
gunicorn project_m_n_e.wsgi
