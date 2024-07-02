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
   1. `file_config.yaml`: configuration file with the output file name.
1. `debug.py`: Python script that simply prints the configuration settings for
   debugging purposes.


## How to use it?
Run with configuratino file settings:
```bash
$ ./gen_rand.py
```
To increase the number of random values:
```bash
$ ./gen_rand.py n=10
```

To use a uniform distribution:
```bash
$ ./gen_rand.py distr=uniform
```

To use a uniform distribution between -1 and 0:
```bash
$ ./gen_rand.py distr=uniform distr.a=-1.0 distr.b=0.0
```

To use a different configuration file:
```bash
$ ./gen_rand.py  -cn file_config.yaml
``` 
or
```bash
$ ./gen_rand.py  --config-name=file_config.yaml
```

To perform multiple runs with different parameter values:
```bash
$ ./gen_rand.py -m distr=uniform,gauss
``` 

To view the configuration settings, e.g., for debugging:
```bash 
$ ./gen_rand.py  --cfg=job  distr=uniform
```
