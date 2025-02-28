#!/bin/bash

# Navigate to the backend directory (change path as needed)
cd /home/sandeep/Documents/classroom-backend || exit

# Activate virtual environment (if using one)
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Set environment variables
export FLASK_APP=app.py  # Change this if your main file has a different name
export FLASK_ENV=production  # Set 'production' for deployment
export SECRET_KEY="SocketsBackendFlask"

# Run Gunicorn with Eventlet for better concurrency
echo "Starting Flask-SocketIO server with Gunicorn + Eventlet..."
gunicorn -k eventlet -w 1 -b 0.0.0.0:5000 app:app

# Keep the script running
exec "$@"
