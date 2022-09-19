FROM python:3

# set a directory for the app
WORKDIR .

# copy all the files to the container
COPY wg-gesucht-updater.py .
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000 

ARG password
ENV password_env=${password}
ENV PYTHONUNBUFFERED=1

# run the command
CMD python wg-gesucht-updater.py -p ${password_env} -u ybsilas@gmail.com silas.a.burger@gmail.com -a 9054089 9363329 -w 1200
