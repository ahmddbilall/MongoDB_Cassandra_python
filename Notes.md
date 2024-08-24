# MongoDB & Cassandra Notes

## 🗃️ MongoDB Commands

### Managing MongoDB Service

- Start MongoDB:
  ```bash
  sudo systemctl start mongod
  ```

- Check MongoDB Status:
  ```bash
  sudo systemctl status mongod
  ```
- Stop MongoDB:
  ```bash
  sudo systemctl stop mongod
  ```

- Restart MongoDB:
  ```bash
  sudo systemctl restart mongod
  ```

### Basic MongoDB Operations

 - Launch MongoDB Shell:
   ```
   mongo
   ```
 
 - Show All Databases:
   ```
   show databases
   ```
   
 -  Switch to a Database:
   ```
   use your_db_name
   ```

 - Show Collections in the Database:
   ```
   show collections
   ```

 - Query a Collection:
   ```
   db.your_collection_name.find().pretty()
   ```

 - Drop a Collection:
   ```
   db.your_collection_name.drop()
   ```   


## 🗄️ Cassandra Commands


### Running Cassandra

 - Start Cassandra with Docker:
   ```
   docker run cassandra
   ```

 - Access the Cassandra Container:
   ```
   docker exec -it CONTAINER_ID bash
   ```
   (Replace CONTAINER_ID with your actual container ID, e.g., 4a37eec4c171)

 - Open Cassandra Shell (CQLSH):
   ```
   cqlsh
   ```

### Keyspace Management

#### Keyspace Overview:

  - A keyspace is a logical partition in memory, containing a collection of tables.
  - Keyspaces are isolated from one another, and switching between them requires specific commands.

**List All Keyspaces:**
   ```
   describe keyspaces;
   ```

**Describe a Specific Keyspace:**
  ```
  describe KEY_SPACE_NAME;
  ```

**Switch to a Keyspace:**
  ```
  use KEY_SPACE_NAME;
  ```
**CREATE a Keyspace**
  ```
  CREATE KEYSPACE example_keyspace
  WITH REPLICATION = {
  'class': 'SimpleStrategy',
  'replication_factor': 3
  };
  ```

**Drop a Keyspace:**
  ```
  DROP KEYSPACE example_keyspace;
  ```

**Alter a Keyspace:**
  ```
  ALTER KEYSPACE example_keyspace
  WITH REPLICATION = {
    'class': 'NetworkTopologyStrategy',
    'datacenter1': 3,
    'datacenter2': 2
  };
  ```

### Understanding Replication Strategies

#### NetworkTopologyStrategy:
Useful for global distribution and fault tolerance. Each datacenter operates independently:
 - Fault Tolerance: Ensures continuous operation even if one datacenter goes down.
 - Data Locality: Reduces latency by keeping data close to users.
 - Global Reach: Ideal for applications with a global user base.

### Table Management

**Describe All Tables in a Keyspace**
  ```
  describe tables;
  ```





  
  
  
