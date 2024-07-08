#!/usr/bin/env bash

set -e
set -x

psql -U postgres
psql -c "CREATE DATABASE test"
