from setuptools import setup

install_requires = [
    "requests",
    "python-dotenv"
]

packages = [
    'python-line-notify'
]

setup(
    name='python-line-notify',
    version='1.0.0',
    packages=packages,
    install_requires=install_requires,
    author="Broccolingual",
    author_email="broccolingual@gmail.com",
    url="https://github.com/broccolingual/python-line-notify",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)