from setuptools import setup
from typing import List

#Declaring variables for setup functions
PROJECT_NAME = "gold-price-predictor"
VERSION= "0.0.1"
AUTHOR = "Devdatta Ghate"
DISCRIPTION= "This is first individual end to end machine learning project"
PACKAGES= ["goldpriceprediction"]
REQUIREMENTS_FILE_NAME= "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return a list of requirement mentioned in requirements.txt file

    return: This function is going to return a list of requirement mentioned in requirements.txt file

    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name= PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    discription= DISCRIPTION,
    packages= PACKAGES,
    install_requires= get_requirements_list()
)
