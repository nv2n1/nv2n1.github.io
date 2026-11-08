---
title: "Installing Hadoop 1.x: A Complete Guide"
date: 2012-10-09 08:41:39 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/hadoop-installation-tutorial/
---

Hadoop 1.x reached end-of-life in 2014 and is no longer maintained. This post documents a deprecated architecture for historical reference only.

For new deployments, use **Hadoop 3.x+** with YARN, which offers significant improvements in resource management, multi-tenancy, and reliability. See the <a href="https://hadoop.apache.org/docs/stable/" rel="nofollow noopener" target="_blank">Apache Hadoop documentation</a> for current versions.

For managed services, consider AWS EMR, Google Dataproc, Azure HDInsight, or Cloudera.

------------------------------------------------------------------------

## Architecture Overview

Hadoop consists of two core components:

- **HDFS (Hadoop Distributed File System)**: The distributed storage layer, loosely modeled after Google File System (GFS). Stores data in blocks across DataNodes with configurable replication.
- **MapReduce**: A programming model and execution framework for batch processing. Hadoop’s implementation is an open-source variant of Google’s original MapReduce, used for processing large datasets across clusters.

The typical cluster topology uses:

- **NameNode**: Manages the HDFS namespace and file system tree
- **JobTracker**: Schedules MapReduce jobs and monitors TaskTrackers
- **DataNodes**: Store HDFS blocks
- **TaskTrackers**: Execute map and reduce tasks (slaves)

This architecture was replaced by YARN in Hadoop 2.x, which separates resource management from job scheduling.

## Prerequisites

- Linux cluster with passwordless SSH configured between nodes
- Dedicated Linux user (typically `hadoop`) on each node
- Java Development Kit (JDK 8+) installed on all nodes

## Setting Up SSH Key-Based Authentication

Enable the `hadoop` user to SSH between nodes without passwords:

``` bash
# On the NameNode, as the hadoop user
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Copy the public key to all DataNodes
for host in $(cat /home/hadoop/nodes); do
  ssh-copy-id -i ~/.ssh/id_rsa.pub hadoop@$host
done
```

The `nodes` file contains one hostname or IP per line.

## Installing Java

Modern Hadoop requires Java 8 or later. Install via your distribution’s package manager where possible:

``` bash
# Ubuntu/Debian
sudo apt-get install openjdk-11-jdk

# RHEL/CentOS
sudo yum install java-11-openjdk-devel

# Or manually download from Oracle/AdoptOpenJDK and extract to:
/home/hadoop/jdk/
```

If installing manually, distribute to all nodes:

``` bash
for host in $(cat /home/hadoop/nodes); do
  scp -r /home/hadoop/jdk hadoop@$host:/home/hadoop/
done
```

## Installing Hadoop 1.x

Download Hadoop from the <a href="https://archive.apache.org/dist/hadoop/common/" rel="nofollow noopener" target="_blank">Apache Archive</a>. Extract to all nodes:

``` bash
# On NameNode
tar xzf hadoop-1.2.1.tar.gz -C /home/hadoop/
ln -s /home/hadoop/hadoop-1.2.1 /home/hadoop/hadoop

# Distribute to DataNodes
for host in $(cat /home/hadoop/nodes); do
  scp -r /home/hadoop/hadoop-1.2.1 hadoop@$host:/home/hadoop/
  ssh hadoop@$host "ln -s /home/hadoop/hadoop-1.2.1 /home/hadoop/hadoop"
done
```

## Configuring Environment Variables

Add to `~/.bashrc` for the `hadoop` user on all nodes:

``` bash
export HADOOP_HOME="/home/hadoop/hadoop"
export JAVA_HOME="/home/hadoop/jdk"
export PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
export HADOOP_CONF_DIR=$HADOOP_HOME/conf
```

Source the file:

``` bash
source ~/.bashrc
```

## Configuring Hadoop

Edit configuration files in `$HADOOP_HOME/conf/` on the NameNode, then distribute to all nodes.

### hadoop-env.sh

Set Java and log paths:

``` bash
export JAVA_HOME=/home/hadoop/jdk
export HADOOP_LOG_DIR=/home/hadoop/data/logs
export HADOOP_PID_DIR=/home/hadoop/pids
```

Create required directories on all nodes:

``` bash
mkdir -p /home/hadoop/data/logs /home/hadoop/pids
```

### core-site.xml

Set the NameNode address (example: 10.1.1.30):

``` xml
<configuration>
  <property>
    <name>fs.default.name</name>
    <value>hdfs://10.1.1.30:9000</value>
  </property>
  <property>
    <name>hadoop.tmp.dir</name>
    <value>/home/hadoop/data/tmp</value>
  </property>
</configuration>
```

### hdfs-site.xml

Configure replication and storage paths:

``` xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>3</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>/home/hadoop/data/dfs/name</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>/home/hadoop/data/dfs/data</value>
  </property>
  <property>
    <name>dfs.namenode.secondary.http-address</name>
    <value>10.1.1.31:50090</value>
  </property>
</configuration>
```

Create directories on all nodes:

``` bash
mkdir -p /home/hadoop/data/dfs/name /home/hadoop/data/dfs/data
```

### mapred-site.xml

Configure the JobTracker (example: 10.1.1.2):

``` xml
<configuration>
  <property>
    <name>mapred.job.tracker</name>
    <value>10.1.1.2:9001</value>
  </property>
  <property>
    <name>mapred.local.dir</name>
    <value>/home/hadoop/data/mapred/local</value>
  </property>
  <property>
    <name>mapred.system.dir</name>
    <value>/hadoop/mapred/system</value>
  </property>
  <property>
    <name>mapred.tasktracker.map.tasks.maximum</name>
    <value>2</value>
  </property>
  <property>
    <name>mapred.tasktracker.reduce.tasks.maximum</name>
    <value>2</value>
  </property>
</configuration>
```

Create local directories on all DataNodes:

``` bash
mkdir -p /home/hadoop/data/mapred/local
```

### slaves

List all DataNode hostnames (one per line), excluding NameNode and JobTracker:

    datanode1
    datanode2
    datanode3
    datanode4

Remove or comment out `localhost` if present.

## Distributing Configuration to All Nodes

After configuring the NameNode:

``` bash
for host in $(cat /home/hadoop/hadoop/conf/slaves); do
  scp -r /home/hadoop/hadoop/conf hadoop@$host:/home/hadoop/hadoop/
done
```

## Starting the Cluster

### Format HDFS (First Time Only)

On the NameNode, format the namespace:

``` bash
hdfs namenode -format
```

This initializes the HDFS directory structure. Do this only once—formatting an existing cluster erases all data.

### Start HDFS

On the NameNode:

``` bash
start-dfs.sh
```

Verify all DataNodes are registered:

``` bash
hadoop dfsadmin -report
```

Wait a few seconds if not all nodes appear immediately.

### Start MapReduce

On the JobTracker node:

``` bash
start-mapred.sh
```

Check job status:

``` bash
hadoop job -list
```

## Running a Test Job

Test with a built-in example. Copy input data:

``` bash
hadoop fs -mkdir input
hadoop fs -put /home/hadoop/hadoop/conf input
```

Run the grep example:

``` bash
hadoop jar /home/hadoop/hadoop/share/hadoop/mapreduce1/hadoop-examples-1.*.jar \
  grep input output 'dfs[a-z.]+'
```

Retrieve results:

``` bash
hadoop fs -cat output/* | head -20
```

Or copy locally:

``` bash
hadoop fs -get output ./output-local
cat ./output-local/*
```

## Stopping the Cluster

``` bash
stop-dfs.sh
stop-mapred.sh
```

## Troubleshooting

### Nodes Don’t Connect

Check network connectivity and firewall rules:

``` bash
# Test SSH from NameNode
ssh hadoop@datanode1 "hostname"

# Check Hadoop ports are reachable
telnet datanode1 50075  # DataNode port
```

### Namenode Safe Mode

If the NameNode won’t exit safe mode after startup:

``` bash
hadoop dfsadmin -safemode leave
```

Safe mode can take minutes on large clusters. Check status with:

``` bash
hadoop dfsadmin -safemode get
```

### Permission Issues

Ensure the `hadoop` user owns all Hadoop directories:

``` bash
sudo chown -R hadoop:hadoop /home/hadoop/data /home/hadoop/hadoop
```

### Firewall Blocking Connections

On RHEL/CentOS systems, disable restrictive firewall rules for internal networks:

``` bash
# Flush iptables (warning: affects all traffic)
sudo iptables -F
sudo systemctl restart iptables
```

For production, use specific rules instead of flushing all policies.

### Check Logs

Review logs on NameNode:

``` bash
tail -f /home/hadoop/data/logs/hadoop-hadoop-namenode-*.log
```

DataNode logs:

``` bash
tail -f /home/hadoop/data/logs/hadoop-hadoop-datanode-*.log
```

## Default Ports

| Service            | Port  |
|--------------------|-------|
| NameNode Web UI    | 50070 |
| DataNode Web UI    | 50075 |
| JobTracker Web UI  | 50030 |
| TaskTracker Web UI | 50060 |
| NameNode RPC       | 9000  |
| JobTracker RPC     | 9001  |

Access web UIs at `http://namenode-ip:50070/` and `http://jobtracker-ip:50030/`.
