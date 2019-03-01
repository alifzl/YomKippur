# Yom Kippur
----
[Yom Kippur](https://en.wikipedia.org/wiki/Yom_Kippur) is a WhatsApp automation tool which aims to be a consistent and permanent solution for non-commercial usage of WhatsApp as an automated bot. 

### What does it do?
----
  - Send/Recieve Single Message in a pre-configured WhatsApp application in the AVD (Android Virtual Device)
  - create contact-list in AVD and use it for the Sending/ Receiving stuff
  - literally it can do everything with AVD (it create a numerous possibilities to persuade)



### Motivations
----
At the very first, I saw [yowsup](https://github.com/tgalal/yowsup) my only choice, but due to the issues listed below I changed my mind in order to implement it in another way.
  - Variety of community issues (linked [here](https://github.com/tgalal/yowsup/issues))
  - Yosup is asynchronous kind of API which interacts with WhatsApp RestAPI, regarding the high-security considerations of WhatsApp, it came very sensitive about the present active sessions of every user and it will be not very friendly with synchronous solutions. (as you probably know the restrictions of using web-view of the WhatsApp which says that we should have a consistent active internet connection in the phone simultaneously)
  - the laziness of mine and also challenging myself to do it in the hard way

### Installation Pre-Requirements
----
Well, Dependencies in this project, they are rather a lot!
First of you should have this requiremnts satisfied:</br>
Windows Installers are refrenced, but it can be implment in linux or MacOS machine (both of them not tested)
| Dependency | Description / Download Links |
| ------ | ------ |
| Android Studio | [Android Studio with Android API 28](https://developer.android.com/studio) |
| MySQL | [Mysql Installer community 8.X or above](https://dev.mysql.com/downloads/installer/) |
| Python 2.7 | [Python 2.7](https://www.python.org/downloads/) |
| Appium | [V1.10 or above](http://appium.io/downloads.html) |
| RabbitMQ | [Latest version of RabbitMQ](https://www.rabbitmq.com/) |
| Postman | [Latest version of Postman](https://www.getpostman.com/downloads/) |





### Development and Contribute?
----
Want to contribute? Great!
Feel free to knock me up at a.fazeli95[at]gmail[dot]com or just create a pull request.



### DoMe
----

### License
----

All of the components used in this project is Open-Source and have MIT License and it can be used in any non-commersial product