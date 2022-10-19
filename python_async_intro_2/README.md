## api

`GET jobs/`

```json
[2, 31232, 12]
```

`POST create_job/{num_boots}`

```json
21
```

`GET wait_for_job?job_id={job_id}`

```json
"done"
```

## usage

### install

```
python3 -m venv env
env/bin/pip install -r requirements.txt
```

### test

```
env/bin/python -m unittest discover .
```
