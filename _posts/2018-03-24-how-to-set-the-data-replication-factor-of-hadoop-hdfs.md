---
title: "Configuring HDFS Replication: Cluster and Per-File Settings"
date: 2018-03-24 08:22:40 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-set-the-data-replication-factor-of-hadoop-hdfs/
---

The replication factor determines how many copies of each data block HDFS maintains across your cluster. The default is 3, which provides adequate fault tolerance for most deployments by surviving both node and rack failures simultaneously.

## Setting Cluster-Wide Default Replication

To set the default replication factor for all new files, add the `dfs.replication` property to `hdfs-site.xml`:

``` xml
<property>
    <name>dfs.replication</name>
    <value>2</value>
    <description>Default block replication factor.</description>
</property>
```

After modifying the file, reload the NameNode configuration without a full restart:

``` bash
hdfs dfsadmin -reconfig namenode properties
```

This approach (available in Hadoop 2.8+) applies the new factor to subsequently written files immediately without disrupting running jobs. If you’re on an older Hadoop version or prefer a clean restart, bounce the NameNode and DataNodes, but only during a maintenance window.

## Overriding Replication for Specific Files

Set replication for individual files or directories using `hdfs dfs -setrep`:

``` bash
hdfs dfs -setrep -R 2 /path/to/file
```

The `-R` flag applies the change recursively to all files within a directory. The NameNode marks blocks for replication or de-replication based on the new factor. New blocks written to the file immediately use the specified factor; existing blocks rebalance gradually to avoid cluster congestion.

For a one-time operation without modifying config files:

``` bash
hdfs dfs -D dfs.replication=1 -put /local/file /hdfs/path
```

This is useful for bulk imports or temporary test data where you need a different replication factor just for that operation.

## Monitoring and Verifying Replication

Check the current replication status of files using `hdfs fsck`:

``` bash
hdfs fsck / -files -blocks -locations
```

This output shows each file’s block locations and replica count. Filter for specific files:

``` bash
hdfs fsck /user/data/ -files -blocks -locations | grep your-file
```

Alternatively, access the NameNode Web UI at `http://namenode-host:9870/dfshealth.html` to inspect individual files, block replicas, and DataNode health interactively.

Use `hdfs dfsadmin -report` to view overall cluster replication statistics:

``` bash
hdfs dfsadmin -report
```

This shows live and dead DataNodes, used and available capacity, and block under-replication counts.

## Replication Constraints and Considerations

**Bounds and validation:** HDFS enforces minimum and maximum replication constraints. Setting `dfs.replication` higher than your number of DataNodes means HDFS replicates to all available nodes but cannot reach the target factor—the NameNode logs warnings. A value of 0 is invalid; HDFS requires at least 1 replica per block.

**Rack topology:** If you’ve configured rack awareness (via `net.topology.script.file.name` or cloud provider integration), HDFS places replicas across racks by default. With a replication factor of 3, the standard placement is 2 replicas on one rack and 1 on another, surviving both node and rack outages.

**Write latency and disk usage:** Increasing replication raises write latency and multiplies disk consumption. Decreasing it saves space but reduces fault tolerance. Factor in your SLA requirements, available storage, and network bandwidth before adjusting.

**De-replication timing:** Lowering the replication factor doesn’t immediately delete excess replicas. The NameNode instructs DataNodes to remove them gradually (controlled by `dfs.namenode.replication.interval` and `dfs.namenode.replication.pending.timeout.sec`) to avoid overwhelming the cluster with delete operations. Use `hdfs dfsadmin -report` to track under-replicated and over-replicated blocks during the transition.

## Production Workflow

For live clusters, adjust replication without downtime:

1.  Update `hdfs-site.xml` on the NameNode
2.  Reload configuration: `hdfs dfsadmin -reconfig namenode properties`
3.  New files immediately use the new factor; existing files rebalance gradually
4.  Monitor with `hdfs dfsadmin -report` until under-replication resolves
5.  Update other NameNodes in HA setups and reload them as well

This approach keeps your cluster running while transitioning to a new replication strategy.
