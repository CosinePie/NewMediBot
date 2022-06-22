# Medi-bot
How to Get the Bot running by Using the Github Code
Firstly clone the repo locally or Download the source code.

After getting the source code you need to install python and rasa on to your system. Our recommendation is to download python using miniconda or Anaconda.

Link for miniconda: https://docs.conda.io/en/latest/miniconda.html

Link for Anaconda: https://www.anaconda.com/products/individual

After installing the python, it is recommended to create a separate environment for RASA and install the required libraries into it.( Sometimes the libraries versions may differ for differnet packeges which might cause some dependency issues while using rasa )

## Command to create a new Env.

conda create -n <Name of Environment> python=3.7

conda create -n Medi-bot python=3.7

Once the environment is created you can activate it using

conda activte <name of environment>

conda activate rasa (our enviornment name)

After activating the environment you can install rasa by using

> python -m pip install --upgrade pip  # to upgrade the pip version
> pip install rasa == 3.0.6
To check that rasa is working or not you can run the below command

rasa --version

** note if you get some error related to sanic you can run the below command to resolve it

pip install sanic==21.9.3

Now you are ready with all the required dependencies. Let's now see how you can train the model.

To train model
you can train your model using below command

rasa train

To talk to bot in shell we need to run following two commands in parallel
> rasa shell
> rasa run actions
rasa shell will provide us with a command line prompt using which we can have conversation with the bot.

To see bot working locally with UI
we need first run the following to commands in parallel.

> rasa run -m models --enable-api --cors "*" 
> rasa run actions
After running the above commands. The next step is to open the webpage.html file in browser.(webpage.html file is present with the source code)

Note - If Got an error like "you must install a WebSocket server that is compatible with your async mode to enable it."
> pip install gevent-websocket
> pip install eventlet
Note - If issue still persists
> pip install sanic==21.6.0
> pip install Sanic-Cors==1.0.0
> pip install sanic-routing==0.7.0
## Phases
We divided our chatbot in two phases.

### Phase 1

In the first phase, we make an assumption that the user already knows the disease name which he/she has been diagnosed with, and wants to gain more information about the disease. Then he/she asks the question about the disease description , causes and prevention methods

<p style="text-align:center;"><figure><img src=images/img8.png alt="Logo" width = "55%" length = "60%"><figcaption><b> Fig Phase 1</b> </figcaption></figure></p>

### Phase 2

In Second phase, chatbot  asks the user what are symptoms of the disease you are facing and after entering the disease symptoms, it will give the disease name and more symptoms that you can face with that disease. By this you get to know that you are also facing that symptoms after reading the chatbot answer. And now you are more sure that you have that particular disease.

<p style="text-align:center;"><figure><img src=images/img9.png alt="Logo" width = "55%" length = "60%"><figcaption><b> Fig Phase 2</b> </figcaption></figure></p>

## Running the bot using Docker
First docker is required to be installed on the system to use it. It can be downloaded using the given link mentioned below.
> Link: https://docs.docker.com/engine/install/

Once docker is installed we need to create docker image of the project, it can be done using the below mentioned command.
> docker build -t \<Name for image> .

> docker build -t Medi-bot .

After creating image using the above command we can check it with the following command
> docker images

It will list out all available images on the system.

To start docker container with the image bulit in above step we can use below command.

> docker run -it -p 5005:5005 \<name of image to run>

> docker run -it  -p 5005:5005 Medi-bot

If it gives an error port 5005 already in use, their are two things that we can do
1. check if some other container is already running with the same port number and stop it
    - To see list of running container we can use
    > docker ps
    - after seeing which container is running already we can stop it using
    > docker stop \<contaner id>
2. We can change link differnet port number with the docker container and update the same port number in the webpage.html file. ( *socketUrl* : [ localhost ]: [ port-number ] )
    > docker run -it  -p [ port-number ]:5005 Medi-bot
    - This will map your localhost [ port-number ] to 5005 and that 5005 port is used by docker container

### Some Useful Commands Realted to Docker
- To list running containers
    > docker ps
- To list all containers(running and stoped both)
    > docker ps -a
- To stop Docker container
    > docker stop \<container-id>
- To see available Images
    > docker images
- To remove a docker image
    > docker image rm -f \<image name>

## Pipeline of our chatbot :-
<p style="text-align:center;"><figure><img src=images/pipeline.png alt="Logo" width = "80%" length = "70%"><figcaption><b> Pipeline of our Chatbot</b> </figcaption></figure></p> 

1. First we started by removing the duplicate rows from the dataset so that there is one unique row for every disease present.

2. Then we performed exploratory data analysis on the dataset to gather more information about the data and try to visualize the data to gain useful insights present in the dataset.

3. In the third step we defined intents based on the disease names and started making example queries which the user may ask to the chatbot.

4. After making questions, we made utterances for the diseases which the bot uses to answer the user's queries.

5. Then we generated the nlu and the domain file and added them to the data folder on which the bot has to be trained.

6. Then we made a custom action file so as to take in symptoms as the user input and accordingly predict the disease the user might have.

7. Then the model is trained on the data generated.

8. After training we tested the model.

9. Then we deployed the model on Telegram and WhatsApp.


## Social media Integration
Social media integration is the process by which we can connect our  social media followers to our website and make this platform available to our customers or followers by our website. so for now we connect our chatbot to:-
1. Whatsapp
2. Telegram

### Whatsapp bot :-
It is very easy to build a whatsapp chatbot using twilio API for Whatsapp. Firstly, we created a twilio account. Twilio provides a WhatsApp sandbox where we can easily develop and test our application. we can connect our phone to whatsapp by selecting messaging and then in messaging by clicking send whatsapp message in try it out option. The whatsapp sandbox page shows us a whatsapp number and code for it.

<p style="text-align:center;"><figure><img src=images/img1.png alt="Logo" width = "90%" length = "60%"><figcaption><b> Fig  Twilio Sandbox for whatsapp</b> </figcaption></figure></p> 


Now we can send message on given number from our whatsapp. The message we send is the code given. Then after sending this code we receive a message from twilio that shows our whatsapp is connected to the sandbox. Then we configure our sandbox by adding webhook URL then we see URL like this 
> https://<host>:<port>/webhooks/twilio/webhook 

And in this we replaced the host and port with the appropriate values from your running Rasa X or Rasa Open Source server.

<p style="text-align:center;"><figure><img src=images/img2.png alt="Logo" width = "95%" length = "60%"><figcaption><b> Fig Twilio Configuration</b> </figcaption></figure></p>


Then After getting credential from Twilio we add those credentials in credentials.yml. We add the Account SID, Auth Token, and the phone number in our credentials.yml file. 

<p style="text-align:center;"><figure><img src=images/img3.png alt="Logo" width = "75%" length = "60%"><figcaption><b> Fig  Twilio Sandbox for whatsapp</b> </figcaption></figure></p>


Then we deploy our chatbot in whatsapp by using command 
> rasa run -m models –enable-api –cors “*” 


After this we run the actions command 
> rasa run actions 

After running the action command we ask a question from the whatsapp bot. Now the picture below we attached is a screenshot of our whatsapp chatbot.

<p style="text-align:center;"><figure><img src=images/img4.jpg alt="Logo" width = "55%" length = "60%"><figcaption><b> Fig Whatsapp Chatbot</b> </figcaption></figure></p>


Now as the multiple users connect we can see  the user id’s as their number

<p style="text-align:center;"><figure><img src=images/multipleusers.png alt="Logo" width = "55%" length = "60%"><figcaption><b> Fig Multiple Users</b> </figcaption></figure></p>


Basically we integrated our chatbot with whatsapp. We used a conversation tool called twilio which provides us with a powerful API through which we connect our chatbot to whatsapp. Ngrok was used to give twilio the access to the port where the chatbot server was running. After this the credentials file was modified to integrate the bot. Finally testing on WhatsApp was done by us.

### Telegram bot :- 
Firstly we have to get API for our bot so for that we have to send a message to bot father /new bot then it asks name and username for our bot. Then after this we get a message as it contains our token to access HTTP API

<p style="text-align:center;"><figure><img src=images/botfather.png alt="Logo" width = "55%" length = "60%"><figcaption><b> Fig Telegram BotFather</b> </figcaption></figure></p>


Ngrok was used to give telegram access to the port where the chatbot server was running. Then we write all the credentials in credentials.yml

<p style="text-align:center;"><figure><img src=images/img6.png alt="Logo" width = "55%" length = "60%"><figcaption><b> Fig Credentials for Telegram</b> </figcaption></figure></p>


Then we deploy our chatbot by using command 
> rasa run -m models –enable-api –cors “*” –debug

After this we run the actions command 
> rasa run actions 

After running the action command we ask a question from the telegram bot.

<p style="text-align:center;"><figure><img src=images/img7.jpg alt="Logo" width = "55%" length = "60%"><figcaption><b> Fig Telegram Bot</b> </figcaption></figure></p>
