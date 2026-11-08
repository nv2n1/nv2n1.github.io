---
title: "High Availability in Distributed Storage: RDA Fundamentals"
date: 2018-03-24 11:43:19 +0000
layout: post
canonical: https://www.systutorials.com/whats-the-difference-between-reliability-durability-and-availability-for-data-storage-system/
---

Understanding the difference between reliability, durability, and availability is critical when designing or operating distributed storage systems like HDFS, Ceph, or cloud object storage. These terms are often confused, but they address distinct concerns.

## Durability

Durability answers: *If the system fails completely, will my data survive?*

Durability is about persistence to non-volatile storage. Data is durable when it’s been written to stable storage (disk, flash, or similar) in a form that can be recovered and used after any type of failure. A durable system ensures that once you acknowledge a write to the client, that data won’t be lost even if every power supply fails simultaneously.

In practice, durability is achieved through:

- Writing data to disk or flash storage (not just RAM)
- Using write-ahead logs or similar mechanisms
- Replicating data across physically independent systems
- Checksums and redundancy (RAID, erasure coding, etc.)

If a node crashes mid-write, durability doesn’t require the system to continue operating—only that previously committed data survives.

## Availability

Availability answers: *When a partial failure occurs, does the system keep working?*

Availability means the system continues to provide its original service despite component failures. This could be a failed disk, a dead node, or a network partition. The system should continue accepting and serving requests without manual intervention.

In distributed system contexts, availability has multiple interpretations:

**System availability** (traditional HA): The entire system remains operational and accessible to clients, even if individual components fail. Classic examples include heartbeat-based failover with virtual IP address takeover.

**Node availability** (CAP Theorem context): Individual nodes that haven’t failed continue to serve requests. This is stricter—it means you can’t arbitrarily shut down healthy nodes to preserve consistency. For example, in a system that values availability over consistency, a minority partition will continue responding to writes rather than blocking to maintain a consistent state.

These interpretations matter because a system optimized for node availability might behave differently than one optimized for system availability.

## Reliability

Reliability is the most ambiguous of the three terms. Different communities define it differently:

- Some use it as a synonym for availability
- Some use it to mean the system as a whole remains available (vs. individual nodes)
- Some use it to mean fault-tolerant consensus—the ability to reach agreement despite failures (essentially what CAP Theorem calls “consistency”)
- Many use it carelessly without a specific definition

Because there’s no consensus, avoid using “reliable” or “reliability” in technical specifications. Instead, be explicit: say “the system maintains availability during node failures” or “data survives total power loss” or “the cluster reaches consensus despite network partitions.”

## Practical Examples

**Scenario 1: HDFS with replication factor 3**

- **Durable**: Yes. Data written to disk on 3 nodes survives any single node failure.
- **Available**: Yes. If one node fails, the remaining replicas serve read requests, and the namenode continues accepting writes.
- **Reliable**: Don’t use this term—specify what you mean.

**Scenario 2: Single-node database with no replication**

- **Durable**: Only if data is flushed to disk before acknowledging writes.
- **Available**: No. A disk failure or crash stops the service entirely.
- **Reliable**: Ambiguous—clarify your requirement.

**Scenario 3: Replicated database with quorum-based writes**

- **Durable**: Yes. Data acknowledged only after write to multiple replicas.
- **Available**: Depends on the quorum size. A system requiring a majority quorum becomes unavailable if you lose too many nodes; this sacrifices availability for consistency.

## In Your Architecture

When designing or evaluating storage systems:

- **Define durability guarantees** in terms of failure scenarios (e.g., “survives simultaneous failure of any 2 nodes”)
- **Define availability requirements** explicitly (e.g., “system continues accepting reads/writes with up to N failures” or “RTO \< 5 minutes”)
- **Avoid “reliability”** without clarification—use the specific term you mean
- **Understand the tradeoffs** (CAP Theorem): you can’t have perfect durability, availability, and consistency simultaneously under network partition
