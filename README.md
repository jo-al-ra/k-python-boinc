# k-python-template
Template for running your python code in KnowledgeX

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
docker build . --tag k-python-template
```

### Run from locally build dcoker image

```bash
rm -rf output && \
docker run \
        --rm \
        -e IEXEC_IN=/iexec_in \
        -e IEXEC_OUT=/iexec_out \
        -e IEXEC_INPUT_FILES_NUMBER=1 \
        -e IEXEC_INPUT_FILES_FOLDER=/iexec_in \
        -e IEXEC_INPUT_FILE_NAME_1=data_set_full.csv \
        -v $(pwd)/output:/iexec_out \
        -v $(pwd)/sample_data:/iexec_in \
        k-python-template
```

Once the execution ends, the result should be found in the folder output.

`cat output/computed.json`

### Deploy to DockerHub

```bash
docker tag k-python-template <dockerhub-user>/k-python-template:1.0.0
docker push <dockerhub-user>/k-python-template:1.0.0
```
### Run docker image directly from dockerhub

```bash
rm -rf output && \
docker run \
        --rm \
        -e IEXEC_IN=/iexec_in \
        -e IEXEC_OUT=/iexec_out \
        -e IEXEC_INPUT_FILES_NUMBER=1 \
        -e IEXEC_INPUT_FILES_FOLDER=/iexec_in \
        -e IEXEC_INPUT_FILE_NAME_1=data_set_full.csv \
        -v $(pwd)/output:/iexec_out \
        -v $(pwd)/sample_data:/iexec_in \
        docker.io/jadenx/k-python-template:1.0.0
```