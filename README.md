# test-assignment-hexlet-mentor
[![CI](https://github.com/emp7yhead/test-assignment-hexlet-mentor/actions/workflows/main.yml/badge.svg)](https://github.com/emp7yhead/test-assignment-hexlet-mentor/actions/workflows/main.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/871e0e2f47d57f96bbd4/test_coverage)](https://codeclimate.com/github/emp7yhead/test-assignment-hexlet-mentor/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Тest assignment for a python mentor position at hexlet.io.

https://hexlet-ru.notion.site/8b301b64d4834a3e91f709f8ada1187a
## Description:
The CLI utility on startup asks the user for a number and give the answer - Fizz, Buzz, FizzBuzz. Launching the application displays a greeting and asks for a number.

## Dependencies:
- python = "^3.10"
- prompt = "^0.4.1"

---
## Installation:
Install make. 
To work with Poetry install Poetry.
To work with Docker install Docker Engine.

The following options can be used for installation:
- ## Poetry: 
  1. Clone repository:
    ```
    git clone https://github.com/emp7yhead/test-assignment-hexlet-mentor.git
    cd test-assignment-hexlet-mentor
    ```
  2. Build the source and wheels archives:
    ```
    make build
    ```
  3. Install builded package:
    ```
    make package-install
    ```
    <img src="https://media0.giphy.com/media/CuX2D2nMkdmsueRf96/giphy.gif?cid=790b7611d70d6bb469cf27dc67d8cb0b0c3d15516f53e51b&rid=giphy.gif&ct=g" width="640"/>
- ## package manager pip:
    ```
    pip install --user git+https://github.com/emp7yhead/test-assignment-hexlet-mentor.git
    ```
    <img src="https://media2.giphy.com/media/7mqeCzCyX9KL6EL0yK/giphy.gif?cid=790b761135cf24847dcd40f6503e7b377fb3a4324e67a02b&rid=giphy.gif&ct=g" width="640"/>
- ## Docker:
    1. Clone repository:
    ```
    git clone https://github.com/emp7yhead/test-assignment-hexlet-mentor.git
    cd test-hexlet-mentor
    ```
    2. Install dependencies:
    ```
    make docker-build
    ```
    <img src="https://media2.giphy.com/media/MijRnnJjcmwUxkHNA3/giphy.gif?cid=790b761175b24218045264b479bf400f13fb3036e132304a&rid=giphy.gif&ct=g" width="640"/>
---
## Launch:
- If you choose installation with `pip` or `Poetry` use command:
    ```
    fizz_buzz
    ```
    <img src="https://media1.giphy.com/media/eRWFGRiJtto2hpE0U8/giphy.gif?cid=790b76115fe6f09321ba69d5d0d33fb1a1c394b1bfeda0f1&rid=giphy.gif&ct=g" width="640"/>

- If you choose installation with `Docker` use command:
    ```
    docker run -ti fizz_buzz
    ```
    <img src="https://media2.giphy.com/media/sBX9tub4daHd42rDE2/giphy.gif?cid=790b7611e97c3c1d470598d7e4631d954c3ab11dbd52dc24&rid=giphy.gif&ct=g" width="640"/>