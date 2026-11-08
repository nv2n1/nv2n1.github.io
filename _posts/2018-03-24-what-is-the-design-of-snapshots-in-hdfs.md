---
title: "HDFS Snapshots: Architecture and Implementation Details"
date: 2018-03-24 11:43:43 +0000
modified: 2026-04-11 15:58:35 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /what-is-the-design-of-snapshots-in-hdfs/
---

HDFS snapshots provide a way to create read-only point-in-time copies of the filesystem or specific directories without duplicating data. Understanding their design helps you implement efficient backup strategies and recover from accidental deletions in production clusters.

## How HDFS Snapshots Work

Snapshots in HDFS use copy-on-write semantics to avoid duplicating data. When you create a snapshot, HDFS records the current state of the filesystem tree without copying actual blocks. If a file or block is modified after the snapshot is taken, the system preserves the original version for the snapshot while allowing writes to proceed on the active filesystem.

The key design principle is that snapshots are immutable once created. They cannot be deleted if there are active references to them, and the snapshot tree itself cannot be modified. This immutability guarantee simplifies consistency requirements across the cluster.

## Snapshot Storage and Metadata

The NameNode stores snapshot metadata in memory, tracking:

- Snapshot IDs and timestamps
- Directory tree state at snapshot creation time
- Inode references for files and directories included in the snapshot
- Block references to ensure blocks aren’t prematurely deleted

This metadata overhead is proportional to the number of snapshots and the filesystem size, so monitor your NameNode heap usage if you maintain many concurrent snapshots.

## Creating and Managing Snapshots

First, enable snapshots on a directory:

``` bash
hdfs dfsadmin -allowSnapshot /path/to/directory
```

Then create a snapshot:

``` bash
hdfs dfs -createSnapshot /path/to/directory snapshot-name
```

List existing snapshots:

``` bash
hdfs dfs -lsSnapshots /path/to/directory
```

Access snapshot contents through the `.snapshot` hidden directory:

``` bash
hdfs dfs -ls /path/to/directory/.snapshot/snapshot-name
```

Delete a snapshot when no longer needed:

``` bash
hdfs dfs -deleteSnapshot /path/to/directory snapshot-name
```

## Practical Considerations

**Retention policies**: Establish a snapshot retention schedule. Keep recent snapshots for quick recovery, but delete old ones to reduce NameNode memory pressure. Many organizations keep daily snapshots for 7-30 days depending on RPO requirements.

**Snapshot-diff reporting**: Use the `snapshotDiff` command to compare snapshots and identify what changed:

``` bash
hdfs snapshotDiff /path/to/directory snapshot1 snapshot2
```

This is valuable for understanding filesystem mutations between recovery points.

**Backup integration**: Snapshots work well with incremental backup tools. After creating a snapshot, you can back up only the blocks created since the previous snapshot, reducing bandwidth usage.

**Performance impact**: Creating snapshots is fast (metadata-only operation), but the presence of many snapshots can slow NameNode operations slightly due to increased metadata processing. Each snapshot holds a reference to inodes, preventing garbage collection of deleted files.

**Block deletion**: Blocks referenced by any snapshot cannot be deleted, even if the live filesystem no longer uses them. This can cause disk space to be held longer than expected. Monitor block storage carefully in environments with long snapshot retention.

## Limitations and Constraints

Snapshots don’t work with encryption zones in the same way as regular directories — verify your security model when combining these features. Additionally, snapshots provide point-in-time recovery at the filesystem level but don’t guarantee application-level consistency for databases or other stateful services.

You cannot take snapshots of snapshots, and the `.snapshot` directory hierarchy has specific access restrictions. Regular users can only view snapshots they have permission to access based on the underlying directory permissions.
