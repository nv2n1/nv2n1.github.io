---
title: "Balancing HDFS DataNode Storage"
date: 2018-03-24 11:43:38 +0000
modified: 2026-04-12 16:55:20 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-balance-datanode-storage-in-hdfs/
---

As nodes are added or removed from a Hadoop cluster, storage utilization becomes uneven across DataNodes. Some fill up while others remain mostly empty, leading to inefficient resource use and potential storage bottlenecks. HDFS provides the Balancer tool to redistribute blocks across DataNodes and even out disk usage.

## Understanding the Balancer

The HDFS Balancer is a tool that moves blocks from over-utilized DataNodes to under-utilized ones. It runs as a separate process and operates within configurable thresholds to avoid disrupting normal cluster operations. The Balancer checks the average storage utilization across all nodes and moves blocks to bring nodes closer to that average.

Key characteristics:

- Runs as a daemon process (doesn’t block normal cluster operations)
- Only moves blocks; data integrity is maintained
- Works on a threshold-based approach: nodes beyond the threshold are considered imbalanced
- Can be run while the cluster handles normal read/write traffic

## Starting the Balancer

Run the Balancer as the HDFS superuser (usually `hdfs`):

``` bash
hdfs balancer
```

To see progress and status information:

``` bash
hdfs balancer -v
```

The tool will output block-moving operations and exit once the cluster reaches an acceptable balance state.

## Common Balancer Options

**Set bandwidth limit** (in MB/s, default 10 MB/s):

``` bash
hdfs balancer -bandwidth 20
```

Use this to throttle the balancer and avoid overwhelming network or disk I/O on production clusters.

**Exclude specific nodes** from balancing:

``` bash
hdfs balancer -exclude /tmp/exclude.txt
```

Create the exclude file with one hostname per line to prevent rebalancing specific DataNodes.

**Set imbalance threshold** (percentage, default 10%):

``` bash
hdfs balancer -threshold 5
```

Lower thresholds mean tighter balancing but require more block moves. Higher thresholds complete faster but leave more skew.

## Stopping the Balancer

The Balancer runs continuously until:

- The cluster reaches the configured balance threshold
- You explicitly stop it with:

``` bash
hadoop dfsadmin -cancelBalancer
```

Or kill the process directly:

``` bash
pkill -f "hdfs balancer"
```

## Monitoring Balancer Operations

Check the balancer logs:

``` bash
tail -f $HADOOP_LOG_DIR/hadoop-hdfs-balancer-*.log
```

Use `dfsadmin` to check cluster balancing status:

``` bash
hdfs dfsadmin -report
```

This shows storage utilization per DataNode and whether the cluster is considered balanced.

## Balancer Configuration in hdfs-site.xml

Fine-tune behavior via these settings:

``` xml
<property>
  <name>dfs.datanode.balance.bandwidthPerSec</name>
  <value>10485760</value> <!-- 10 MB/s in bytes -->
</property>

<property>
  <name>dfs.balancer.moverThreads</name>
  <value>1000</value> <!-- concurrent block moves -->
</property>

<property>
  <name>dfs.balancer.max-size-to-move</name>
  <value>10737418240</value> <!-- max bytes per DataNode per run -->
</property>
```

## When to Run the Balancer

Run the Balancer:

- After adding new DataNodes to the cluster
- After decommissioning or removing nodes
- When utilization skew reaches unacceptable levels (monitor via `hdfs dfsadmin -report`)
- During maintenance windows on large clusters to minimize performance impact

Avoid running during peak traffic unless bandwidth limits are set conservatively.

## Important Notes

The Balancer respects rack awareness and replication constraints—it won’t violate data locality or create replicas beyond policy. On large clusters with many under-replicated blocks, prioritize fixing replication issues first; the Balancer won’t operate effectively if the cluster is already struggling with block placement.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Balancing HDFS DataNode Storage with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Balancing HDFS DataNode Storage. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
