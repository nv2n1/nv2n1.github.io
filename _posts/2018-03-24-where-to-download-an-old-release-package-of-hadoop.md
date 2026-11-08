---
title: "How to Download Older Versions of Hadoop"
date: 2018-03-24 11:51:35 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/where-to-download-an-old-release-package-of-hadoop/
---

Sometimes you need an older version of Hadoop — for compatibility with existing jobs, to reproduce bugs, or to match a specific cluster environment. The Apache Hadoop project maintains an archive of all past releases.

## From the Apache Archive

All Hadoop releases are available from the Apache Software Foundation’s distribution archive:

```wp-block-code
https://archive.apache.org/dist/hadoop/common/
```

Browse the directory to find the version you need. Each release directory contains:

- Source tarball (`hadoop-X.Y.Z-src.tar.gz`)
- Binary tarball (`hadoop-X.Y.Z.tar.gz`)
- Release notes and checksums

Download a specific version directly:

```wp-block-code
# Example: Hadoop 3.3.6
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

# Example: Hadoop 2.10.2
wget https://archive.apache.org/dist/hadoop/common/hadoop-2.10.2/hadoop-2.10.2.tar.gz
```

## Verify the Download

Always verify checksums for downloaded archives:

```wp-block-code
# Download SHA256 checksum
wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz.sha256

# Verify
sha256sum -c hadoop-3.3.6.tar.gz.sha256
```

Or verify with GPG signatures:

```wp-block-code
# Import Apache release keys
gpg --import https://downloads.apache.org/hadoop/common/KEYS

# Verify signature
gpg --verify hadoop-3.3.6.tar.gz.asc hadoop-3.3.6.tar.gz
```

## Install the Downloaded Version

Extract and configure the specific version:

```wp-block-code
tar -xzf hadoop-3.3.6.tar.gz
sudo mv hadoop-3.3.6 /usr/local/hadoop
```

Set environment variables in your `~/.bashrc` or `~/.profile`:

```wp-block-code
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
```

## Running Multiple Versions Side by Side

If you need to test against multiple Hadoop versions, install each in a separate directory and switch using environment variables:

```wp-block-code
# Directory structure
/usr/local/hadoop-2.10.2/
/usr/local/hadoop-3.3.6/
/usr/local/hadoop-3.4.0/

# Switch function in ~/.bashrc
hadoop_use() {
    export HADOOP_HOME=/usr/local/hadoop-$1
    export PATH=$(echo $PATH | sed "s|/usr/local/hadoop[^:]*||g"):$HADOOP_HOME/bin:$HADOOP_HOME/sbin
}

# Usage
hadoop_use 3.3.6
hadoop version
```

## Docker for Quick Testing

For testing without a full install, use Docker images with specific Hadoop versions:

```wp-block-code
# Pull a specific version
docker pull apache/hadoop:3.3.6

# Run a pseudo-distributed cluster
docker run -it apache/hadoop:3.3.6 bash
```

Community-maintained images are also available with full cluster setups for integration testing.

## Compatibility Notes

When choosing an older Hadoop version, consider:

- **Java version:** Hadoop 2.x requires Java 7 or 8. Hadoop 3.x supports Java 8 and 11. Hadoop 3.3+ supports Java 17.
- **API changes:** Some APIs were deprecated and removed between major versions. Check the release notes for breaking changes.
- **Security patches:** Older versions may have unpatched vulnerabilities. Use the latest patch release within a minor version (e.g., 2.10.2 rather than 2.10.0).
- **Configuration differences:** Hadoop 3.x changed several configuration parameter names from 2.x. Check the migration guide when upgrading.

## Cloudera and Hortonworks Distributions

If you need a specific CDP, CDH, or HDP version, check the vendor archives:

- Cloudera: `https://archive.cloudera.com/`
- Hortonworks (now part of Cloudera): archived under Cloudera’s repositories

These distributions bundle Hadoop with specific versions of Spark, Hive, HBase, and other ecosystem components that have been tested together.

## Using Maven with Specific Hadoop Versions

If you’re compiling Java applications against a specific Hadoop version, specify it in your `pom.xml`:

```wp-block-code
<properties>
    <hadoop.version>3.3.6</hadoop.version>
</properties>

<dependencies>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-common</artifactId>
        <version>${hadoop.version}</version>
    </dependency>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-hdfs</artifactId>
        <version>${hadoop.version}</version>
    </dependency>
    <dependency>
        <groupId>org.apache.hadoop</groupId>
        <artifactId>hadoop-mapreduce-client-core</artifactId>
        <version>${hadoop.version}</version>
    </dependency>
</dependencies>
```

For Hadoop 2.x, use `hadoop-common` and `hadoop-hdfs` artifacts. For Hadoop 1.x, the artifact was simply `hadoop-core`.

When testing against multiple versions, use Maven profiles to switch:

```wp-block-code
<profiles>
    <profile>
        <id>hadoop2</id>
        <properties><hadoop.version>2.10.2</hadoop.version></properties>
    </profile>
    <profile>
        <id>hadoop3</id>
        <properties><hadoop.version>3.3.6</hadoop.version></properties>
    </profile>
</profiles>
```

Build with: `mvn clean package -Phadoop3`

## Running Local Test Clusters

For development and testing, run Hadoop locally in pseudo-distributed mode:

```wp-block-code
# Configure etc/hadoop/core-site.xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>

# Configure etc/hadoop/hdfs-site.xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>

# Format the namenode and start
bin/hdfs namenode -format
sbin/start-dfs.sh
sbin/start-yarn.sh
```

Verify the cluster is running:

```wp-block-code
jps  # Should show NameNode, DataNode, ResourceManager, NodeManager

# Web UI
# NameNode: http://localhost:9870 (Hadoop 3.x) or http://localhost:50070 (Hadoop 2.x)
# ResourceManager: http://localhost:8088
```

This pseudo-distributed setup mimics a full cluster on a single machine, making it easy to test against specific Hadoop versions without provisioning hardware.
