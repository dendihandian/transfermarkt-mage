FROM python:3.8-slim

RUN mkdir -p /opt/mage/app

COPY transfermarkt/ /opt/mage/app/

RUN pip install mage-ai

WORKDIR /opt/mage/app

EXPOSE 6789

ENTRYPOINT ["mage", "start"]
