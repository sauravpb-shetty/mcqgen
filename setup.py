# from  setuptools  import find_packages,setup
# # from flask import Flask
# import pandas as pd 

# setup(
#     name='mcqgenrator',
#     version='0.0.1',
#     author='saurav shetty',
#     author_email='sauravds39@gmail.com',
#     install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
#     packages=find_packages()
# )
from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='saurav shetty',
    author_email='sauravds39@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)