# AsyncSSH

AsyncSSH is a non-standard Python library for working with SSH client/server.
It can be used to execute command on a remote host, or perform file transfers
using the SFTP protocol.


## What is it?

1. `environment.yml`: An conda environment file that can be used to create a
   Python environment with AsyncSSH installed.
1. `ls.py`: performs an `ls` command for the specified directory on a remote
   host.
1. `wc.py`: example of executing a command on a remote machine that reads from
   standard input, and writes to standard output/error.
1. `ssh_interaction.ipynb`: Jupyter notebook illustrating the use of AsyncSSH
   to interact with a remote host, execute commands on it, and transfer files
   using SFTP.
