# Yom Kippur
[Yom Kippur](https://en.wikipedia.org/wiki/Yom_Kippur) is a WhatsApp automation tool which aims to be a consistent and permanent solution for non-commercial usage of WhatsApp as an automated bot. 

### What does it do?
----
  - Send/Recieve Single Message in a pre-configured WhatsApp application in the AVD (Android Virtual Device)
  - create contact-list in AVD and use it for the Sending/Receiving stuff
  - literally it can do everything with AVD (it create a numerous possibilities to persuade)



### Motivations
----
At the very first, I saw [yowsup](https://github.com/tgalal/yowsup) my only choice, but due to the issues listed below I changed my mind in order to implement it in another way:
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
| JAVA | [Java JDK 11](https://www.oracle.com/technetwork/java/javase/downloads/index.html) |
| MySQL | [Mysql Installer community 8.X or above](https://dev.mysql.com/downloads/installer/) |
| Python 2.7 | [Python 2.7](https://www.python.org/downloads/) |
| Appium | [V1.10 or above](http://appium.io/downloads.html) |
| RabbitMQ | [Latest version of RabbitMQ](https://www.rabbitmq.com/) |
| Postman | [Latest version of Postman](https://www.getpostman.com/downloads/) |

**Considerations:**
 you can use conda virenv for the python 2.7, but it drived me a serious headache (Not Recommended)</br>
 main reason which I used python 2 for this project is that Appium, MySQL connector client and RabbitMQ were incompatibile together in version 3.


### Configuration

First of all, be patient in this part. it took me blood and tears to wipe the dependency shits for doing this such a simple task.</br>

**1.Android Virtual Device** </br>
luanch AVD Manager of Android Studio, setup an device with android 9.0 with API 28 (pick and appropriate name for the AVD because we need it in further steps). </br>
notice that you should install WhatsApp through the AVD itself, so select the PlayStore supported version.</br>
check you have this environment variables in your account:


| Variable Name | Variable Value |
| ------ | ------ |
| ANDROID_HOME | C:\Users\FZL\AppData\Local\Android\Sdk |
| JAVA_HOME | C:\Program Files\Java\jdk-11.0.2 |
| PYTHONPATH | C:\Python27;C:\Python27\Lib\site-packages;C:\Python27\Lib;C:\Python27\DLLs;C:\Python27\Scripts |
| Patch | C:\Python27;C:\Python27\Scripts;C:\Python27\Lib\site-packages;C:\Program Files\Java\jdk-11.0.2;C:\Program Files\Java\jdk-11.0.2\bin; |

then you should start your AVD, install WhatsApp in that, and also authorize the ADB with your device (mandatory) </br> to do that you should execute  `adb devices` or `adb usb` in order to check the autorization of the AVD.

```sh
C:\Users\FZL\AppData\Local\Android\Sdk\platform-tools: adb devices
List of devices attached
emulator-5554   device
```
</br> if you are seeing the unauthorized result, you should follow this [link](https://stackoverflow.com/questions/23081263/adb-android-device-unauthorized).

**2.RabbitMQ Configuration** </br>

after installiztion of RaabitMQ, you should run `rabbitmq-plugins enable rabbitmq_management ` in the RabbitMQ sbin directory in order to enable the Web-GUI of the RabbitMQ management sytem. restrating the RabbitMQ service may be needed.</br> 
after this you should be able to access the RabbitMQ Web-GUI with `http://localhost:15672/#/` address in your local machine. if yes, create a new user by the below commands and make it administartor:

```sh
rabbitmqctl add_user username password
# This makes the user a administrator
rabbitmqctl set_user_tags username administrator
# This sets permissions for the user
rabbitmqctl set_permissions -p / username ".*" ".*" ".*"
```
login with newly created credentials and import the queue specifications which is already attached in this Repo which called `RabbitMQ_Conf.json` in the Import definitions sections under the overview menue.</br>
it would create the necessary configurations for the RabbitMQ and enables the needed privilages. 

**3.Appium** </br>
Just run the Appium server with the default settings. `appium --default-capabilities '{"noReset": "True"}'` is already embeded in code. TL;DR: there is no thing to do in this step.

**4.MySQL** </br>
Install the community edition of the MySQL, create an appropriate DB account and set the service run automatically when OS starts.

**5.Install the python dependencies** </br>
Simply run `pip install –r dependencies.txt` in order to resolve the dependency of used libraries.</br>
You may face deprecated version of `MySQLdb` library which is solvable with installing [this]( https://pypi.org/project/MySQL-python/) and [this]( https://dev.mysql.com/downloads/connector/python/). Take care of installing the python 2.x version of mentioned libraries.

**6.Create directories for the log files** </br>
Create the directories and files as it’s mentioned below:
```sh
# directories
C:\var\log [directory]
C:\var\log\whatsapp_api [directory]
# log files
C:\var\log\api.log
C:\var\log\whatsapp_single_consumer.log
C:\var\log\whatsapp_single_worker.log
C:\var\log\
```

**7.Set the Yom Kippur’s configuration file** </br>
Go to `YomKippur-master\configs\config.cfg` and input the following.</br> 
(don't change anything esle unless you know what are you doing)
```sh
[mysql]
host=127.0.0.1
username='your MySQL username'
password='your MySQL password'
database=Whatsapp

[rabbitmq]
ip=127.0.0.1
ipqueuename=ipaddr.queue
username='your RabbitMQ username'      
password='your RabbitMQ password' 

[queue_name]
single_message=whatsapp_singlemessage_queue
broadcast_message=whatsapp_broadcastmessage_queue
add_contact=whatsapp_newcontact_listener_queue
listen_message=whatsapp_messagelistener_queue

```

Run the `main.py` and `add_new_contact_producer.py` in two separate terminal/CMD environment.</br> if you didn't see any error, you are good to go.


### Runnig
----
1. make sure MySQL server is running
2. make sure RabbitMQ sever is runnig
3. run Appium with defualt settings
3. run these scripts
```sh
python main.py
python add_new_contact_producer.py
python single_message_producer.py

```
4. run Postman and create desirable Post commands from the list below:

#### Adding contact in Google Contacts APP
URL : [http://127.0.0.1:5000/api/v0.1/add_new_contact](http://127.0.0.1:5000/api/v0.1/add_new_contact) </br>
TYPE : POST</br>
HEADERS : Content-Type:application/json</br>
BODY :</br>
{"mobile_number":"+98 XXXXX XXXXX","emulator_name":"pix"}</br>
RESPONSE :</br>
{ "corr_id": "767ae095-0066-49fb-b955-063286ceed1e", "message": "Singal received for Adding Contact", "status": "1" }</br>

#### Sending Single Message via Whatsapp
URL : [http://127.0.0.1:5000/api/v0.1/send_single_message](http://127.0.0.1:5000/api/v0.1/send_single_message)</br>
TYPE: POST</br>
HEADERS :</br>
Content-Type:application/json</br>
BODY :</br>
{"mobile_number":"+98 XXXXX XXXXX","emulator_name":"pix","message_body":"Salaaaaam!"}</br>
Response :</br>
{ "corr_id": "78f21f25-b781-4312-87e5-ebcd73e9b67e", "message": "Singal received for sending message", "status": "1" }</br>


### Development and Contribute?
----
Want to contribute? Great!
Feel free to knock me up at a.fazeli95[at]gmail[dot]com or just create a pull request.



### DoMe
----

### License
----

All of the components used in this project is Open-Source and have MIT License and it can be used in any non-commersial product