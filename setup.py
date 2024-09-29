from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        'flask',  # Add other dependencies here
        'ibm-watson',
    ],
    author="Your Name",
    description="An emotion detection application using Watson NLP"
)
