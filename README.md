# python_online
Executor of python code in browser using Flask framework

How to run project with Docker:
-------------------------------------------
* Download and install [Docker](https://www.docker.com/)
* Download project:
```
docker pull aleksejsamarin/python_online
```
* Run project:
```
docker run -d -p <your_ip>:<your_port>:5000 aleksejsamarin/python_online
```

How to run project without Docker:
-------------------------------------------
* Download and install [Python](https://www.python.org/downloads/), [Git](https://git-scm.com/download/).
* Download project:
```
mkdir directory
cd directory
git clone https://github.com/AleksejSamarin/python_online.git .
```
* Install requirements:
```
pip3 install -r requirements.txt --user
```
* Run project:
```
python flaskr/main.py
```

Program usage example:
-------------------------------------------
![Image](https://github.com/AleksejSamarin/python_online/blob/master/task/result.png)
