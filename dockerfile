FROM python:3.12

SHELL [ "/bin/bush" ,"-c" ]
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# RUN python -m pip install --upgrade pip
# RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
# libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim
# RUN useradd -rms /bin/bush tk && chmod 777 opt/ run/
WORKDIR /tk
# RUN mkdir /tk/static && mkdir /tk/media && chown -R tk:tk /tk && chmod 755 /tk
# RUN mkdir /tk/static && mkdir /tk/media
COPY --chown=tk:tk . .
RUN pip install -r requirements.txt
USER tk
CMD [ "gunicorn" , "-b" , "0.0.0.8001" , "TEHNOCK.wsgi:application"]