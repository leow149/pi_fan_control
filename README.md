# pi_fan_control

With this python script the speed of a 4-pin PWM fan is rising with the temperature of your raspi-CPU.

**!!!YOU HAVE TO CONNECT THE GROUND OF THE FAN TO A GROUND PIN OF YOUR PI TO GET THIS TO WORK!!!**

## Initialisation: 

- Connect the PWM pin of your fan to GPIO 12

- Connect the ground pin of your fan to a ground pin of your Pi

- `python3 -m pip -r requirements.txt`

- `python3 pi_fan_control.py`

- *Optional: Change `mintemp` and `maxtemp` in the python script to your needs. Below `mintemp` it will set the speed to slowest and above `maxtemp` it will set it to fastest.*
