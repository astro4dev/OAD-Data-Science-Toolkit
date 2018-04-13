##############################################################################################
# Purpose   : Dockerize Components of a simple data science stack.
# Python    : 3.6
# Version   : 0.1
# Author    : Dr. Rob Lyon (robert.lyon@manchester.ac.uk)
##############################################################################################
#
# This docker file will setup an environment with only a basic data science stack.
#
##############################################################################################

# Use well supported Ubuntu distribution.
FROM ubuntu:18.04

# Contact me for help!
MAINTAINER robert.lyon@manchester.ac.uk


# The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT,
# COPY and ADD instructions that follow it in the Dockerfile. If the WORKDIR doesn’t
# exist, it will be created even if it’s not used in any subsequent Dockerfile instruction.
WORKDIR /home

#####################################################################
# Make required directories
#####################################################################

# Now create some diectories to store files and scripts
RUN mkdir soft
RUN mkdir workspace
RUN mkdir workspace/data

#####################################################################
# Install System tools needed
#####################################################################

RUN apt-get update \
  && apt-get install -y \
  wget \
  unzip \
  bzip2

#####################################################################
# Install Miniconda (python 3.6 version)
#####################################################################

# Change to the soft (aka software directory).
WORKDIR /home/soft

# Now install Miniconda to manage the python environment. This installs numpy, scipy, matplotlib,
# jupyter etc. Type conda list inside the built docker container, to view the python modules already
# installed.

RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /home/soft/anaconda
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH /home/soft/anaconda/bin:$PATH

#####################################################################
# Update Anaconda and install data science tools
#####################################################################

RUN conda update -n base conda

# Python packages from conda.
RUN conda install -y \
    numpy \
    scipy \
    matplotlib \
    scikit-learn

# Imbalanced learning library.
RUN conda install -c conda-forge certifi
RUN conda install -c conda-forge imbalanced-learn

#####################################################################
# Prepare data and workspace
#####################################################################

WORKDIR /home/workspace/data
RUN wget https://archive.ics.uci.edu/ml/machine-learning-databases/00372/HTRU2.zip
RUN unzip HTRU2.zip


RUN rm HTRU2.zip
RUN rm HTRU_2.arff
RUN rm Readme.txt
# IPython/Jupyter
EXPOSE 8888

#####################################################################
# Finally...
#####################################################################

# Define the command that will be exectuted when docker runs the container.
WORKDIR /home
ENTRYPOINT /bin/bash