FROM locustio/locust

ADD source /locust-source

ADD init-file /init-file

EXPOSE 5557 5558 8089

ENTRYPOINT ["/init-file/run.sh"]
