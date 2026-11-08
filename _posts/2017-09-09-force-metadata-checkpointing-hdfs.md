---
title: "HDFS NameNode Metadata Checkpointing: Resolving Sync Issues"
date: 2017-09-09 04:37:04 +0000
author: "Eric Ma"
layout: post
categories: [systems-architecture]
canonical: /force-metadata-checkpointing-hdfs/
---

The Secondary NameNode periodically merges the fsimage and edits log files to keep the edits log manageable and consolidate metadata. When this checkpointing fails, you’ll see errors like:

    ERROR org.apache.hadoop.hdfs.server.namenode.SecondaryNameNode: Exception in doCheckpoint
    java.io.IOException: Inconsistent checkpoint fields.

This typically indicates a mismatch between the NameNode and Secondary NameNode metadata states, often from unclean shutdowns or network interruptions during the checkpoint process. Forcing a manual checkpoint can resolve the issue and restore consistency.

## Prerequisites

You need HDFS admin permissions to run these commands. Execute them as the HDFS super user (typically the `hdfs` user running the NameNode daemon).

## Step 1: Save Latest Metadata to fsimage

Put the NameNode in safe mode and flush pending edits:

``` bash
hdfs dfsadmin -safemode enter
hdfs dfsadmin -safemode get
hdfs dfsadmin -saveNamespace
hdfs dfsadmin -safemode leave
```

The `-saveNamespace` command writes all pending edits into the fsimage file while in safe mode. This creates a clean starting point for the Secondary NameNode and prevents further edits from being added during the checkpoint process.

Verify safe mode is exited:

``` bash
hdfs dfsadmin -safemode get
```

You should see output like `Safe mode is OFF`.

## Step 2: Clean Secondary NameNode State

Stop the Secondary NameNode service:

``` bash
sudo systemctl stop hadoop-hdfs-secondarynamenode
```

For older Hadoop deployments without systemd, use:

``` bash
sudo $HADOOP_HOME/sbin/hadoop-daemon.sh stop secondarynamenode
```

Verify the process has stopped:

``` bash
jps | grep SecondaryNameNode
```

Identify the checkpoint directory (or directories if multiple are configured):

``` bash
hdfs getconf -confKey dfs.namenode.checkpoint.dir
```

Example output:

    file:///var/lib/hadoop-hdfs/cache/hdfs/dfs/namesecondary

Back up the current checkpoint directory so it can be rebuilt from scratch:

``` bash
sudo mv /var/lib/hadoop-hdfs/cache/hdfs/dfs/namesecondary /var/lib/hadoop-hdfs/cache/hdfs/dfs/namesecondary.old
sudo mkdir -p /var/lib/hadoop-hdfs/cache/hdfs/dfs/namesecondary
sudo chown hdfs:hadoop /var/lib/hadoop-hdfs/cache/hdfs/dfs/namesecondary
sudo chmod 700 /var/lib/hadoop-hdfs/cache/hdfs/dfs/namesecondary
```

If multiple checkpoint directories are configured (comma-separated in `dfs.namenode.checkpoint.dir`), clean all of them.

## Step 3: Force Manual Checkpoint

Trigger an immediate checkpoint on the Secondary NameNode:

``` bash
hdfs secondarynamenode -checkpoint force
```

This forces a checkpoint regardless of the configured `dfs.namenode.checkpoint.period` or `dfs.namenode.checkpoint.txns` thresholds. The command will:

1.  Contact the NameNode and retrieve the current fsimage and edits log
2.  Merge them into a new fsimage
3.  Return the merged fsimage to the NameNode for validation

The command may take several minutes for large clusters. Monitor progress in the logs.

## Step 4: Restart Secondary NameNode

Once the manual checkpoint completes, start the Secondary NameNode service:

``` bash
sudo systemctl start hadoop-hdfs-secondarynamenode
```

Or with older deployments:

``` bash
sudo $HADOOP_HOME/sbin/hadoop-daemon.sh start secondarynamenode
```

## Verification

Check the Secondary NameNode logs for successful completion:

``` bash
tail -f /var/log/hadoop-hdfs/hadoop-hdfs-secondarynamenode-*.log
```

Look for messages like:

    Checkpoint done. New Image size: X bytes

You can also verify the checkpoint on the NameNode side:

``` bash
hdfs dfsadmin -report | grep "Last checkpoint"
```

The timestamp should reflect the time you forced the checkpoint.

## Troubleshooting

**Checkpoint fails with namespace ID mismatch:**

This indicates the NameNode and Secondary NameNode have diverged significantly. Beyond the steps above:

- Verify network connectivity between the NameNode and Secondary NameNode hosts
- Check for clock skew: `ntpstat` on both hosts should show synchronized time
- Ensure no concurrent HDFS rolling upgrades are in progress
- Verify the NameNode and Secondary NameNode are running compatible Hadoop versions

**Secondary NameNode hangs or takes excessive time:**

Initial checkpointing after a long downtime can take hours on large clusters with substantial edits logs. Monitor progress via:

``` bash
tail -f /var/log/hadoop-hdfs/hadoop-hdfs-secondarynamenode-*.log | grep -i "loading\|merging\|saving"
```

Check the Secondary NameNode web UI (default port 50090) to see the number of transactions processed.

**“Cannot get image” or “No valid image found” errors:**

This suggests the fsimage on the NameNode is corrupted. Check the NameNode’s metadata directory:

``` bash
ls -lh /var/lib/hadoop-hdfs/dfs/name/current/
```

If the fsimage is missing or corrupted, you may need to restore from backup or force format. Consult your HDFS backup strategy before proceeding.

**Large edits log slowing checkpoints:**

If the NameNode’s edits log consistently grows beyond 1GB, adjust the checkpoint frequency in `hdfs-site.xml`:

``` xml
<property>
  <name>dfs.namenode.checkpoint.period</name>
  <value>3600</value>  <!-- seconds, default is 3600 (1 hour) -->
</property>
```

Or trigger checkpoints based on transaction count instead:

``` xml
<property>
  <name>dfs.namenode.checkpoint.txns</name>
  <value>1000000</value>  <!-- trigger every 1 million transactions -->
</property>
```

Restart the Secondary NameNode to apply changes.
