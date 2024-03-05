FROM python:3.10
COPY /* /webapp
WORKDIR /webapp
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT [ "uvicorn" ]
CMD [ "--host","0.0.0.0", "main:app" ]
