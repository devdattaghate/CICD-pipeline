# goldpriceprediction-CICD-pipeline
This my first individual end to end project for complete ML-CICD pipeline

Problem definition:
    Objective: Predict the price of gold based on historical data and other relevant features.

    Deliverables: 
        A predictive model for gold prices.
        A user interface for predictions.

Data Collection:



Softwares and accounts Requirements:

    1.[Github account]: (https://github.com)
    2.[Heroku account]: (https://id.heroku.com/login) 
    3.[VS code IDE]: (https://code.visualstudio.com/download)
    4.[Git cli]: (https://git-scm.com/downloads)
    5.[GIT Documentation]: (https://git-scm.com/docs/gittutorial)

Git commands:

STEP1 : creating conda environment

'''conda --version'''

'''conda create -p venv python==3.9 -y'''

'''conda activate venv/'''

'''pip install -r requirements.txt'''

To add files to git 
'''git add.'''

OR

'''git add <file name>'''

> NOTE: To ignore file or folder from git we can write name of file/folder in .gitignore file'''

To check git status
'''git status'''

To check all version maintaned by git
'''git log'''

To create version/commit all changes by git 

'''git commit -m "message" '''

To send version/ changes to github

'''git push origin main'''

To check remote URL
'''git remote -v'''

STEP2: create Flask app & run

To set CI/CD pipeline in heroku we need 3 information

1.HEROKU_EMAIL = herokudev91@gmail.com
2.HEROKU_API_KEY = <>
3.HEROKU_APP_NAME = goldpriceprediction

STEP3: BUILD DOCKER IMAGE
'''
docker build -t <image_name> : <tag_name> .
'''
> NOTE: Image name for docker must be in lowercase & you required fast internet connection to build image. 
> NOTE: Also make sure to open docker dekstop, so docker is up & running

To list docker image
'''
docker images
'''

Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 <IMAGE ID>
'''

To check running container in docker 
'''
docker ps
'''

To stop docker container
'''
docker stop <container id>
'''
STEP4: creat .github\workflows\ main.yaml file and write workflow info for deploy to heroku  

STEP5: add secrets to git hub\setting\secrets\actions\ add secrets like heroku mail, api_key, app_name

Troubleshooting while deployment 
"""
Heroku app is not set to use a Docker-based deployment. Instead, it is currently on Heroku-24, which is a standard buildpack-based stack. Since you're trying to deploy a Docker container, you need to switch the stack to a container-based environment.

Solution: Switch to a Container Stack

Run the following command:

heroku stack:set container -a <app-name>
"""


