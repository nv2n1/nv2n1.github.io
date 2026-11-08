---
title: "Distributed Systems and Cloud Computing: Essential Reading Guide"
date: 2012-09-15 22:41:05 +0000
layout: post
canonical: https://www.systutorials.com/reading-list-for-system-research-on-cloud-computing/
---

Understanding distributed systems and cloud computing starts with the literature. These papers form the foundation for anyone working in the space — they’re not just historical artifacts, they’re still actively referenced and their design principles remain relevant.

### Internet-Scale Systems and Datacenters

The Google cluster architecture paper remains essential reading. It laid out the practical realities of building and operating datacenters at scale:

- Luiz Barroso, Jeffrey Dean, Urs Hoelzle. “Web Search for a Planet: The Google Cluster Architecture.” IEEE Micro, Vol. 23, No. 2, pp. 22-28, 2003.

## Distributed Computing Frameworks

**MapReduce** established the pattern for large-scale data processing on commodity clusters and remains influential:

- Dean, J. and Ghemawat, S. “MapReduce: Simplified Data Processing on Large Clusters.” OSDI’04, 2004.

**Spark and in-memory computation** refined the approach with fault tolerance and performance improvements:

- Matei Zaharia et al. “Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing.” NSDI’12, 2012.

Modern systems build on these foundations with graph computation frameworks (Pregel, GraphX) and specialized execution engines, but the core abstraction of defining computations on distributed collections remains the same.

## Consensus and Coordination

Paxos is fundamental to understanding how distributed systems reach agreement. Multiple papers help with understanding:

- Lamport, L. “The Part-Time Parliament.” ACM Transactions on Computer Systems, Vol. 16, No. 2, pp. 133-169, 1998.
- Lamport, L. “Paxos Made Simple.” ACM SIGACT News, Vol. 32, No. 4, pp. 18-25, 2001.

Practical systems implementing Paxos show how to build reliable services:

- Burrows, M. “The Chubby Lock Service for Loosely-Coupled Distributed Systems.” OSDI’06, 2006.

Modern systems like etcd, Consul, and ZooKeeper implement similar consensus protocols (Raft, which is more intuitive than Paxos, or variations of Paxos). Understanding Chubby is valuable because many current coordination services follow its patterns.

## Distributed Storage

**GFS** established the model for scalable distributed file systems:

- Ghemawat, S., Gobioff, H., and Leung, S. “The Google File System.” SOSP’03, 2003.

GFS principles inform systems like HDFS, Ceph, and cloud storage backends today. The paper clearly addresses scalability, consistency guarantees, and fault tolerance — challenges that remain central.

## Key-Value Stores and Databases

**Dynamo** introduced the eventually-consistent distributed hash table:

- DeCandia, G. et al. “Dynamo: Amazon’s Highly Available Key-Value Store.” SOSP’07, 2007.

This paper shaped the design of modern NoSQL stores. Understanding the trade-offs Dynamo makes between consistency and availability is critical.

**Bigtable** showed how to layer structured data storage on top of distributed infrastructure:

- Chang, F. et al. “Bigtable: A Distributed Storage System for Structured Data.” OSDI’06, 2006.

The wide-column model Bigtable introduced influenced HBase, Cassandra, and other systems.

## Strong Consistency at Scale

As systems matured, the limitations of eventual consistency became clear. Recent papers address distributed transactions:

- Baker, J. et al. “Megastore: Providing Scalable, Highly Available Storage for Interactive Services.” CIDR’11, 2011.

- Corbett, J. C. et al. “Spanner: Google’s Globally-Distributed Database.” OSDI’12, 2012.

Spanner is particularly important — it shows how to provide ACID semantics across geographically distributed datacenters using synchronized clocks and careful engineering. Understanding the CAP theorem trade-offs and how Spanner navigates them is essential for modern systems work.

## Where to Start

If you’re new to this material, begin with “Paxos Made Simple” and the MapReduce paper — both are relatively accessible and provide context for everything else. Then move to GFS, Dynamo, and Bigtable as a coherent progression through the storage layer. Finally, study Spanner to see how modern systems handle the consistency problem at global scale.
