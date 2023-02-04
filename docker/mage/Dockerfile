FROM python:3.8-slim

RUN mkdir -p /opt/mage/app

COPY transfermarkt/ /opt/mage/app/

WORKDIR /opt/mage/app

RUN pip install -r requirements.txt

EXPOSE 6789

ENTRYPOINT ["mage", "start"]
