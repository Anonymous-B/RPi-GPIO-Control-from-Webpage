
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   0: {'name' : 'GPIO 0', 'state' : GPIO.LOW},
   1: {'name' : 'GPIO 1', 'state' : GPIO.LOW},
   2: {'name' : 'GPIO 2', 'state' : GPIO.LOW},
   3: {'name' : 'GPIO 3', 'state' : GPIO.LOW}, 
   4: {'name' : 'GPIO 4', 'state' : GPIO.LOW},
   5: {'name' : 'GPIO 5', 'state' : GPIO.LOW},
   6: {'name' : 'GPIO 6', 'state' : GPIO.LOW},
   7: {'name' : 'GPIO 7', 'state' : GPIO.LOW},
   8: {'name' : 'GPIO 8', 'state' : GPIO.LOW},
   9: {'name' : 'GPIO 9', 'state' : GPIO.LOW},
   10: {'name' : 'GPIO 10', 'state' : GPIO.LOW},
   11: {'name' : 'GPIO 11', 'state' : GPIO.LOW},
   12: {'name' : 'GPIO 12', 'state' : GPIO.LOW},
   13: {'name' : 'GPIO 13', 'state' : GPIO.LOW},
   14: {'name' : 'GPIO 14', 'state' : GPIO.LOW},
   15: {'name' : 'GPIO 15', 'state' : GPIO.LOW},
   16: {'name' : 'GPIO 16', 'state' : GPIO.LOW},
   17: {'name' : 'GPIO 17', 'state' : GPIO.LOW},
   18 : {'name' : 'GPIO 18', 'state' : GPIO.LOW},
   19: {'name' : 'GPIO 19', 'state' : GPIO.LOW},
   20: {'name' : 'GPIO 20', 'state' : GPIO.LOW},
   21: {'name' : 'GPIO 21', 'state' : GPIO.LOW},
   22: {'name' : 'GPIO 22', 'state' : GPIO.LOW},
   23: {'name' : 'GPIO 23', 'state' : GPIO.LOW},
   24: {'name' : 'GPIO 24', 'state' : GPIO.LOW},
   25: {'name' : 'GPIO 25', 'state' : GPIO.LOW},
   26: {'name' : 'GPIO 26', 'state' : GPIO.LOW},
   27: {'name' : 'GPIO 27', 'state' : GPIO.LOW},
   
   
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
   
