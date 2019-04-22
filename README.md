# Sprint 1 Design Document
Zephyr semester project

## Deployment Environment 
The project is hosted on an EC2 server and can be accessed by the user on an internet connected device. A Raspberry PI controls the system and the hardware associated with it including motion sensors, lights, and a camera. 

## Functional Requirements

### Adjust Lights
1. The system should control attributes of the lights remotely via user input.
2. The system must update to manual actions done by the user.
3. The system should know what attributes of the lights can be changed.
4. The system should restrict users from lights based off privilege.

### Front Door Camera
1. The sensor must detect movement.
2. The camera must take a photo of visitor.
3. The database must be updated to have accurate information of the system's status.
4. The users are notified of an event.
5. The users can check the status and view the photo taken by the camera.
6. The user can view a live stream of outside their front door.

### Television Time Restriction
1. The Zephyr system should login users before use.
2. The Zephyr system should log the shows watched.
3. The Zephry system should log the amount of time each show is watched.
4. The Zephry system should handle ending the session gracefully.

## Database Design

### Full System 
ERD - https://drive.google.com/file/d/1E9FZYTcrmXXyHGFVdGMhGa6XWK0NyF9V/view?usp=sharing

### Front Door Camera
ERD - https://drive.google.com/file/d/1D54ridRq3nqnebNRgT4SLS5RFa8G-JrE/view

### Lights Controller
ERD - https://drive.google.com/file/d/1chGReG3twRqIuH7UxfmMHUwRtvx66AjE/view?usp=sharing

### Television Time Restriction
ERD - https://drive.google.com/file/d/1m5J6BBzVJmYVEjZuhqa1mVOAtMoAqAtq/view?usp=sharing

## Files

### Stub Files

### User Interface Files

#### Front Door UI 
1. A container with the current status of the front door and a thumbnail of the outside view.
2. A table holding previous records that include a timestamp of an event and the corresponding photo taken at the time.

#### Light Control UI
1. Selection menu of the rooms with light connected to the system.
2. When a light is selected options useable by the light will show up to edit.
3. A confirmation window will pop up after the change is sent with either a sucess or error message.

#### Television Time Restriction
1. Login screen for admin (Similar sign up screen)
2. A screen with all connected devices, and all devices trying to pair with the system. 
3. After selecting a device, you can select accounts on the televisions to pull up the restriction page
4. The restrictions page will have different fields that will allow the admin to create different types of rules

### Model Files

#### Front Door Model
1. Photo: A photo is taken and saved along the time it was taken.
2. Status: The status of the front door is recorded and updated for every event.

#### Light Control Model
1. Form layout with the information used to edit the light.
2. current status information of the lights will be stored so the user can see what the current state is before changing.
3. The privilege attached to the account will be checked with before editing the light so an unauthorized user can't change lights they aren't allowed to manipulate.

#### Television Time Restriction
1. Account - Used to keep track of different users and privilege
2. Restriction - Tied weakly to the Accounts they are applied to
3. Television - Tv name and id that are connected to the Zephyr system, so that different restrictions can be put on different devices
4. Show - This model is used by the restrictions for content monitoring (I.e R rated movies not allowed for 12 year olds)

### Controller Files

#### Front Door Controller
1. Sensor functions
* movement_listen(): the system activates actively listens for movement, which triggers the next function.
* activate_camera(): the system proceeds to activate the camera.

2. Camera functions
* sensor_listen(): the camera is only active if the sensor has been activated.
* take_photo(): a photo is taken and saved into the database.
* sleep(): the camera sleeps after a certain amount of time after there is no longer movement detected until awoken again.

3. App functions
* stream_surveillance(): opens a connection between the camera and app to allow the user to see outside the front door.

#### Light Control Controller
1. Edit Functions
* editLight(): The system will apply the recieved for info from the user to the selected light.
* changeColor(): Edits the RGB vaule of the light.
* changeBrightness(): Edits the brightness of the light.
* changeState(): Turns the light on/off.
* editPrivilege(): Lets an Admin change the access to the light.

2. Check Functions
* checkLight(): Gets the current status of the light to update to the server.
* checkColor(): Grabs the RGB vaule of the light.
* checkBrightness(): Grabs the brightness of the light.
* checkState(): Checks if the light is on/off.
* checkPrivilege(): Will check who has access to changing the light.

3. Update Functions
* updateLight(): Will update the status of the light everytime it is changed (Both with app and manually).
* listenLight(): Will check if the light is turned off manually.
* serverConnect(): Will connect the update function to the server to send the values.

4. Error Functions
* failError(): Loads the error message if the edit fails.
* success(): Loads the success message when the light changes successfully.

#### Television Time Restriction
1. Admin Methods
* createAccount(): Creates an account for a userName password etc. This will allow users to login and use the television(s)
* createRestriction(): Creates a restriction that can be reused and applied to multiple accounts
* editAccount(): allows for changing of passwords, permissions, and restrictions.
* editRestriction(): also accessable from the edit account view, used to update fields of the restriction
* viewUsage(): shows analytics of users and the content that were viewing, times of day etc.

2. User Methods
* login(): logs the usres into the account
* changePassword(): if permissions allow, let users change the password for their account

3. Television Methods
* userDidLogin(): starts tracking the data of the user
* userDidLogout(): stops tracking the data of the user
* notifyUser(): if a violation occurs or a time limit is getting reached the zephry system will show the message
* goHome(): if a violation occurs then the television will go back to the home screen 

### Languages

1. Python
* Python is the main language used for this project. Python is used to access the database server and controlling a hardware device.
2. Skill gaps
* Jon: no experience coding in Python
* Everyone: no experience connecting to devices with Bluetooth and hardware in general
* Zach: experience with cmake files and in general larger scale low-level development
* Issue will be integrating and bridging with c code when necessary
3. Django 
* Not a language, but we will use this to for DB and model template

# Sprint 2

## Sprint 1 Issues

Many ideas were created during Spring 1 of this project. Our group developed three use cases for the Home Automation Zephyr Project: TV Time Restriction, Front Door Monitoring, and Lights Adjustment.  Our first "pass" from the previous sprint involved a Django server to host the databases required but the scope proved to be too big as we are limited by the time remaining to implement all of our use cases given we do not have experience with hardware and coding in Python. We ultimately decided to implement the Lights Adjustment use case for this Sprint.

The next objective therefore is to create a simple application that changes the confirguration of a light, accessible from any browser. Our options included emulating the system in a web application by using the *states* a light can take and displaying the output of what the room might look like. The other is to use a Raspberry PI and relay switch to control a light remotely.

## Light Configuration

For our light configuration we are going to be using _blank_. This model will allow us to use *flask* on a *raspberry pi* to communicate with the light. We will still be able to use our python stubed out from our old plan for most of the use case. But after that, setups for testing will be minimal as we will have the connection hosted through a server so the users only have to visit the website.

### Hardware Components

To achieve our goal, a relay is used to connect the Raspberry PI and the light. It acts as a switch and could be toggled simply by running the commands:

```python
#on
GPIO.output (relay_pin, GPIO.LOW)
#off
GPIO.output (relay_pin, GPIO.HIGH)
```

* Raspberry Pi
* Relay
* Lights

### Necessary libraries

The GPIO channels must set up and used by the relays

```
sudo apt-get install python-rpi.gpio
```

### Virtual environment

Everything is created in a Python virtual environment to keep everything separated

```sh
sudo apt-get install python-virtualenv
mkdir lightsApp
cd lightsApp

#activate the virtual environment
virtualenv lightsEnv
lightsEnv/bin/activate

#install required library on virtual environment
pip install flask uwsgi rpi.gpio
```

### Functionality

This code sets up the relay connections and listens for commands. 

```python
#WIP - need to work on code for turning on lights

from flask import Flask, render_template
import RPi.GPIO as GPIO
 
app = Flask(__name__)
 
#pin connected to relay
#pin state

#GPIO set up
 
#default route, without anything
# set routes for actions: on and off
	
# return to the template with new info
```

### Front-end

Flask handles the front-end of the application. Currently working on code


```
mkdir templates
cd templates
```
lightsApp.html
```html
#WIP - work on html
#button to turn on
#button to turn off
#etc
```

```css
//WIP - work on css code to make it pretty
//maybe jquery
```
