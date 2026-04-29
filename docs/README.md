Python is a very versatile programming language that has a wide range of
applications.  This training concentrates on interaction with the
operating system, the file system, other applications and the network.
This is useful for systems programming, but also when you want to use
Python as a coordination language for your workflows.
This training introduces modules that are useful in that context.

## Learning outcomes

When you complete this training you will

  * know how to write scripts that handle command line arguments,
    configuration files and environment variables;
  * know how to log information or errors from your applications;
  * be able to perform file system-related tasks;
  * be able to use a templating library for reporting;
  * be able to interact with processes on a Linux system;
  * be able to interact with remote systems using SSH;
  * be able to interact with compressed files.

## Schedule

Total duration: 4 hours.

  | Subject                                     | Duration |
  |---------------------------------------------|----------|
  | introduction and motivation                                       |  5 min.  |
  | command line argument, configuration files, environment variables | 40 min.  |
  | logging                                                           | 10 min.  |
  | interacting with the file system                                  | 40 min.  |
  | coffee break                                                      | 10 min.  |
  | data formats                                                      | 30 min.  |
  | templates                                                         | 10 min.  |
  | interacting with processes                                        | 45 min.  |
  | interacting with remote systems using SSH                         | 30 min.  |
  | compressed files                                                  | 10 min.  |
  | wrap up                                                           | 10 min.  |


## Training materials

Slides are available in the
 [GitHub repository](https://github.com/gjbex/Python-for-systems-programming),
as well as example code and hands-on material.


## Target audience

This training is for you if you need to use Python for scripting and
coordination of processes.


## Prerequisites

You will need experience programming in Python.  This is not a training that starts
from scratch.

If you plan to do Python programming in a Linux or HPC environment you should
be familiar with these as well.

More concretely, participants should already be comfortable with the following:

* running Python code in Jupyter or from the command line;
* variables, numbers, strings, booleans, and basic containers such as lists,
  tuples, and dictionaries;
* `if`/`else` statements, `for` loops, and simple comprehensions;
* writing and calling functions with arguments and return values;
* importing modules and using functions, classes, and constants from them;
* reading and writing small text files using `open(...)`;
* basic exception handling with `try`/`except`;
* working with paths and file names at a basic level;
* reading short Python scripts without needing every line explained.

You do not need prior experience with `argparse`, `configparser`, logging,
Jinja2, `subprocess`, `psutil`, AsyncSSH, Hydra, FastAPI, or binary/XML/CSV
parsing libraries beyond the Python basics. Those are part of the training
itself.

### Quick self-assessment

If you can do most of the tasks below without looking up basic Python syntax,
you are likely ready for this training.

* write a function that reads a text file and counts the number of lines;
* use `if`/`else` and a loop to filter or transform file names;
* import a module such as `pathlib`, `os`, `json`, or `csv` and use one of its
  basic features;
* define a small script that accepts one or two command-line arguments;
* read a short script that opens files, loops over records, and prints a
  result;
* build a dictionary from a few key-value pairs and retrieve one by key;
* make a small change to an existing script, run it again, and interpret the
  output;
* read a short traceback or error message and identify roughly where the
  problem occurred.

If several of these items still feel difficult, the training will probably move
too fast. In that case, it is better to first take a short introductory Python
course or refresh the basics.

### Software and access requirements

For following along hands-on, you need
* laptop or desktop with internet access.
* a Python environment that can run Jupyter Lab if you want to use your own system;
* access to Google Colaboratory if you prefer not to install software.


## Level of the Material

For participants who already have basic Python programming experience, the material in this training is approximately

* Introductory: 20 %
* Intermediate: 60 %
* Advanced: 20 %

These percentages describe the level of the systems programming and scripting
topics covered in the training, not the required entry level in Python itself.


## Trainer(s)

  * Geert Jan Bex ([geertjan.bex@uhasselt.be](mailto:geertjan.bex@uhasselt.be))
