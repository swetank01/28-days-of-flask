FROM python:3.11.0a5-alpine
ENV PYHTONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
# ENTRYPOINT ["/app/entrypoint.sh"]