---
title: "Configuring Heap Size for Hadoop NameNode, DataNode, and YARN"
date: 2018-03-24 11:43:14 +0000
modified: 2026-04-12 16:06:23 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /making-hadoop-java-process-heap-larger/
---

When running Hadoop on systems with substantial memory, the default 1GB heap size is often inadequate. If you check running processes with `ps aux` and see `-Xmx1000m`, you’re working with the default configuration that doesn’t scale to modern hardware.

## Understanding Hadoop Heap Configuration

Hadoop’s Java process memory is controlled by environment variables set in configuration files. The three main components that benefit from heap tuning are:

- **NameNode**: manages the file system namespace
- **DataNode**: handles block storage and I/O operations
- **YARN ResourceManager/NodeManager**: manages cluster resources and container allocation

Each component has its own heap settings and can be tuned independently.

## Configuring YARN Heap Size

Edit `$HADOOP_CONF_DIR/yarn-env.sh` (typically `/etc/hadoop/conf/` or your custom config path):

``` bash
# Uncomment and set the ResourceManager/NodeManager heap
export YARN_HEAPSIZE=4096

# For ResourceManager specifically (if you need different sizing)
export YARN_RESOURCEMANAGER_HEAPSIZE=8192

# For NodeManager specifically
export YARN_NODEMANAGER_HEAPSIZE=4096
```

## Configuring HDFS Heap Size

Edit `$HADOOP_CONF_DIR/hadoop-env.sh`:

``` bash
# General HDFS heap setting (applies to NameNode, DataNode, Secondary NameNode)
export HADOOP_HEAPSIZE=4096

# NameNode specific heap (recommended for large clusters)
export NAMENODE_HEAPSIZE=8192

# DataNode specific heap (typically smaller than NameNode)
export DATANODE_HEAPSIZE=2048

# Secondary NameNode heap
export SECONDARY_NAMENODE_HEAPSIZE=4096
```

## Sizing Recommendations

For a 32GB node, consider these starting points:

- **NameNode** (on dedicated master): 8–16GB depending on namespace size (typically 1-2KB per file)
- **DataNode**: 2–4GB (mostly for caching and block management)
- **YARN ResourceManager**: 4–8GB for large clusters (\>100 nodes)
- **YARN NodeManager**: 2–4GB (scale with number of containers)

Never allocate all available memory to Java heaps—reserve 20–30% for OS, buffers, and other processes.

## Applying Changes

After editing the configuration files, restart the relevant services:

``` bash
# For YARN
$HADOOP_HOME/sbin/stop-yarn.sh
$HADOOP_HOME/sbin/start-yarn.sh

# For HDFS
$HADOOP_HOME/sbin/stop-dfs.sh
$HADOOP_HOME/sbin/start-dfs.sh
```

Verify the new heap size is active:

``` bash
ps aux | grep java | grep -E "NameNode|DataNode|ResourceManager"
```

You should now see updated `-Xmx` values in the process arguments.

## Advanced Tuning with JVM Options

For finer control, add JVM parameters to `HADOOP_NAMENODE_OPTS` and similar variables in `hadoop-env.sh`:

``` bash
export NAMENODE_OPTS="-Xmx16g -Xms16g -XX:+UseG1GC -XX:MaxGCPauseMillis=50"
export DATANODE_OPTS="-Xmx4g -Xms4g -XX:+UseG1GC"
```

Setting `-Xms` (initial heap) equal to `-Xmx` (maximum heap) prevents heap resizing and improves predictability on large machines.

## Monitoring Heap Usage

Track actual heap consumption to right-size your allocations:

``` bash
# Check NameNode heap usage via JMX
jconsole localhost:9010

# Or use logs from $HADOOP_LOG_DIR/hadoop-*-namenode-*.log
```

Adjust settings based on observed peaks, not theoretical maximums.

## Hadoop Cluster Health Monitoring

Regular health checks prevent small issues from becoming cluster-wide problems. Monitor HDFS capacity utilization and ensure DataNode heartbeats are current. Watch for under-replicated blocks which indicate potential data loss risk.

Key monitoring commands include hdfs dfsadmin -report for cluster overview, yarn node -list for NodeManager status, and hdfs fsck / for filesystem consistency checks. Set up automated alerts for critical metrics like disk usage above 85% or failed NodeManagers.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
