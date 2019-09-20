#!/bin/bash
RAND_PORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
HOST=localhost
echo Connect to: http://$HOST:$RAND_PORT
docker run -it -p $RAND_PORT:8888 jupyter/base-notebook start-notebook.sh --NotebookApp.password='' --NotebookApp.token=''
