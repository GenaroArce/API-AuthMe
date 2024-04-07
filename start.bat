@echo off
echo Installing dependencies...
pip install -r requirements.txt
echo Dependencies installed correctly.

echo Starting the API...
python api.py