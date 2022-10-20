# k-python-boinc
Container for running your boinc in KnowledgeX


[Medium Article](https://blog.knowledgex.eu/how-to-run-your-python-code-in-knowledgex-749e2651370c)
## Non TEE workflow

Paste your code into the `def your_python_code()` in the `template_app.py`. 

### Run locally with env variables

```bash
  IEXEC_INPUT_FILES_NUMBER=1 \
  IEXEC_IN=sample_data \
  IEXEC_INPUT_FILES_FOLDER=sample_data \
  IEXEC_INPUT_FILE_NAME_1=data_set_full.csv \
  IEXEC_OUT=output \
  python3 src/template_app.py
```

### Build Docker image

```bash
docker build . --tag k-python-boinc
```

### Run from locally build docker image

```bash
rm -rf output && \
docker run \
        --rm \
        -e IEXEC_IN=/iexec_in \
        -e IEXEC_OUT=/iexec_out \
        -e IEXEC_INPUT_FILES_NUMBER=0 \
        -e IEXEC_INPUT_FILES_FOLDER=/iexec_in \
        -v $(pwd)/output:/iexec_out \
        -v $(pwd)/sample_data:/iexec_in \
        k-python-boinc
```

Once the execution ends, the result should be found in the folder output.

`cat output/computed.json`

### Deploy to DockerHub

```bash
docker tag k-python-boinc <dockerhub-user>/k-python-boinc:1.0.0
docker push <dockerhub-user>/k-python-boinc:1.0.0
```
### Run docker image directly from dockerhub

```bash
rm -rf output
docker run \
        --rm \
        -e IEXEC_IN=/iexec_in \
        -e IEXEC_OUT=/iexec_out \
        -e IEXEC_INPUT_FILES_NUMBER=1 \
        -e IEXEC_INPUT_FILES_FOLDER=/iexec_in \
        -e IEXEC_INPUT_FILE_NAME_1=data_set_full.csv \
        -v $(pwd)/output:/iexec_out \
        -v $(pwd)/sample_data:/iexec_in \
        docker.io/jadenx/k-python-boinc:1.0.0
```
