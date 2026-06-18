import os

GIT_DIR = '.dgit'

def init():
    os.makedirs(GIT_DIR, exist_ok=True)