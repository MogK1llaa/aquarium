#!/bin/bash
gunicorn3 --threads 5 --workers 1 --bind 192.168.1.83:5000 -m 007 wsgi:app
