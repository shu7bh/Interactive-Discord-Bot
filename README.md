# Discord-Bot
A mini-project to create a discord bot with multiple functionalities

## Features ##
Currently it has 3 different types of features:
* Entertainment
* Identification
* Admin

### Entertainment ###
There are two features currently:
* ping: Getting to know the latency of the bot in responding to your message
* 8ball: Employed wizardry to correctly answer all the dumb questions asked
* joke: Tells a random text joke using an API.
* random: Returns a random number between 2 integers

### Identification ###
For a large server, in which people have vague usernames, this functionality comes in handy.
People can identify themselves using this bot, and any person can find out using their tag what their name is... no more awkward questions every 2 months!

### Admin ###
Some special permissions are needed for this function to work.
* clear: Deletes the messages in a particular channel. There is one parameter, the number of messages to be deleted
* ban: Bans a user from the server. The parameter to be given is the tag of the user.
* unban: Unbans a user from the server. The name and discriminator id must be specified as the parameter (username#1234).
* kick: Kicks a user from the server. The parameter to be given is the tag of the user.

The only feature currently here is to clear messages in a bulk.
The bot needs manage_messages permission to be able to run this.

### Future Features ###
Any and every feature can be added over here. This bot is a ideally supposed to be one bot fit alls. Just started working on this in my free time for learning purposes.


## Pre Requisites ## 
Create a python virtual env in the main directory using
```
$ python3 -m venv env && cd env
$ source bin/activate
$ pip install -r ../requirements.txt
```

To run this bot in your server, do the following:
* Create a file named token.txt in the same directory as that of the bot.py
* In this file, add your discord bot token.

## Run The Bot ##

You have to run the bot.py in your machine.
After you have gone through the prerequisites, you can now run this bot

To run this type the following in the command line in the cloned directory `$python3 bot.py`
If no errors have occured, the bot should start functioning

To run this file in your terminal in the background do the following:
```
$python3 bot.py &
```

To keep this file running even after you close your terminal, do the following:
```
$nohup python3 bot.py > Log/log.out 2> Log/log.err &
```

To kill this program, you have to first identify the pid of your program.
To do this, type `$pidof python3 bot.py`

The first number `<pid>` is generally the one that has to be killed by you to stop the execution of the program.

Kill it using the folliwng command: `kill <pid>`

Here `log.out` will contain the stdout while `log.err` will contain the error messages received by the bot

## Add the Bot on your server ###

* To do this, go to your discord applications, OAuth2 tab.
* Click on the option bot from the set of options available.
* Next click on the permissions you want to give it.
* Copy the generated url.
* Paste this url on a browser.
* Select the server in which you want to deploy it.

Voila! You have added this bot in your server. Have fun!
