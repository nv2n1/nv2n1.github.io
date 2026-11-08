---
title: "Finding HDFS Files with Replication Factor 1"
date: 2018-03-24 11:53:43 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /how-to-find-out-all-files-with-replication-factor-1-in-hdfs/
---

Files with replication factor 1 are a liability in production HDFS clusters. They have no redundancy, meaning a single node failure results in data loss. Identifying and fixing these files should be part of your regular cluster maintenance.

## Using the HDFS CLI

The most straightforward approach is using `hdfs fsck` with output parsing:

``` bash
hdfs fsck / -files -blocks -replicaDetails | grep "Replica.*1$"
```

This command traverses the entire filesystem starting from root, reports block details, and filters for blocks with only one replica. However, this approach can be slow on large clusters and generates substantial output.

A more efficient method uses `hdfs fsck` with `-storagepolicies` flag and direct inspection:

``` bash
hdfs fsck / -files -blocks 2>/dev/null | awk '/UNDER_REPLICATED|Block.*Replica/ {print}'
```

## Finding Specific Files

To list only the actual files (not blocks) with replication factor 1:

``` bash
hdfs fsck / -files -blocks 2>/dev/null | grep -B2 "under replicated Block"
```

For a cleaner output showing just the file paths:

``` bash
hdfs dfs -find / -type f -exec hdfs fsck {} \; 2>/dev/null | grep -i "under.replicated" | awk '{print $NF}'
```

A better approach uses the NameNode WebUI or queries the fsimage directly. If you have access to the NameNode, use:

``` bash
hdfs oiv -p Delimited -i /path/to/fsimage -o /tmp/fsimage.txt
cat /tmp/fsimage.txt | awk -F',' '$6 == 1 {print $2}' | sort -u
```

This reads the fsimage file and extracts filenames where the replication factor (column 6) equals 1.

## Using JMX Metrics

For programmatic access to under-replicated block information:

``` bash
curl -s http://namenode:9870/jmx | jq '.beans[] | select(.name=="Hadoop:service=NameNode,name=FSNamesystemState") | .UnderReplicatedBlocks'
```

This gives you the total count of under-replicated blocks without parsing raw fsck output.

## Fixing the Problem

Once identified, increase the replication factor:

``` bash
hdfs dfs -setrep -w 3 /path/to/file
```

The `-w` flag waits for replication to complete before returning. For directories:

``` bash
hdfs dfs -setrep -R -w 3 /path/to/directory
```

To set a default replication factor cluster-wide, modify `hdfs-site.xml`:

``` xml
<property>
  <name>dfs.replication</name>
  <value>3</value>
</property>
```

## Automation

For regular monitoring, create a cron job that alerts when files with RF=1 are detected:

``` bash
#!/bin/bash
UNDER_REP=$(hdfs fsck / -files -blocks 2>/dev/null | grep -c "under replicated")
if [ $UNDER_REP -gt 0 ]; then
  echo "Alert: $UNDER_REP under-replicated blocks found" | mail -s "HDFS Alert" ops@example.com
fi
```

Run this daily to catch issues early. Consider integrating with your monitoring stack (Prometheus, Grafana) for better visibility.

## Performance Considerations

Running `hdfs fsck` on large clusters blocks NameNode operations. Schedule full scans during maintenance windows. For continuous monitoring on production clusters, rely on NameNode metrics via JMX rather than full filesystem checks.

## 2026 Best Practices and Advanced Techniques

For Finding HDFS Files with Replication Factor 1, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
