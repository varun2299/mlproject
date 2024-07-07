from setuptools import find_packages, setup

def get_requirements(file_path):

    req = []
    with open(file_path) as file:
        req = file.readlines()
        req = [x.replace("\n","") for x in req]

        if '-e .' in req:
            req.remove('-e .')
    return req

setup(

name = 'mlproject',
version = '0.0.1',
author = 'varun',
author_email = 'varunpandey133@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)