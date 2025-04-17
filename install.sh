#!/bin/bash

echo "Starting NetSniff installation..."

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Installation completed."
echo "To start NetSniff:"
echo "source .venv/bin/activate && sudo python3 main.py"
