FROM python:bullseye

RUN mkdir -p /execute
WORKDIR /execute

ADD ./requirements.txt /execute/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /execute/requirements.txt --no-warn-script-location

COPY ./ /execute/

RUN useradd -ms /bin/sh rooot
RUN chmod -R og-w /execute
RUN chmod -R og+r /execute
RUN chmod ugo+x ./shell

ENV FLAG1="ITASEC{it_4as_A_th3ft_not_a_D0nat10n!}"
ENV FLAG2="ITASEC{A_fr0zen_USER-AGENT}"
ENV FLAG3="ITASEC{An_inn0cent_(and_Cute)_AP1}"

RUN python3 /execute/app.py docker
CMD ["uwsgi", "--http", ":5000", "--wsgi-file", "app.py", "--callable", "app", "--thunder-lock", "--enable-threads"]


