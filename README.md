# Raspberry Pi APIs

APIs that make your RaspberryPi do cool things.

## Setup

```
python3 -m pip install pipenv
git clone git@github.com:Smotko/RaspberryAPI.git && cd RaspberyAPI/
pipenv install
pipenv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## Speach API

Make your RaspberryPI speak to you!

### Setup

```
sudo apt-get install espeak
sudo raspi-config  # Use this command to configure the Audio output (either AUX or HDMI)
aplay /usr/share/sounds/alsa/*  # To make sure your Audio output is working
```