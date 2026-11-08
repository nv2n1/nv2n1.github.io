---
title: "Hadoop Port Reference Guide"
date: 2012-01-15 23:18:22 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/hadoop-default-ports/
---

Hadoop daemons communicate over specific TCP ports that you’ll need to know for cluster setup, firewall configuration, and application development. These ports are configurable but come with sensible defaults in Hadoop 3.x.

## HDFS Ports

| Service | Port | Configuration Property | Purpose |
|----|----|----|----|
| Namenode HTTP UI | 9870 | `dfs.namenode.http-address` | Web UI and metadata operations |
| Namenode HTTPS UI | 9871 | `dfs.namenode.https-address` | Secure web interface |
| Namenode IPC | 8020 | `fs.defaultFS` or `dfs.namenode.rpc-address` | Client-to-namenode communication |
| Secondary Namenode HTTP | 9868 | `dfs.namenode.secondary.http-address` | Checkpoint operations UI |
| Datanode HTTP UI | 9864 | `dfs.datanode.http.address` | Block operations and reports |
| Datanode IPC | 9866 | `dfs.datanode.ipc.address` | Namenode-to-datanode commands |
| Datanode Data Transfer | 9867 | `dfs.datanode.address` | Block data transfer between nodes |

## YARN Ports (Hadoop 2.x+)

| Service | Port | Configuration Property | Purpose |
|----|----|----|----|
| ResourceManager HTTP UI | 8088 | `yarn.resourcemanager.webapp.address` | Web UI for job monitoring |
| ResourceManager HTTPS UI | 8090 | `yarn.resourcemanager.webapp.https.address` | Secure web interface |
| ResourceManager IPC | 8032 | `yarn.resourcemanager.address` | Client submissions and heartbeats |
| NodeManager HTTP UI | 8042 | `yarn.nodemanager.webapp.address` | Per-node resource status |
| NodeManager IPC | 8040 | `yarn.nodemanager.address` | Heartbeat and container management |

## MapReduce Ports

| Service | Port | Configuration Property | Purpose |
|----|----|----|----|
| JobHistoryServer HTTP | 19888 | `mapreduce.jobhistory.address` | Job history UI and queries |
| JobHistoryServer IPC | 10020 | `mapreduce.jobhistory.webapp.address` | Client access to job history |

## Configuring Non-Default Ports

Edit `etc/hadoop/core-site.xml` for HDFS settings:

``` xml
<property>
  <name>fs.defaultFS</name>
  <value>hdfs://namenode.example.com:8020</value>
</property>
```

Edit `etc/hadoop/hdfs-site.xml` for datanode and namenode specific ports:

``` xml
<property>
  <name>dfs.namenode.http-address</name>
  <value>0.0.0.0:9870</value>
</property>
<property>
  <name>dfs.namenode.rpc-address</name>
  <value>namenode.example.com:8020</value>
</property>
<property>
  <name>dfs.datanode.address</name>
  <value>0.0.0.0:9867</value>
</property>
```

Edit `etc/hadoop/yarn-site.xml` for YARN resource manager ports:

``` xml
<property>
  <name>yarn.resourcemanager.address</name>
  <value>resourcemanager.example.com:8032</value>
</property>
<property>
  <name>yarn.resourcemanager.webapp.address</name>
  <value>0.0.0.0:8088</value>
</property>
```

## Firewall Configuration

When running Hadoop behind a firewall or NAT, expose these port ranges:

- **Clients to cluster**: 8020 (HDFS), 8032 (YARN RM)
- **Web UI access**: 9870 (Namenode), 8088 (ResourceManager), 19888 (Job History)
- **Cluster-internal communication**: 9866-9867 (Datanode), 8040 (NodeManager) — restrict to cluster subnet only

For production deployments, bind IPC ports to specific interfaces rather than `0.0.0.0`. Bind web UIs to `0.0.0.0` or a management network interface.

## Checking Open Ports

Verify which ports are listening on a Hadoop node:

``` bash
netstat -tlnp | grep -E ':(8020|8032|9870|9866|9867|8042|8040|8088|19888)'
```

Or with `ss` (preferred in modern Linux):

``` bash
ss -tlnp | grep -E ':(8020|8032|9870|9866|9867|8042|8040|8088|19888)'
```

Check HDFS connectivity from a client:

``` bash
hdfs dfs -ls hdfs://namenode.example.com:8020/
```

## High Availability and Federation Considerations

In HA setups with multiple namenodes, configure separate ports for each namenode in `hdfs-site.xml`:

``` xml
<property>
  <name>dfs.namenode.rpc-address.mycluster.nn1</name>
  <value>nn1.example.com:8020</value>
</property>
<property>
  <name>dfs.namenode.rpc-address.mycluster.nn2</name>
  <value>nn2.example.com:8020</value>
</property>
```

With HDFS Federation, each namenode namespace gets its own port configuration. Ensure no port conflicts when running multiple services on the same hardware.

## Modern Alternatives

For new deployments, evaluate managed Hadoop services (AWS EMR, Google Dataproc, Azure HDInsight) that handle port configuration and cluster management automatically. Kubernetes-based options like Apache Hadoop on Kubernetes or cloud-native data platforms may better suit modern infrastructure needs.

## 2026 Best Practices and Advanced Techniques

For Hadoop Port Reference Guide, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
