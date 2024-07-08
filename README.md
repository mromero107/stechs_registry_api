# API Deployment and Usage Guide

This guide provides instructions on how to deploy and use the API.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Test](#test)
- [API Endpoints](#api-endpoints)


## Prerequisites

Before deploying and using the API, make sure you have the following prerequisites:

- Docker

## Build and run the API

1. make build
2. make setenv
3. make up
4. Visit `http://localhost:8000/api/docs` to access the documentation of the API.

## Test

1. make test

## API Endpoints

The API provides the following endpoints:

1. POST /cableModems - Create a new cable modem.
2. GET /cableModems - Get a list of cable modems.
3. GET /cableModems/{id} - Get a specific cable modem by ID.

For detailed information on each endpoint, refer to the API documentation.

