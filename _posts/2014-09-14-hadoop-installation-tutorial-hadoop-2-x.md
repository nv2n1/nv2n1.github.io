---
title: "Setting Up a Hadoop 2.x Cluster for Development and Legacy Systems"
date: 2014-09-14 18:13:09 +0000
layout: post
canonical: https://www.systutorials.com/hadoop-installation-tutorial-hadoop-2-x/
---

Hadoop 2.x reached end-of-life in 2016. This guide covers setup for learning purposes and legacy system maintenance only. For production deployments, use Hadoop 3.x or later, which includes performance improvements, better YARN scheduling, HDFS erasure coding, and improved security. Cloud-managed options like AWS EMR, Google Dataproc, and Azure HDInsight eliminate most operational overhead.

This guide walks through setting up a three-node cluster (hofstadter, snell, biot) with hofstadter as the NameNode/ResourceManager. Hadoop 2.x introduced YARN (Yet Another Resource Negotiator), decoupling resource management from MapReduce job scheduling — a significant architectural change from 1.x.

## Prerequisites

- Linux user `hadoop` exists on all nodes with home directory `/home/hadoop/`
- Root or sudo access to configure system settings
- Network connectivity between all nodes with consistent DNS or `/etc/hosts` configuration
- JDK 8 or later (Hadoop 2.10.1 works through Java 21, though testing with Java 8-11 is more common)

## Hostname and Network Configuration

Hadoop uses hostnames for node discovery. Edit `/etc/hosts` on every node:

    10.0.3.29   hofstadter
    10.0.3.30   snell
    10.0.3.31   biot

Verify connectivity:

``` bash
ping -c 1 hofstadter
ping -c 1 snell
ping -c 1 biot
```

For clusters with 10+ nodes, use DNS instead of `/etc/hosts` to reduce maintenance burden.

## SSH Key-Based Authentication

The Hadoop user on the NameNode must SSH to all DataNodes without password prompts. Generate Ed25519 keys as the hadoop user on the NameNode:

``` bash
su - hadoop
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
```

Distribute the public key to all nodes:

``` bash
for node in snell biot; do
  ssh-copy-id -i ~/.ssh/id_ed25519.pub hadoop@$node
done
```

Test passwordless login:

``` bash
ssh hadoop@snell hostname
ssh hadoop@biot hostname
```

Both commands should return the node’s hostname without prompting for a password.

## Java Installation

Hadoop requires a JDK, not just a JRE. Install via your package manager or manually:

``` bash
# Using package manager (recommended)
apt-get install openjdk-11-jdk  # Debian/Ubuntu
# or
dnf install java-11-openjdk-devel  # RHEL/CentOS/Fedora
```

For manual installation, download from the OpenJDK repository and extract to `/usr/java/`:

``` bash
mkdir -p /usr/java
cd /usr/java
# Download and extract JDK tarball
ln -s jdk-21.x.x default
```

Add to `~/.bashrc` for the hadoop user on all nodes:

``` bash
export JAVA_HOME=/usr/java/default
export PATH=$JAVA_HOME/bin:$PATH
```

Source and verify:

``` bash
source ~/.bashrc
java -version
```

## Hadoop Installation

Download Hadoop 2.10.1 (final 2.x release) from the Apache archive:

``` bash
cd /home/hadoop
wget https://archive.apache.org/dist/hadoop/common/hadoop-2.10.1/hadoop-2.10.1.tar.gz
tar xzf hadoop-2.10.1.tar.gz
ln -s hadoop-2.10.1 hadoop
```

Add to `~/.bashrc` for the hadoop user on all nodes:

``` bash
export HADOOP_COMMON_HOME=$HOME/hadoop
export HADOOP_MAPRED_HOME=$HADOOP_COMMON_HOME
export HADOOP_HDFS_HOME=$HADOOP_COMMON_HOME
export YARN_HOME=$HADOOP_COMMON_HOME
export PATH=$PATH:$HADOOP_COMMON_HOME/bin:$HADOOP_COMMON_HOME/sbin
```

Reload and verify:

``` bash
source ~/.bashrc
hadoop version
```

## Configuration

All configuration files live in `$HADOOP_COMMON_HOME/etc/hadoop/`. Edit `.xml` files directly with a text editor — do not rely on shell scripts to modify them, as manual edits may be lost.

### core-site.xml

Set the NameNode address. Add this inside the `<configuration>` tags:

``` xml
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://hofstadter/</value>
  <description>NameNode URI</description>
</property>
```

### hdfs-site.xml

Configure HDFS replication and storage directories:

``` xml
<property>
  <name>dfs.replication</name>
  <value>3</value>
  <description>Number of block replicas</description>
</property>
<property>
  <name>dfs.namenode.name.dir</name>
  <value>file:///home/hadoop/hdfs/namenode</value>
  <description>NameNode metadata storage</description>
</property>
<property>
  <name>dfs.datanode.data.dir</name>
  <value>file:///home/hadoop/hdfs/datanode</value>
  <description>DataNode block storage</description>
</property>
```

Create these directories on all nodes:

``` bash
mkdir -p /home/hadoop/hdfs/namenode /home/hadoop/hdfs/datanode
chown hadoop:hadoop /home/hadoop/hdfs
```

Set `dfs.replication` to match your number of DataNodes or fewer. A three-node cluster can use replication factor 3; smaller clusters should lower this value.

### yarn-site.xml

Configure YARN resource management:

``` xml
<property>
  <name>yarn.resourcemanager.hostname</name>
  <value>hofstadter</value>
  <description>ResourceManager host</description>
</property>
<property>
  <name>yarn.nodemanager.aux-services</name>
  <value>mapreduce_shuffle</value>
  <description>Shuffle service for MapReduce</description>
</property>
<property>
  <name>yarn.nodemanager.resource.memory-mb</name>
  <value>4096</value>
  <description>Memory available per NodeManager in MB</description>
</property>
<property>
  <name>yarn.scheduler.minimum-allocation-mb</name>
  <value>512</value>
  <description>Minimum memory per container in MB</description>
</property>
<property>
  <name>yarn.scheduler.maximum-allocation-mb</name>
  <value>4096</value>
  <description>Maximum memory per container in MB</description>
</property>
```

Adjust memory values based on actual available RAM. A common formula: (total_ram – 2GB_system_overhead) = `yarn.nodemanager.resource.memory-mb`. If a node has 8GB RAM, set this to 6144 MB.

### mapred-site.xml

Copy the template and configure MapReduce to use YARN:

``` bash
cp $HADOOP_COMMON_HOME/etc/hadoop/mapred-site.xml.template \
   $HADOOP_COMMON_HOME/etc/hadoop/mapred-site.xml
```

Add to `mapred-site.xml`:

``` xml
<property>
  <name>mapreduce.framework.name</name>
  <value>yarn</value>
  <description>Use YARN for MapReduce</description>
</property>
<property>
  <name>mapreduce.jobhistory.address</name>
  <value>hofstadter:10020</value>
  <description>Job history server address</description>
</property>
<property>
  <name>mapreduce.jobhistory.webapp.address</name>
  <value>hofstadter:19888</value>
  <description>Job history web UI</description>
</property>
<property>
  <name>mapreduce.map.memory.mb</name>
  <value>512</value>
  <description>Memory per map task</description>
</property>
<property>
  <name>mapreduce.reduce.memory.mb</name>
  <value>512</value>
  <description>Memory per reduce task</description>
</property>
```

These map/reduce memory settings should not exceed `yarn.scheduler.maximum-allocation-mb`.

### workers (formerly slaves)

Edit `etc/hadoop/workers` and list all DataNode hostnames:

    hofstadter
    snell
    biot

The NameNode/ResourceManager can also run DataNode/NodeManager services (as shown here), though production deployments often dedicate the NameNode to metadata management only.

## Distribute Configuration to All Nodes

Use rsync to copy Hadoop configuration to all DataNodes:

``` bash
cd /home/hadoop
for node in snell biot; do
  echo "Syncing to $node..."
  rsync -avxz --delete hadoop/ hadoop@$node:/home/hadoop/hadoop/
done
```

Verify on each node:

``` bash
ssh hadoop@snell ls /home/hadoop/hadoop/etc/hadoop/core-site.xml
ssh hadoop@biot ls /home/hadoop/hadoop/etc/hadoop/core-site.xml
```

## Format the NameNode

On the NameNode only, initialize HDFS metadata:

``` bash
hdfs namenode -format
```

This creates the initial fsimage. Do this only once. Re-formatting destroys all HDFS data and cannot be undone.

## Start the Cluster

### Option 1: Individual Service Control

On the NameNode:

``` bash
hdfs --daemon start namenode
```

On each DataNode:

``` bash
hdfs --daemon start datanode
```

On the ResourceManager (usually the NameNode):

``` bash
yarn --daemon start resourcemanager
```

On each NodeManager:

``` bash
yarn --daemon start nodemanager
```

The `--daemon` flag runs the service in the background. Older Hadoop versions used `start-dfs.sh` and `start-yarn.sh` scripts, which still work but are less flexible.

### Option 2: Use Cluster Start Scripts

From the NameNode, start HDFS across all nodes listed in `workers`:

``` bash
start-dfs.sh
```

This command uses SSH to launch NameNode and DataNode services. Similarly, start YARN:

``` bash
start-yarn.sh
```

Run these scripts from the NameNode to ensure proper SSH communication.

## Verify Cluster Status

Check HDFS health:

``` bash
hdfs dfsadmin -report
```

Sample output:

    Configured Capacity: 335,854,977,024 (312.59 GB)
    Present Capacity: 335,854,977,024 (312.59 GB)
    DFS Remaining: 335,854,977,024 (312.59 GB)
    DFS Used: 0 (0 B)
    DFS Used%: 0.00%
    Under replicated blocks: 0
    Blocks with corrupt replicas: 0
    Missing blocks: 0

    Live datanodes (3):
    Name: 10.0.3.30:50010 (snell)
    Hostname: snell
    ...

Check YARN node status:

``` bash
yarn node -list
```

Sample output:

    Total Nodes:3
             Node-Id            Node-State Node-Http-Address   Number-of-Running-Containers
    hofstadter:43469           RUNNING    hofstadter:8042                              0
    snell:57039                RUNNING    snell:8042                                    0
    biot:52834                 RUNNING    biot:8042                                     0

All nodes should report RUNNING state.

## Web UIs

Access cluster dashboards via browser:

- **HDFS NameNode**: <a href="http://hofstadter:9870/" rel="nofollow">http://hofstadter:9870/</a> (shows block inventory, replication status, dead nodes)
- **YARN ResourceManager**: <a href="http://hofstadter:8088/" rel="nofollow">http://hofstadter:8088/</a> (shows running and completed applications, node resources)
- **Job History Server**: <a href="http://hofstadter:19888/" rel="nofollow">http://hofstadter:19888/</a> (MapReduce job logs)

## Run a Test Job

Create HDFS home directory:

``` bash
hadoop fs -mkdir -p /user/hadoop
```

Upload test data:

``` bash
hadoop fs -put $HADOOP_COMMON_HOME/etc/hadoop test-input
```

Run the built-in grep example:

``` bash
hadoop jar $HADOOP_COMMON_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar \
  grep test-input test-output 'dfs[a-z.]*'
```

Monitor the job at <a href="http://hofstadter:8088/" rel="nofollow">http://hofstadter:8088/</a>. Once complete, check results:

``` bash
hadoop fs -ls test-output/
hadoop fs -cat test-output/part-r-00000
```

The output will list all lines from the input containing the regex pattern.

## Stop the Cluster

### Option 1: Individual Service Control

On each node, stop services in reverse order:

``` bash
# On each DataNode
hdfs --daemon stop datanode

# On NameNode
hdfs --daemon stop namenode

# On each NodeManager
yarn --daemon stop nodemanager

# On ResourceManager
yarn --daemon stop resourcemanager
```

### Option 2: Use Cluster Stop Scripts

From the NameNode:

``` bash
stop-dfs.sh
stop-yarn.sh
```

These scripts use SSH to stop services across all nodes in `workers`.

## Debugging and Troubleshooting

Check logs on any node:

``` bash
ls $HADOOP_COMMON_HOME/logs/
tail -f $HADOOP_COMMON_HOME/logs/hadoop-hadoop-namenode-hofstadter.log
tail -f $HADOOP_COMMON_HOME/logs/hadoop-hadoop-datanode-snell.log
```

### Connection Refused / SSH Failures

- Verify SSH is running on all nodes: `systemctl status ssh` (or `sshd` on some systems)
- Check that the hadoop user can SSH without a password: `ssh hadoop@snell echo test`
- Ensure firewall rules permit SSH (port 22) and Hadoop ports (9000, 9870, 8088, 50010)

### Port Conflicts

- NameNode: 9000 (RPC), 9870 (web UI)
- DataNode: 50010 (data transfer), 50020 (IPC)
- ResourceManager: 8032 (RPC), 8088 (web UI)
- NodeManager: 8042 (web UI), 8040 (RPC)

Check if ports are in use:

``` bash
netstat -tlnp | grep :9000
lsof -i :8088
```

### Java Not Found

- Verify `JAVA_HOME` is set: `echo $JAVA_HOME`
- Confirm the path exists: `ls $JAVA_HOME/bin/java`
- Source `~/.bashrc` again if recently added: `source ~/.bashrc`

### Blocks Under-Replicated

- Check that `dfs.replication` does not exceed the number of DataNodes
- Verify all DataNodes are healthy: `hdfs dfsadmin -report`
- Wait for the rebalancer to complete; this can take minutes on large datasets

### NameNode Safemode

On startup, HDFS enters safemode while blocks are inventoried. Check status:

``` bash
hdfs dfsadmin -safemode get
```

Force exit (only if blocks are verified):

``` bash
hdfs dfsadmin -safemode leave
```

## Full Cluster Reset

To reset from scratch:

``` bash
# Stop all services
stop-dfs.sh
stop-yarn.sh

# Clean data on NameNode
rm -rf /home/hadoop/hdfs /home/hadoop/hadoop/logs

# Clean data on all DataNodes
for node in snell biot; do
  ssh hadoop@$node 'rm -rf /home/hadoop/hdfs /home/hadoop/hadoop/logs'
done

# Re-format and restart
hdfs namenode -format
start-dfs.sh
start-yarn.sh
```

## Configuration Reference

| Parameter | File | Purpose | Example |
|----|----|----|----|
| `fs.defaultFS` | core-site.xml | NameNode address | `hdfs://hofstadter/` |
| `dfs.replication` | hdfs-site.xml | Block replication factor | `3` |
| \`d |  |  |  |
