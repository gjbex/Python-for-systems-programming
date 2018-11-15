# Python systems programming

This repository contains material for a training on how to do systems
programming using Python.  The notebooks can be executed on
[Google Colab](https://colab.research.google.com/).

Python is a very versatile programming language that has a wide range of
applications.  This training concentrates on interaction with the
operating system, the file system, other applications and the network.
This is useful for systems programming, but also when you want to use
Python as a coordination language for your workflows.

Subjects and Python modules that will be covered:

  * interacting with the operating system: os, platform, sys, psutil
  * interacting with the filesystem: os.path, pathlib, shutil,
    fileinput, tempfile
  * running & communicating with other processes: sh, subprocess
  * command line arguments & configuration files: argparse, configparser
  * compressing & decompressing files: e.g., gzip, tarfile
  * running remote commands using SSH: paramiko


## What is it?

Jupyter notebooks:

  1. `system_information.ipynb`:
     illustrates how to use several standard library modules to
     retrieve information from the operating system
     [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gjbex/PythonSysProg/blob/master/system_information.ipynb)
  1. [`filesystem_interaction.ipynb`](https://colab.research.google.com/github/gjbex/PythonSysProg/blob/master/filesystem_interaction.ipynb):
     illustrates how to work with the file system.
  1. [`shell_interaction.ipynb`](https://colab.research.google.com/github/gjbex/PythonSysProg/blob/master/shell_interaction.ipynb):
     illustrates the use of the `sh` and
     `subprocess` modules to interact with the shell.
  1. [`julia.ipynb`](https://colab.research.google.com/github/gjbex/PythonSysProg/blob/master/julia.ipynb):
     illustrates monitoring a running process.
  1. [`compressed_files.ipynb`](https://colab.research.google.com/github/gjbex/PythonSysProg/blob/master/compressed_files.ipynb):
     illustrating how to work with compressed files and archives.

The notebook on SSH is not included, since that can not be used
without proper authentication.

Supporting materials:

  1. `julia_omp.f90`: Fortran source code used in several of the Jupyter
     notebooks.
     
