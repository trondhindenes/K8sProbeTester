FROM python:3.6.6
WORKDIR /app
COPY . .
RUN pip install pipenv
RUN pipenv install --system
EXPOSE 80
RUN ls
ENTRYPOINT ["uwsgi"]
CMD ["--wsgi-file", "wsgi.py","--http", "0.0.0.0:80", "--enable-threads", "--disable-write-exception", "--disable-logging"]