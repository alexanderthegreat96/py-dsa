# Default action
.PHONY: test

# The first argument is "test", the second is the name of the file
test:
	@# Capture the second word from the command line arguments
	$(eval NAME := $(filter-out $@,$(MAKECMDGOALS)))
	@if [ -z "$(NAME)" ]; then \
		echo "Error: Please specify a file name. Example: make test bubble_sort"; \
		exit 1; \
	fi
	python3 -m unittest -v tests/test_$(NAME).py

# This catch-all prevents Make from complaining that the filename isn't a target
%:
	@:
