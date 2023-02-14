#!/bin/sh

CUR_DIR=$(pwd)
cd "$(dirname $0)"
python3 -m app.db.seeds
cd $CUR_DIR
