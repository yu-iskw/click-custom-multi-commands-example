NAME := click-multi-commands-example

create-conda:
	conda env create -f environment.yml -n $(NAME)

update-conda:
	conda env update -f environment.yml -n $(NAME)

remove-conda:
	conda env remove -y -n $(NAME)

lint:
	pycodestyle custom_commands
