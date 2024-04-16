# Rerunnable

Toy application to explore the possibilities created by
using argparse options stored in a file.


## What is it?
1.  rerunnable.py`: script to explore the possibilities.


## How to use?

```bash
$ ./rerunnable.py  --verbose  --number 5  --type bye  gjb
$ ./rerunnable.py @rerunnable_cla.txt
```

This will rerun the application with all the settings specified for the
previous run.

To override options:
```bash
$ ./rerunnable.py  @rerunnable_cla.txt --number 3
```


## Conclusions

This approach works well for command line options, e.g., `--number 5`.

It is not flexibile for flags, e.g., `--verbose` since they can not be "unset".

It is not flexible either for positional arguments since they can not be modified.
