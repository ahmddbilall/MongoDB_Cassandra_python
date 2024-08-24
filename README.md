# Practicing No sql on kali linux using python




## Installation 

### MongoDB

reffer to offical [documentation](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/#std-label-install-mdb-community-debian)

or 

run following commands:

From a terminal, install gnupg and curl if they are not already available:
```
sudo apt-get install gnupg curl
```

To import the MongoDB public GPG key, run the following command:
```
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor
```

- Create a /etc/apt/sources.list.d/mongodb-org-7.0.list file for MongoDB.

    Create the list file using the command appropriate for your version of Debian:

    ```Debian 12 "Bookworm"
    echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
    ```



- Reload local package database
    Issue the following command to reload the local package database:
    ```
    sudo apt-get update
    ```


- Install the MongoDB packages
    To install the latest stable version, issue the following
    ```
    sudo apt-get install -y mongodb-org
    ```

### Cassandra
you need to install docker first

- Pull cassandra image using docker
    ``` 
    docker pull cassandra
    ```

- check if image is pulled or not
    ```
    docker images
    ```

- run cassandra 
    ```
    docker run -p 7000:7000 -p 7001:7001 -p 7199:7199 -p 9042:9042 -p 9160:9160 --name cassandra -d cassandra:latest
    ```





## Start environment

### Virtural environmet

```
python3 -m venv env
```

```
source env/bin/activate
```

### install dependencies

```
pip install -r requirement.txt
```
### Run Cassandra 

- cassandra run
 ```
 docker start cassandra
 ```

- check if the container is running or not

    ```
    docker ps
    ```


### run mongoDB

- start mongoDB server
```
sudo systemctl start mongod
```

- check if mongodb server is started or not
```
sudo systemctl status mongod
```


## Run Application

```
streamlit run 1_main.py
```
