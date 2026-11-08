---
title: "Configuring HDFS Replication Factors by Directory"
date: 2018-03-24 11:45:26 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-set-replication-factors-for-hdfs-directories/
---

HDFS doesn’t natively support directory-level replication factor inheritance. Even if you set a specific replication factor on a directory and its files, new files created in that directory will default to the cluster’s global `dfs.replication` setting (typically 3).

This limitation can complicate multi-tier storage strategies where you want temporary or low-priority data on fewer replicas to save space, while keeping critical data at higher replication.

## Setting Replication Factors on Existing Files

To set the replication factor for existing files in a directory, use the `hdfs dfs -setrep` command:

``` bash
hdfs dfs -setrep -w 2 /tmp/
```

The `-w` flag waits for the replication to complete before returning. Without it, the command returns immediately after the request is queued. For large directories, this can take considerable time depending on cluster load and available bandwidth.

To set replication recursively on a directory tree:

``` bash
hdfs dfs -setrep -R -w 2 /tmp/
```

## The Problem: New Files Don’t Inherit Directory Settings

Any newly written files to `/tmp/` will still use the default cluster replication factor, not the 2 replicas you set on existing files. This is a known limitation documented in <a href="https://issues.apache.org/jira/browse/HDFS-199" rel="nofollow noopener" target="_blank">HDFS-199</a>, which remains unresolved.

## Workaround: Daemon Script for Continuous Enforcement

If you need to enforce lower replication on a directory, run a periodic daemon to adjust new files:

``` bash
#!/bin/bash
while true; do
    hdfs dfs -setrep -R 2 /tmp/
    sleep 300
done
```

Schedule this as a cron job or systemd service instead of a manual while loop. A 5-minute interval balances overhead with timeliness. Adjust the sleep duration based on your write rate and tolerance for temporary over-replication.

**Systemd service approach:**

Create `/etc/systemd/system/hdfs-replication-enforce.service`:

``` ini
[Unit]
Description=Enforce HDFS Replication Factor for /tmp/
After=network.target
Wants=hdfs-datanode.service

[Service]
Type=simple
User=hdfs
ExecStart=/usr/local/bin/enforce-hdfs-replication.sh
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Then create `/usr/local/bin/enforce-hdfs-replication.sh`:

``` bash
#!/bin/bash
set -e

REPLICATION_FACTOR=2
TARGET_DIR=/tmp/
CHECK_INTERVAL=300

while true; do
    hdfs dfs -setrep -R "${REPLICATION_FACTOR}" "${TARGET_DIR}" 2>&1 | logger -t hdfs-replication
    sleep "${CHECK_INTERVAL}"
done
```

Make it executable and enable the service:

``` bash
chmod +x /usr/local/bin/enforce-hdfs-replication.sh
systemctl enable hdfs-replication-enforce.service
systemctl start hdfs-replication-enforce.service
```

## Better Alternatives

**1. Application-level control:** Have clients explicitly set replication when writing files via the Hadoop API or Spark configs:

``` python
# PySpark example
df.write \
    .option("dfs.replication", "2") \
    .parquet("/tmp/data")
```

**2. HDFS erasure coding:** For archival or low-access directories, erasure coding (available since Hadoop 3.0) provides better space efficiency than multiple replicas:

``` bash
hdfs ec -setPolicy -policy RS-3-2-1024k /archive/
```

This uses 5 blocks (3 data + 2 parity) instead of 3 replicas, saving ~40% space while maintaining fault tolerance.

**3. Storage policies:** Use heterogeneous storage (SSD, HDD, archival) with storage policies to optimize placement without changing replication:

``` bash
hdfs storagepolicies -setPolicy -policy COLD -path /archive/
```

## Monitoring Replication Status

Check current replication of a directory:

``` bash
hdfs dfs -stat "%r" /tmp/
```

List all files with replication factors:

``` bash
hdfs dfs -ls -R /tmp/ | awk '{print $2, $NF}'
```

The first column is the replication factor, the second is the file path.

## Performance Considerations

Running `-setrep` on large directories is I/O intensive. Schedule enforcement during low-traffic windows if possible. Monitor NameNode logs for excessive replication task queuing:

``` bash
tail -f /var/log/hadoop/hdfs/namenode.log | grep "Replication"
```

For directories receiving constant writes, accept that some files will temporarily exceed your target replication factor until the enforcement script catches up.
