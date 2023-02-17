[organism_growth_model.ipynb](organism_growth_model.ipynb) contiene un problema con una serie de ejercicios para introducir los conceptos y técnicas de aprendizaje supervisado moderno.

![organism](organism.png)

El problema es extremadamente sencillo, pero las técnicas y herramientas introducidas para su solución son las mismas que se usan para entrenar modelos de deep learning con billones de parámetros.

- [usage](#usage)
	- [install](#install)
	- [run notebook](#run-notebook)
	- [using docker](#using-docker)

## usage

JAX seems to work on linux and OS X but is tricky on windows, if you run into install problems you might want to run this inside docker as described below.

### install

```bash
python3 -m venv env
env/bin/pip install -r requirements.txt
```

### run notebook

```bash
env/bin/jupyter notebook
```

### using docker

You can run this using the standard python docker image: this command will launch an interactive docker container, mount the current directory under /supervised_learning, and map port 8888 to your host:

```bash
docker run -it --rm \
	-v $(pwd):/supervised_learning \
	-p 8888:8888 \
	--workdir /supervised_learning \
	python:3.10 /bin/bash
```

You can execute the install in the docker container, run jupyter in the container and point your browser to the appropriate url (read the output of the `jupyter notebook` command):

```bash
python3 -m venv env
env/bin/pip install -r requirements.txt
env/bin/jupyter notebook --no-browser --allow-root --ip=0.0.0.0 --port=8888
```
