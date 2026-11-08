---
title: "Forcing HDFS Metadata Checkpoints"
date: 2018-03-24 11:54:21 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-force-a-checkpointing-of-metadata-in-hdfs/
---

The NameNode in HDFS maintains the filesystem namespace in memory. The Secondary NameNode (or Checkpoint Node in HA setups) periodically merges the namespace image (fsimage) with the edit logs to create a new checkpoint. Understanding how to force this process is essential for cluster maintenance and recovery operations.

## How Checkpointing Works

The checkpoint process combines the fsimage and edit logs into a new fsimage, then the Secondary NameNode uploads it back to the primary NameNode. This reduces startup time and edit log size, preventing unbounded growth that could cause serious performance issues.

By default, checkpointing occurs every 3600 seconds (1 hour) or when the edit logs accumulate 1 million transactions, whichever comes first. You can adjust these via `hdfs-site.xml`:

``` xml
<property>
  <name>dfs.namenode.checkpoint.interval</name>
  <value>3600</value>
  <description>Seconds between checkpoints</description>
</property>

<property>
  <name>dfs.namenode.checkpoint.txns</name>
  <value>1000000</value>
  <description>Number of transactions before forcing checkpoint</description>
</property>
```

## Forcing a Checkpoint Manually

### Using the NameNode HTTP Interface

Access the NameNode web UI (typically `http://namenode-host:9870`) and navigate to **Utilities → Start Checkpoint**. This triggers an immediate checkpoint on the Secondary NameNode.

### Using the Command Line

The cleanest approach is the `hdfs dfsadmin` command:

``` bash
hdfs dfsadmin -saveNamespace
```

This initiates a checkpoint and saves the namespace. It’s a safe operation that won’t interrupt normal cluster operations.

For checking the current namespace state before forcing a checkpoint:

``` bash
hdfs dfsadmin -report
```

### Using the Secondary NameNode Directly

If you need to trigger checkpointing from the Secondary NameNode host:

``` bash
hadoop secondarynamenode -checkpoint force
```

This forces an immediate checkpoint, useful when you need to ensure the fsimage is current before maintenance windows.

## Monitoring Checkpoint Progress

Watch the NameNode logs to verify checkpoint completion:

``` bash
tail -f /var/log/hadoop/hdfs/hadoop-hdfs-namenode-*.log | grep -i checkpoint
```

Look for messages indicating successful merge operations. On systemd-based systems, you can also use:

``` bash
journalctl -u hadoop-namenode -f | grep -i checkpoint
```

Check the Secondary NameNode logs similarly:

``` bash
tail -f /var/log/hadoop/hdfs/hadoop-hdfs-secondarynamenode-*.log
```

## High Availability Setups

In HA clusters with Zookeeper and multiple NameNodes, checkpointing behavior differs. The Standby NameNode performs checkpoint duties. Force checkpointing with:

``` bash
hdfs haadmin -getServiceState nn1
hdfs dfsadmin -saveNamespace
```

Ensure you’re connecting to the active NameNode before running `saveNamespace`.

## Performance Considerations

Forcing frequent checkpoints on very large namespaces (millions of files) can temporarily increase I/O and CPU usage. Check edit log size first:

``` bash
ls -lh /var/lib/hadoop-hdfs/dfs/name/current/
```

If edit logs exceed 500MB, a checkpoint becomes urgent for recovery speed. Perform it during low-traffic periods if the cluster is production.

## Common Issues

**“Checkpoint already in progress”** — Wait for the previous checkpoint to complete. Check Secondary NameNode status in the web UI.

**Slow checkpoint on large clusters** — This is normal. The Secondary NameNode needs time to download, merge, and re-upload the fsimage. For multi-terabyte namespaces, expect 5-15 minutes.

**Edit logs not shrinking after checkpoint** — Verify the Secondary NameNode successfully uploaded the new fsimage by checking its logs for “Upload successful” messages. If missing, check network connectivity and storage space on both NameNode and Secondary NameNode.

## Safe Practices

Always checkpoint before major maintenance:

- NameNode hardware upgrades
- Firmware updates on storage systems
- Planned cluster restarts

Never force checkpoints back-to-back—allow 30+ seconds between operations for proper fsimage rotation.
