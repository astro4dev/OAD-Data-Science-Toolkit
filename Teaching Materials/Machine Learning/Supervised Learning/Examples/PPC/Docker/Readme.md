# Docker File Info

## Author: Rob Lyon
## Email : robert.lyon@manchester.ac.uk
## web   : www.scienceguyrob.com

# Overview

I've provided a simple dockerfile you can use to build a environment that can be used to run the notebooks. All you have to do is move the resources you require into the notebook, and you should be good to go.

#### OS & Packages Installed

Image OS: Ubuntu 18.04
  
| Number |          Package            |
|--------|-----------------------------|
|1.      |  wget                       |
|2.      |  unzip                      |
|3.      |  bzip2                      |

#### Non-OS Software:
  
| Number |            Package            |
|--------|-------------------------------|
|1.      |  Miniconda                    |

#### Python Modules (Python 3.6):

A full scipy stack, numpy, matplotlib, jupyter notebooks, certifi, scikit-learn, imbalanced-learn.

### Docker Quick Start

Docker is a system that runs a virtualised software environment. You can, in simple terms, run an OS
within in OS (e.g. run a full Linux kernel on your Mac). Docker is cool, and below I share the
Docker commands I use most often. These will help you get started. For more detailed help please see,

[Docker guide](https://docs.docker.com/engine/getstarted/)

[Docker site](https://www.docker.com)

[Docker User guide](https://docs.docker.com/engine/userguide/)

[Docker command line reference](https://docs.docker.com/engine/reference/commandline/cli/)


#### Docker Commands
To execute docker commands you usually use sudo. Below are the main docker commands available to you.

**LOGIN COMMAND** - This command logs you into the docker hub, which is useful if you want to
upload your own docker images. The dockerhub is an online system which hosts pre-built docker images.

  `sudo docker login`


**IMAGES COMMAND** - This command lists the docker images downloaded onto your host machine, available to run locally.

  `sudo docker images`


**BUILD COMMAND** - This builds the specified docker file on your host machine. Note the full
stop at the end - this is required and isn’t a typo.

  `sudo docker build -t <docker file> .`


**PUSH COMMAND** - This uploads the docker file built via the build command, to the dockerhub
(needs a dockerhub account and you must be logged in).

  `sudo docker push <docker file>`


**RMI COMMAND** - This deletes a local docker image. Useful if an image is faulty,
or disk space is low. To find the docker image id’s, just run the `sudo docker images command`.

  `sudo docker rmi -f <image id>`


**PULL COMMAND** - This pulls the specified docker image from the docker hub.

  `sudo docker pull <docker file>`


**RUN COMMAND** - This runs a docker image locally on your host machine. The -v flag tells
docker to mount a host file directory, inside the docker container. This allows you to copy files
between the host, and the virtualised docker container. Here are the main parameters:

* **-i** is the interactive flag
* **-t** tells docker to open a terminal
* **-v** mounts a volume
* **-p** route ports between the host and container


`sudo docker run -it -v <local dir path>:<docker image dir path> <docker file>`

The ordering of flags and parameters matters. Put all the flags and parameters before the docker image is specified.

**Caveats:**
When using the `-v` flag, if you specify a path that already exists in the docker image via `<path to create in image>`,
    then any files there will be overwritten, IF they exist in `<path to local folder>`.


**Examples**

Here I list the available images:

```[lyon@zeus ~]$ sudo docker images
[sudo] password for lyon:
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
my-docker-image        latest              19e0164251da        8 days ago          84.91 MB
debian                 wheezy              34a0b91d4fe9        13 days ago         84.91 MB
scienceguyrob/docker   latest              44ddec452b70        2 weeks ago         3.521 GB
hello-world            latest              c54a2cc56cbb        4 months ago        1.848 kB
```

Here I run my docker image:

```[lyon@zeus ~]$ sudo docker run -it scienceguyrob/docker
root@3c6064b40e3b:~ls
DockerImageReadme.txt  psr
root@3c6064b40e3b:~
```

### Running Jupyter

To run jupyter in the container, you have to pipe the notebook server output to your host machine.

You can use the following steps to achieve this.

1. Run the docker container with the command,

      `sudo docker run -i -t -p 9999:9999 <your docker username>/<name of your image>`

2. Next you need to run your notebook (within the container) on the IP 0.0.0.0. to do this run the command,

      `jupyter notebook --notebook-dir=workspace --ip=0.0.0.0 --port=9999 --no-browser`

3. Now open `http://localhost:9999` in your browser to view your jupyter notebook.

You can load a workspace directory from your host machine into your container. For example I have
a path `/Volumes/data/Dropbox/Projects/Jupyter` which has my notebooks. If I run,

   `sudo docker run -i -t -p 9999:9999 scienceguyrob/pulsardsd -v /Volumes/data/Dropbox/Projects/Jupyter:/home/workspace`

I should see my notebooks when running:

`jupyter notebook --notebook-dir=workspace --ip=0.0.0.0 --port=9999 --no-browser`

Please be careful mounting volumes, as anything altered in your host folder will be changed.

### License

The code and the contents of this notebook are released under the GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007. 
