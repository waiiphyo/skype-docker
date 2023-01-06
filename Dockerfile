FROM python:3.6-alpine

ENV Skype_Username $skype_user
ENV Skype_Password $skype_passwd
ENV flask_host $host
ENV flask_port $port

RUN pip install flask \
    && pip install SkPy

RUN mkdir /root/skype/
COPY skypeapi.py /opt/

EXPOSE $port

#EXPOSE

WORKDIR /opt

CMD ["python", "skypeapi.py"]



