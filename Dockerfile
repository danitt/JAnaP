FROM python:2.7.18

# Clone
WORKDIR /app
RUN git clone https://github.com/danitt/JAnaP.git

# Install dependencies
WORKDIR /app/JAnaP
RUN pip2 install -r bin/requirements.txt

# Share projects folder to host
RUN mkdir /app/JAnaP/data/projects
VOLUME /app/JAnaP/data/projects

# Set env
ENV APP_HOST=0.0.0.0
EXPOSE 5000

CMD [ "python", "web/application.py" ]
