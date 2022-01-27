FROM python:3.9.7
LABEL maintainer "Sebastian Herrmann <s36400@beuth-hochschule.de>"
WORKDIR /code
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./ ./
EXPOSE 8050
CMD ["python", "./app.py"]