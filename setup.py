from setuptools import setup, find_packages
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements.txt file and returns the list of requirements
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author= 'Ajeet',
    author_email= 'ajeet@arizona.edu',
    packages=find_packages(),  # this will automatically find all the packages in the project directory and include them
    # it(find_packages) will look for __init__.py files in the directories to identify packages and build them accordingly.
   
    # Install_requires=['pandas', 'numpy','seaborn']  lib names are taken from the requirements.txt file
    Install_requires=get_requirements('requirements.txt')

)