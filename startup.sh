#!/bin/bash

exec gunicorn -k eventlet -w 1 --bind 0.0.0.0:5000 app:app
