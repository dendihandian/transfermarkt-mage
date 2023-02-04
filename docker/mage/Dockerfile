FROM python:3.8-slim

RUN mkdir -p /opt/mage/app

COPY transfermarkt-pipeline/ /opt/mage/app/

RUN pip install mage-ai

WORKDIR /opt/mage/

EXPOSE 6789

ENTRYPOINT ["mage", "start", "app"]
