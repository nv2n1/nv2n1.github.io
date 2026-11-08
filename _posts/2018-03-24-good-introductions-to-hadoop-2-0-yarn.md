---
title: "Understanding YARN: Resource Management and Cluster Fundamentals"
date: 2018-03-24 08:22:28 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /good-introductions-to-hadoop-2-0-yarn/
---

YARN (Yet Another Resource Negotiator) fundamentally restructured Hadoop 2.0 by decoupling resource management from application logic. If you’re transitioning from Hadoop 1.x or building systems on top of YARN, understanding its architecture is essential for effective cluster administration and application development.

## Essential Reading

**The foundational paper**

Start with “Apache Hadoop YARN: Yet Another Resource Negotiator” by Vinod Kumar Vavilapalli et al. (SoCC13). This remains the canonical reference for understanding architectural decisions and design trade-offs. It’s dense but explains *why* YARN works the way it does, not just the mechanics.

**Practical guides**

“Apache Hadoop YARN: Concepts and Applications” by Arun Murthy (a core YARN contributor) bridges theory and real-world implementation. It’s more accessible than academic papers while remaining technically solid.

**Official documentation**

The <a href="https://hadoop.apache.org/docs/current/hadoop-yarn/" rel="nofollow noopener" target="_blank">Apache Hadoop YARN documentation</a> provides comprehensive API references and configuration details. Treat it as reference material rather than a tutorial—use it once you understand the core concepts.

## Core Architecture Components

**Resource Manager and Node Manager**

The Resource Manager (RM) is the cluster-level authority allocating resources globally. Node Managers (NM) run on each data node, managing node-local resources and reporting node health to the RM. This split between global and local management enables YARN to support multiple processing frameworks simultaneously.

**Application Master**

Each YARN application spawns an Application Master (AM) that negotiates resources with the RM and orchestrates task execution. Unlike Hadoop 1.x’s centralized JobTracker, the AM pattern is distributed—each application handles its own scheduling logic. This allows frameworks like Spark and Flink to implement custom scheduling strategies.

**Containers**

YARN abstracts compute resources as containers: logical bundles of CPU, memory, and optional GPU. Applications request containers with specific requirements rather than fixed task slots. This flexibility enables better resource utilization than Hadoop 1.x’s rigid slot model.

## Configuration and Tuning

Review `yarn-site.xml` settings critical to your workload:

``` xml
<!-- Total memory available per node -->
<property>
  <name>yarn.nodemanager.resource.memory-mb</name>
  <value>8192</value>
</property>

<!-- Maximum memory per container request -->
<property>
  <name>yarn.scheduler.maximum-allocation-mb</name>
  <value>4096</value>
</property>

<!-- Container virtual CPU cores -->
<property>
  <name>yarn.nodemanager.resource.cpu-vcores</name>
  <value>4</value>
</property>

<!-- Application Master memory -->
<property>
  <name>yarn.app.mapreduce.am.resource.mb</name>
  <value>1024</value>
</property>
```

Misconfiguring these limits prevents applications from requesting sufficient resources. A common mistake is setting `maximum-allocation-mb` lower than what your largest jobs need.

## Scheduler Selection

YARN ships with two primary schedulers:

**Capacity Scheduler** — partitions cluster capacity into queues with guaranteed minimums. Use this for multi-tenant environments where different teams or applications need resource isolation. Supports queue hierarchies and priority levels.

**Fair Scheduler** — allocates resources dynamically based on application demand, ensuring no application starves. Better for batch processing where jobs have variable duration and resource needs.

Check which scheduler is active:

``` bash
yarn schedulerconf -getSchedulerconf | grep scheduler.class
```

## Practical Setup and Monitoring

Deploy a test cluster using Docker or local containers rather than physical hardware:

``` bash
# Start a basic YARN cluster in containers
docker-compose up -d

# Submit a test job
yarn jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar \
  wordcount /input /output

# Monitor at http://localhost:8088
```

Check the ResourceManager web UI for application state, container allocation, and scheduler queue information. Monitor logs at `$HADOOP_LOG_DIR/yarn-<user>-resourcemanager-*.log` on the RM host.

Key metrics to observe:

- **Allocated vs Available memory**: Indicates scheduler saturation
- **Container startup time**: Flags slow AM negotiation or allocation delays
- **Task failure rates**: Track application stability

## Next Steps

After understanding these fundamentals:

1.  Study how your processing framework (Spark, Flink, etc.) implements the Application Master interface
2.  Configure resource limits for your workload using memory and vcore constraints
3.  Set up queue hierarchies if running multi-tenant clusters
4.  Enable log aggregation to centralize application logs across nodes
5.  Monitor long-term resource usage and adjust node capacity accordingly

YARN’s flexibility comes from understanding resource negotiation. Invest time in observing how containers are allocated during actual job execution—the web UI and logs reveal far more than documentation alone.
