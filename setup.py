from setuptools import setup

install_requires = [
    "requests==2.25.1",
    "python-dotenv==0.15.0"
]

packages = [
    'python-line-notify'
]

setup(
    name='python_line_notify',
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