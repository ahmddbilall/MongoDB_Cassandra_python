# Practicing NoSQL on Kali Linux Using Python

## Overview

This project demonstrates how to interact with NoSQL databases—MongoDB and Cassandra—using Python on a Kali Linux environment. It includes setup instructions, configuration, and running a sample application with Streamlit.

## Installation 

1. **Refer to the [official MongoDB documentation](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/#std-label-install-mdb-community-debian)** for detailed instructions.

2. **Alternatively, follow these steps to install MongoDB:**

   - **Install prerequisites:**

     ```bash
     sudo apt-get install gnupg curl
     ```

   - **Import the MongoDB public GPG key:**

     ```bash
     curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
        sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
        --dearmor
     ```

   - **Create a MongoDB repository list file:**

     For Debian 12 "Bookworm", run:

     ```bash
     echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
     ```

   - **Update local package database:**

     ```bash
     sudo apt-get update
     ```

   - **Install MongoDB packages:**

     ```bash
     sudo apt-get install -y mongodb-org
     ```

### Cassandra

1. **Install Docker** if not already installed.

2. **Pull the Cassandra Docker image:**

   ```bash
   docker pull cassandra
    ```

3. **Verify that the image is pulled:**
    ```
    docker images
    ```

4. **Run Cassandra using Docker:**
    ```
    docker run -p 7000:7000 -p 7001:7001 -p 7199:7199 -p 9042:9042 -p 9160:9160 --name cassandra -d cassandra:latest
    ```



## Start environment

### Virtural environmet

 1. **Create a virtual environment:**
   ```
   python3 -m venv env
   ```  
 2. **Activate the virtual environment:** 
   ```
   source env/bin/activate
   ```

### install dependencies

 1. **Install required Python packages:**
   ```
   pip install -r requirement.txt
   ```

### Run Cassandra 

 1. **Start Cassandra container:**
    ```
    docker start cassandra
    ```
 2. **Check if the container is running:**
    ```
    docker ps
    ```


### Run MongoDB

 1. **Start MongoDB server:**
   ```
   sudo systemctl start mongod
   ```
 2. **Check MongoDB server status:**
   ```
   sudo systemctl status mongod
   ```


## Run Application

 1. **Start the Streamlit application:**
   ```
   streamlit run 1_main.py
   ```


