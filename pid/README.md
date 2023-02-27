WIP de ejemplo de ejercicios para PIDs.

- [usage](#usage)
	- [install](#install)
	- [run tests](#run-tests)
	- [run notebook](#run-notebook)
	- [using docker](#using-docker)

## usage

### install

```bash
python3 -m venv env
env/bin/pip install -r requirements.txt
```

### run tests

```bash
env/bin/python -m unittest discover . -p "*.py" -v
```

### run notebook

```bash
env/bin/jupyter notebook
```

### using docker

```bash
docker run -it --rm \
	-v $(pwd):/pid \
	-p 8888:8888 \
	--workdir /pid \
	python:3.10 /bin/bash
```

You can execute the install in the docker container, run jupyter in the container and point your browser to the appropriate url (read the output of the `jupyter notebook` command):

```bash
python3 -m venv env
env/bin/pip install -r requirements.txt
env/bin/jupyter notebook --no-browser --allow-root --ip=0.0.0.0 --port=8888
```
