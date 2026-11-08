---
title: "Configuring Hadoop\u2019s Job Scheduling Policy"
date: 2018-03-24 11:50:17 +0000
author: "Eric Ma"
layout: post
categories: [design-patterns-architecture]
canonical: /how-change-my-policy-of-scheduling-in-hadoop/
---

The YARN resource scheduler determines how cluster resources are allocated to jobs. By default, Hadoop uses the Capacity Scheduler, but you can switch to an alternative like the Fair Scheduler or configure different scheduling policies.

## Identifying Your Current Scheduler

Check which scheduler is currently active by examining your configuration:

``` bash
grep -A 2 "yarn.resourcemanager.scheduler.class" $HADOOP_HOME/etc/hadoop/yarn-site.xml
```

The default scheduler is:

    org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler

## Switching Schedulers

Edit `$HADOOP_HOME/etc/hadoop/yarn-site.xml` and modify or add the scheduler configuration property:

``` xml
<property>
  <name>yarn.resourcemanager.scheduler.class</name>
  <value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler</value>
</property>
```

After making changes, restart the ResourceManager:

``` bash
$HADOOP_HOME/sbin/yarn-daemon.sh stop resourcemanager
$HADOOP_HOME/sbin/yarn-daemon.sh start resourcemanager
```

Or in a Hadoop cluster environment:

``` bash
$HADOOP_HOME/sbin/stop-yarn.sh
$HADOOP_HOME/sbin/start-yarn.sh
```

## Available Schedulers

**Capacity Scheduler** (default)

- Organizes resources into queues
- Each queue has a guaranteed capacity
- Best for multiple teams sharing a cluster
- Configuration file: `capacity-scheduler.xml`

**Fair Scheduler**

- Allocates resources fairly across jobs
- Jobs receive equal shares unless configured otherwise
- Supports job priorities and pool configurations
- Configuration file: `fair-scheduler.xml`

## Configuring the Fair Scheduler

If you switch to Fair Scheduler, create a `fair-scheduler.xml` file in `etc/hadoop/`:

``` xml
<?xml version="1.0"?>
<allocations>
  <pool name="production">
    <minResources>2048mb,4vcores</minResources>
    <maxResources>8192mb,16vcores</maxResources>
    <weight>4.0</weight>
  </pool>
  <pool name="development">
    <minResources>512mb,2vcores</minResources>
    <weight>1.0</weight>
  </pool>
  <defaultPool>development</defaultPool>
  <queuePlacementPolicy>
    <rule name="specified" create="false"/>
    <rule name="default"/>
  </queuePlacementPolicy>
</allocations>
```

Then reference it in `yarn-site.xml`:

``` xml
<property>
  <name>yarn.scheduler.fair.allocation.file</name>
  <value>/path/to/fair-scheduler.xml</value>
</property>
```

## Configuring the Capacity Scheduler

For Capacity Scheduler (default), edit `capacity-scheduler.xml`:

``` xml
<property>
  <name>yarn.scheduler.capacity.root.queues</name>
  <value>production,development</value>
</property>

<property>
  <name>yarn.scheduler.capacity.root.production.capacity</name>
  <value>60</value>
</property>

<property>
  <name>yarn.scheduler.capacity.root.development.capacity</name>
  <value>40</value>
</property>

<property>
  <name>yarn.scheduler.capacity.root.production.maximum-capacity</name>
  <value>100</value>
</property>
```

## Verifying the Change

After restarting, check the ResourceManager logs:

``` bash
tail -f $HADOOP_HOME/logs/yarn-*.log | grep -i scheduler
```

Access the YARN ResourceManager web UI (typically `http://resourcemanager-host:8088`) and verify the scheduler is running correctly under the “Cluster” menu.

## Key Differences in Job Ordering

- **Capacity Scheduler**: Jobs queue within their assigned queue; higher capacity queues get priority
- **Fair Scheduler**: Jobs are prioritized by submission order within each pool, with weight-based fair allocation

Choose based on your cluster’s needs: Capacity Scheduler for multi-tenant environments with strict resource guarantees, Fair Scheduler for more flexible, fair resource distribution.

## Hadoop Cluster Health Checks

Regular health checks keep your Hadoop cluster running smoothly:

- Check HDFS health: hdfs dfsadmin -report
- Check YARN resources: yarn node -list
- Monitor running applications: yarn application -list
- Check NameNode status through the web UI at port 9870
- Review ResourceManager metrics at port 8088

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Comprehensive Guide: 2026 Best Practices

This article provides foundational knowledge for working with Configuring Hadoop’s Job Scheduling Policy. In 2026, modern best practices emphasize security, reproducibility, and automation. Following these guidelines helps maintain clean, maintainable systems.

## Advanced Techniques and Alternatives

While the core commands and methods described in this article work well for most scenarios, advanced users often explore alternative tools for specific edge cases. Always document your custom configurations and configurations to help with troubleshooting and knowledge sharing within your team.

## Troubleshooting Common Issues

When encountering problems, follow a systematic debugging approach. Start with the simplest possible test case to isolate the issue. Check logs and error messages carefully—they often contain direct hints about what went wrong. For system-level issues, verify dependencies are correctly installed and configured before attempting complex workarounds.

## Performance Optimization Tips

- Monitor resource usage regularly to identify bottlenecks
- Use caching strategies where appropriate to reduce redundant computation
- Keep software updated to benefit from security patches and performance improvements
- Profile your code or configuration before applying optimizations
- Document performance baselines to measure the impact of changes

## Related Commands and Tools

These complementary tools and commands are frequently used alongside the topic of this article. Learning them expands your toolkit and makes you more efficient in daily workflows.

- System monitoring: top, htop, iotop for resource tracking
- File operations: find, locate, fd for efficient searching
- Network diagnostics: ping, traceroute, mtr, ss for connectivity checks
- Log analysis: journalctl, dmesg, tail for real-time log monitoring
- Package management: dnf history, apt list –installed, rpm -qa for inventory

## Integration with Modern Workflows

Consider how this technique integrates with modern automation and DevOps practices. Container-based deployments provide consistency across environments. Infrastructure as code tools like Terraform and Ansible enable reproducible configurations. Monitoring and alerting systems ensure timely notification of issues before they impact users.

## 2026 Updates and Changes

As of 2026, many tools and frameworks have introduced new features and deprecated old approaches. Always consult official documentation for your specific version when planning implementations. Community forums and Q&A sites can provide practical workarounds for edge cases not covered in official guides.

## Quick Reference Summary

This article covered essential concepts and practical examples. For deep dives, refer to official documentation or specialized guides. Practice in a test environment before applying changes to production systems.
