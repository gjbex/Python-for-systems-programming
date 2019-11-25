# Application

Example of a very simple application that prints random integers between
two given values.  It uses argparse and configparser to handle configuration
files and command line arguments.

The parameters are
* `n`: the number of random values to generate,
* `a`: the smallest value to generate, and
* `b`: the largest value to generate.

The point is to illustrate specifying the parameters via
1. defaults in the application,  `n = 1`, `a = 0`, `b = 6`,
1. a "system" configuration file, `etc/my_app.conf`, `n = 2`, `a = 1`, `b = 6`,
1. optionally, a configurtion file specified as a command line option, i.e.,
   `--conf my_app.conf`, `n = 3`, `a = 2`,
1. command line options.

## What is it?
1. `my_apps.py`: Python script to print random integer values.
1. `etc/my_app.conf`: "system" level configuration file.
1. `my_app.conf`: optional "user" level configuration file.
