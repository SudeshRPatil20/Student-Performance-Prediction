# here we will give all the thing require to set an envirement to create an project of ml like pipeling to deploy 
# in simple word it will create your python folder in such that it will be deployed 

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path)->List[str]:
    '''
    this function will return the list of requirements
    '''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    

setup(
    name="mlproject",
    version="0.0.1",
    author="Sudesh",
    author_email="Sudeshrpatil201@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)