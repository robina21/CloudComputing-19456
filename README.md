Read me for Build a Dockerfile, Image, and Container



APP FOLDER contains the following:

Make these two microservices work together (Optional).
 
the client.py file has the both the services working together.
The city names gets converted to zip code and then converted to weather.

From the browser pass the city name and it will output the weather on the UI


Screen shots for weather client file has the following:

Screen of the docker file output, image output, container output and the browser outputs.

Build a Dockerfile, Image, and Container
Getting Started
These instructions will help to Build a Docker file, an image and a container to run a python script on the web server
Prerequisites
•	Docker
•	Libraries: Requests, uszipcode 


Build the Image:

```docker build -t request-client .```

 
[![Picture1.png](https://i.postimg.cc/BvzVdTvX/Picture1.png)](https://postimg.cc/WDM8ZJgv)

Run The Container:

```docker run -p 8000:8000 request-client```

[![P2.png](https://i.postimg.cc/kG7MbPdr/P2.png)](https://postimg.cc/5YkWhG0p)


