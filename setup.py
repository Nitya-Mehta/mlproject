from setuptools import find_packages, setup
from typing import List

# This function returns the list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements] #As we readlines() it also gives \n so here we are just replacing it with ""
        
        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements

setup(
    name = 'mlproject',
    version='0.0.0.1',
    author='Nitya',
    author_email='nityachintan@gmail.com',
    packages=find_packages(), #Goes inside the src folder finds the __init__.py file to run
    install_requires=get_requirements('requirements.txt')
)