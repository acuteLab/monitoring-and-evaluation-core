#!/usr/bin/python
cd authentication_service
pipenv shell
pipenv install -r requirements.txt
python -m uvicorn main:app --reload
wait