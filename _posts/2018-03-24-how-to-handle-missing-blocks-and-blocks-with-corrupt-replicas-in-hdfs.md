---
title: "Diagnosing and Repairing Corrupt HDFS Blocks"
date: 2018-03-24 11:47:07 +0000
author: "Eric Ma"
layout: post
categories: [systems-architecture]
canonical: /how-to-handle-missing-blocks-and-blocks-with-corrupt-replicas-in-hdfs/
---

When you see output like this from `hdfs dfsadmin -report`, you need to understand what each metric means and how to respond:

    Under replicated blocks: 139016
    Blocks with corrupt replicas: 9
    Missing blocks: 0

Understanding block states in HDFS is essential for cluster health. The distinction between these categories determines how urgent your response needs to be.

## Block Categories and What They Mean

**Corrupt replica blocks** contain at least one replica that failed checksum validation, but the block also has at least one healthy replica available. Data isn’t currently lost, but redundancy is reduced—if another replica fails, you lose data. These blocks should trigger investigation but aren’t emergencies.

**Missing blocks** occur when none of a block’s replicas are accessible or valid. All replicas are either unavailable (DataNodes down), corrupt, or deleted. Missing blocks mean data is currently inaccessible and require immediate action.

**Under-replicated blocks** have fewer healthy replicas than the configured replication factor. HDFS automatically re-replicates these over time, but if the process stalls, it indicates underlying issues.

## Identifying Affected Files

The first step is always to determine which files are affected. Use `hdfs fsck` to scan the cluster:

``` bash
hdfs fsck / -files -blocks -locations
```

For a summary of problem blocks:

``` bash
hdfs fsck / -list-corruptfileblocks
```

To focus on a specific directory:

``` bash
hdfs fsck /user/hive/warehouse -files -blocks
```

The output shows block IDs, replica locations, and which replicas are corrupt. Note the pool IDs and DataNode addresses—you’ll need these.

## Root Causes and Diagnostics

**Hardware or filesystem failures on DataNodes** are the most common cause. Check DataNode logs:

``` bash
tail -f /var/log/hadoop/hdfs/datanode.log
```

Look for I/O errors, disk full warnings, or checksum failures. Run `dmesg` on affected DataNodes to catch kernel-level issues.

**Offline DataNodes holding replicas.** If a DataNode was down during maintenance or crashed, its blocks become unavailable. Check DataNode status:

``` bash
hdfs dfsadmin -report | grep -A 10 "Dead datanodes"
```

Bringing the DataNode back online often resolves missing blocks automatically as the NameNode re-replicates.

**Single replica files.** Files with replication factor 1 cannot recover from a lost replica. Once the block is gone, it’s gone. Identify these:

``` bash
hdfs fsck / -files -blocks | grep "Replica count: 1"
```

**Network issues causing false corruption detection.** Transient network failures during block transfers can trigger false corruption flags. Monitor DataNode-to-DataNode communication.

## Recovery Procedures

**For corrupt replica blocks with healthy copies:**

Delete the corrupt file and restore from backup if available:

``` bash
hdfs dfs -rm /path/to/corrupt/file
```

Alternatively, wait for HDFS to automatically purge the corrupt replicas (usually within 24 hours by default, controlled by `dfs.blockreport.intervalMsec`).

**For missing blocks from active files:**

First, bring any offline DataNodes back online:

``` bash
systemctl start hadoop-hdfs-datanode
```

Wait 10-15 minutes for the DataNode to heartbeat and re-register its blocks. Check progress:

``` bash
hdfs fsck / -list-corruptfileblocks
```

If the DataNode cannot come back online, the data is likely unrecoverable. Delete the file:

``` bash
hdfs dfs -rm -r /path/to/file
```

And restore from a backup.

**For files with replication factor 1:**

These have no redundancy. Increase the replication factor immediately:

``` bash
hdfs dfs -setrep -w 3 /path/to/file
```

The `-w` flag waits for replication to complete. Once replication finishes, the block is safe.

## Prevention and Best Practices

**Set minimum replication to 3** for any critical data. Update `hdfs-site.xml`:

``` xml
<property>
  <name>dfs.replication</name>
  <value>3</value>
</property>
```

**Monitor proactively.** Check `hdfs fsck` output weekly and set up alerts on DataNode logs:

``` bash
hdfs fsck / -list-corruptfileblocks | mail -s "HDFS Corruption Alert" admin@example.com
```

**Maintain healthy DataNode disk space.** Corrupt blocks often result from full or nearly-full disks. Keep at least 10% free:

``` bash
hdfs dfsadmin -report | grep "Configured Capacity"
```

**Replace failing hardware immediately.** Don’t let degraded nodes sit in your cluster. If a DataNode is showing signs of disk failure, decomission it and replace the hardware.

**Run regular backups.** No amount of replication replaces actual backups. Use distcp or external tools to snapshot critical datasets.

## When to Escalate

If missing or corrupt blocks persist after bringing DataNodes online, involve your storage team. Run a full filesystem check in safe mode for deeper diagnosis, though be warned this locks the cluster:

``` bash
hdfs dfsadmin -safemode enter
hdfs fsck / -list-corruptfileblocks
hdfs dfsadmin -safemode leave
```

Only use this as a last resort for a few files, not routine checks.
