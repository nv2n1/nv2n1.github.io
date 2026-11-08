---
title: "Safely Stopping Stray HDFS DataNode Processes on Multiple Nodes"
date: 2018-03-24 11:49:22 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-manually-kill-hdfs-datanodes/
---

When `stop-dfs.sh` fails to cleanly terminate DataNode processes, you’re left with orphaned Java processes consuming resources and potentially causing cluster issues. This happens most often after ungraceful cluster shutdowns or when the standard stop script encounters communication problems with specific nodes.

## Understanding the Problem

The typical symptom is `stop-dfs.sh` reporting that certain nodes have no DataNode to stop, despite DataNode processes still running:

    hdfs-node-000208: no datanode to stop

This occurs because the NameNode can’t communicate with the DataNode (network issues, hung process, or misconfiguration), so the graceful shutdown protocol never reaches that node. The Java process persists orphaned on the filesystem.

## Quick Single-Node Approach

For a single node, use `jps` to identify DataNode PIDs, then kill them directly:

``` bash
jps | grep DataNode | awk '{print $1}' | xargs kill -9
```

Breaking this down:

- `jps` lists all running Java processes with their PIDs
- `grep DataNode` filters for DataNode processes only
- `awk '{print $1}'` extracts just the PID (column 1)
- `xargs kill -9` forcefully terminates each PID

## Mass Kill Across Multiple Nodes

For clusters with dozens or hundreds of nodes, automate the process across your cluster. This script iterates through your node list and kills DataNodes everywhere:

``` bash
for node in $(cat /etc/hadoop/conf/workers); do 
  echo "Processing $node..."
  ssh "$node" 'jps | grep DataNode | awk "{print \$1}" | xargs -r kill -9' 2>/dev/null
done
```

Key improvements over older approaches:

- Uses `workers` file (standard in modern Hadoop distributions) instead of deprecated `slaves` file
- Uses `awk` instead of `cut` for cleaner field extraction
- Uses `-r` flag with `xargs` (safer than `--no-run-if-empty`, and more portable)
- Adds error suppression for nodes that may be unreachable
- Properly quotes variables to handle node names with special characters

## More Sophisticated Bulk Approach

For large clusters, parallelize the operations to complete faster:

``` bash
cat /etc/hadoop/conf/workers | while read node; do
  (
    echo "Killing DataNodes on $node..."
    ssh -o ConnectTimeout=5 -o BatchMode=yes "$node" \
      'jps | grep DataNode | awk "{print \$1}" | xargs -r kill -9' && \
      echo "$node: success" || echo "$node: failed or timeout"
  ) &

  # Limit parallel SSH connections to avoid overwhelming the network
  if (( $(jobs -r -p | wc -l) >= 10 )); then
    wait -n
  fi
done
wait
```

This runs up to 10 concurrent SSH sessions, which is reasonable for most clusters. Adjust the `10` based on your cluster size and network capacity.

## Verification

After killing processes, verify they’re gone:

``` bash
for node in $(cat /etc/hadoop/conf/workers); do
  ssh "$node" 'jps | grep DataNode' && echo "$node: STILL RUNNING (manual check needed)" || echo "$node: clean"
done
```

## Prevention

To avoid this situation in production:

- Always use `hdfs dfsadmin -shutdownDatanode <node> CANCEL` to gracefully drain a node before restarting it
- Configure appropriate timeouts in `hdfs-site.xml` (dfs.datanode.ipc.address, dfs.datanode.socket.write.timeout)
- Monitor DataNode health regularly with `hdfs dfsadmin -report`
- Use `systemctl` or your service manager to cleanly restart HDFS daemons instead of killing processes manually when possible

## When to Use `-9` vs `-15`

The scripts above use `kill -9` (SIGKILL) for certainty, but understand the trade-offs:

- `kill -15` (SIGTERM) gives the process a chance to shut down gracefully, but may hang indefinitely on a stuck process
- `kill -9` terminates immediately, but DataNode may not have flushed buffers or closed block replicas cleanly
- For stray processes that `stop-dfs.sh` couldn’t reach, `-9` is justified since graceful shutdown already failed
