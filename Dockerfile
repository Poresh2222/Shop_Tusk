FROM python:3.8

WORKDIR /SHOP2
COPY . /SHOP2
RUN pip install pipenv
COPY Pipfile Pipfile.lock /SHOP2/
RUN pipenv install --system --dev

EXPOSE 8000