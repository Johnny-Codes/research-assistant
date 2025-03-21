To run with remote database: `export USE_REMOTE_DB=True && python manage.py runserver`

gunicorn research.wsgi:application --bind 0.0.0.0:8000

tmux:
start new session `tmux new -s django_server'

run django server:
cd into folder and activate venv

run gunicorn

detach from tmux `ctrl + B` then press `D`

reattach:
tmux attach -t django_server
