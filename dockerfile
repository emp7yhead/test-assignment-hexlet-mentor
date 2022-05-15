FROM python:3.10.4

WORKDIR /usr/src/fizzbuzz

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/usr/src/fizzbuzz"

CMD [ "python", "./fizzbuzz/scripts/game.py" ]