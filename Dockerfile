FROM python:3

# set a directory for the app
WORKDIR /Users/lindadaignault/Documents/coding/wg/wg-gesucht-updater

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000 

ARG password
ENV password_env=${password}
ENV PYTHONUNBUFFERED=1
ENV GOOGLE_APPLICATION_CREDENTIALS="./wg-gesucht-38980-dcac8f9f2907.json"

# run the command
CMD python wg-gesucht-updater.py -p ${password_env} -u ybsilas@gmail.com silas.a.burger@gmail.com -a 9054089 9363329 
