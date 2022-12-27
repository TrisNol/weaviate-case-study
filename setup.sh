python -m venv ./venv
./venv/Scripts/activate
pip install -r requirements.txt

docker-compose up -d
python -m app.main