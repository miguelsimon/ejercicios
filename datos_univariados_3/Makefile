env_ok: requirements.txt
	rm -rf env env_ok
	python3 -m venv env
	env/bin/pip install -r requirements.txt
	touch env_ok

run_notebook: env_ok
	env/bin/jupyter notebook

clean:
	rm -rf env_ok env
