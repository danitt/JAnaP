
# JAnaP - Junction Analyzer Program

Please refer to the following article for more information and/or cite when using the JAnaP for published works : Gray, K.M., Katz, D.B., Brown, E.G. et al. Ann Biomed Eng (2019). https://doi.org/10.1007/s10439-019-02266-5

Please also complete this short form prior to download: https://forms.gle/m7sGwd69sEhiGRJc9 so we can track who is using the program and for what research applications it is being used. 

All necessary instructions to install and use the program can be found in the JAnaP User Guide provided.


## Quick Start
The easiest way to run the application on any operating system is via [Docker](https://www.docker.com).


1. Install Docker
    - https://www.docker.com/products/docker-desktop

2. Run the following commands from your terminal

    - 2.1. Folder Creation (initial setup only)

        - `mkdir projects`

        - **Note**: this is where the data will be stored for the JAnaP projects you set up (see User Manual)

    - 2.2. Starting Application

        - Linux/Mac: ```docker run --rm -p 5000:5000 -v `pwd`/projects:/app/JAnaP/data/projects danitt/janap```

        - Windows: ```docker run --rm -p 5000:5000 -v projects:/app/JAnaP/data/projects danitt/janap```

3. Open your browser to this page:

    - `http://localhost:5000`

**Note:** you do _not_ have to download this repository at all, simply follow the above steps



## Setup

### Configuration

The file `node.conf` contains a default configuration that is loaded by the application. If you need to move the data directory (i.e. using an external drive to hold large files), create a file named `node.conf.local` which will be read **instead** of `node.conf`. The application does not combine the options from both files, if `.local` exists it will use those options. 

### Windows 

You will need to install the C++ compiler for Python. Download it here: https://www.microsoft.com/en-us/download/details.aspx?id=44266

To setup everything you need to run the code on a Windows machine, run the `setup.bat` file which can be found in `bin/setup.bat`. This script will do the following: 

### Linux

Use the following commands:

```
$ mkdir bin/packages
$ wget -P bin/packages/ https://s3.amazonaws.com/umd-cells/packages/ij150-linux64-java8.zip
$ unzip bin/packages/ij150-linux64-java8.zip -d bin/packages/
```

Then setup a virtualenv to work out of and install requirements: 

```
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r bin/requirements.txt
```

### Setting up Notebooks

```
$ jupyter nbextension enable --py widgetsnbextension
```

### Checking for Errors

In order to check for errors after running jobs, navigate to your main repository, then go to: data / projects / 'your project name' / system / job errors
