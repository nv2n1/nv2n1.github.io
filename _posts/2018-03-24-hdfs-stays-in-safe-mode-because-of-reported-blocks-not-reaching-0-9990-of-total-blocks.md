---
title: "Recovering HDFS from Safe Mode After DataNode Failures"
date: 2018-03-24 11:46:19 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/hdfs-stays-in-safe-mode-because-of-reported-blocks-not-reaching-0-9990-of-total-blocks/
---

When a NameNode restarts, it enters safe mode to rebuild its understanding of block-to-DataNode mappings. If DataNodes don’t report their blocks quickly enough or some don’t come back online, the NameNode may stay stuck in safe mode with a message like:

    The reported blocks 1968810 needs additional 5071 blocks to reach the 
    threshold 0.9990 of total blocks 1975856. Safe mode will be turned off 
    automatically.

## Why HDFS Gets Stuck in Safe Mode

The NameNode’s startup sequence works like this:

1.  **Reads FSImage and edits log** — recovers all known files and block metadata from persistent storage
2.  **Waits for Initial Block Reports** — each DataNode reports which blocks it holds
3.  **Checks the threshold** — verifies that at least `dfs.namenode.safemode.threshold-pct` (default 0.9990) of known blocks have been reported by at least `dfs.namenode.replication.min` (default 1) DataNode

Once the threshold is met, the NameNode waits an additional `dfs.namenode.safemode.extension` seconds (default 30), then exits safe mode and begins replication operations.

If the threshold isn’t reached, the NameNode intentionally stays in safe mode. This is safety-by-design: Hadoop won’t automatically delete blocks or trigger aggressive re-replication when DataNodes are missing or offline. A human should investigate first — entire racks might be down, network issues could exist, or disk corruption may have occurred.

## Diagnosing the Problem

Check the NameNode web UI (default port 9870) or logs for details:

``` bash
tail -f /var/log/hadoop/hdfs/namenode.log | grep -i "safe mode"
```

Common causes:

- **DataNodes still starting** — legitimate, just need to wait longer
- **DataNode disk problems** — check DataNode logs for I/O errors
- **Network partitioning** — DataNodes can’t reach the NameNode
- **Misconfigured replication factor** — blocks expecting more replicas than available DataNodes
- **Missing DataNodes** — nodes that held blocks are permanently offline

## Safe Ways to Exit Safe Mode

### Option 1: Wait (Recommended First Step)

If DataNodes are starting up, patience often works. Monitor progress:

``` bash
hdfs dfsadmin -safemode get
```

This returns a status like `Safe mode is ON` with details. Check back periodically.

### Option 2: Lower the Threshold Temporarily

If you’re confident DataNodes are healthy but just slow to report, adjust the threshold in `hdfs-site.xml`:

``` xml
<property>
  <name>dfs.namenode.safemode.threshold-pct</name>
  <value>0.9</value>
</property>
```

Then restart the NameNode. Only do this if you understand the operational risk.

### Option 3: Force Exit Safe Mode

**Only use this if you’ve verified the situation and are willing to accept the consequences** (potential data loss from aggressive re-replication or block deletion):

``` bash
hdfs dfsadmin -safemode leave
```

## After Exiting Safe Mode

Once safe mode is off, check for corrupted or missing blocks:

``` bash
hdfs fsck / -files -blocks
```

For a detailed report with specific problem locations:

``` bash
hdfs fsck / -files -blocks -locations -racks
```

If you find corrupted files and want to remove them (ensure you have backups):

``` bash
hdfs fsck / -delete
```

Or to move corrupted files to `/lost+found` for manual inspection first:

``` bash
hdfs fsck / -move
```

## Prevention and Best Practices

- **Monitor DataNode health** regularly; don’t wait for restart failures

- **Increase safe mode timeout** if you have slow-starting DataNodes:

  ``` xml
  <property>
  <name>dfs.namenode.safemode.extension</name>
  <value>60000</value>
  </property>
  ```

- **Keep adequate replication** — if you only have 2 DataNodes but configured replication factor 3, you’ll struggle with safe mode

- **Review logs proactively** — NameNode and DataNode logs contain early warnings about connectivity or disk issues

- **Test failover procedures** in non-production environments first to understand behavior

Safe mode exists to prevent data loss. Respect it, investigate the root cause, and only force exit when you’re absolutely certain of your cluster’s state.
