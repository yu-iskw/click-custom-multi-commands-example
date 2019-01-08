# Example of click's custom multip commands with dynamicaly loading

## Prepare for the environment

```
# Create anaconda environment.
make create-conda

# Activate the anaconda environment.
conda activate click-multi-commands-example

# Install the package locally.
pip install -e .
```

## Run the commands

```
##############################################
$ custom_commands
Usage: custom_commands [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  command1
  command2:w

#############################################
$ custom_commands command1
Usage: custom_commands command1 [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete
  update

$ custom_commands command1 create
create is invoked in command1.

#############################################
$ custom_commands command2
Usage: custom_commands command2 [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete
  update

$ custom_commands command2 delete
delete is invoked in command2.
```

## Links
- https://click.palletsprojects.com/en/7.x/commands/#custom-multi-commands
