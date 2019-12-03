# Hydra

Hydra is an application framework developed by Facebook that can be useful
in the context of scientific software.

It support configuration file handling, command line arguments, logging,
multiruns and so on.

## What is it?

1. `gen_rand.py`: Python script to write random numbers to standard
   output.
1. `conf/`: directory containing the configuration files.
   1. `config.yaml`: configuration file with the defaults.
   1. `distr/gauss.yaml`: configuration file for the Gaussian distirubtion.
   1. `distr/uniform.yaml`: configuration file for the uniform distirubtion.

## How to use it?
Run with configuratino file settings:
```bash
$ ./gen_rand.py
```
To increase the number of random values:
```bash
$ ./gen_rand.py 10
```

To use a uniform distribution:
```bash
$ ./gen_rand.py distr=uniform
```

To use a uniform distribution between -1 and 0:
```bash
$ ./gen_rand.py distr=uniform distr.a=-1.0 distr.b=0.0
```
