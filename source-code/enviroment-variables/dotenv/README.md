# dotenv

The `dotenv` package is a simple and efficient way to load environment
variables from a `.env` file into your application's environment. It is
commonly used in development and testing environments to manage configuration
settings without hardcoding them into the source code.  Another important use
case is to keep sensitive information, such as API keys and database
credentials, out of version control systems.


## What is it?

1. `dot_env`: file to be renamed to `.env` in the directory where the script is
   run.
1. `dotenv_demo.py`: demo script that uses `dotenv` to load environment
   variables from the `.env` file.
1. `.gitignore`: to ignore the `.env` file in version control.
