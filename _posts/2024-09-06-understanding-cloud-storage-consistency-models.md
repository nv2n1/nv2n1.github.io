---
title: "Cloud Storage Consistency Models Explained"
date: 2024-09-06 14:35:45 +0000
layout: post
canonical: https://www.systutorials.com/understanding-cloud-storage-consistency-models/
---

Cloud storage systems face a fundamental trade-off: you can’t have everything at once. The consistency model you choose directly impacts latency, availability, and how complex your application logic needs to be. Here’s what you actually need to know to pick the right one.

### Strong Consistency

Guarantees that any read returns the most recent write. After you write data, every subsequent read—regardless of which node handles it—sees that write immediately.

**When to use:** Financial transactions, medical records, critical configuration data. Anything where stale reads are unacceptable.

**Real examples:**

- Google Cloud Spanner uses atomic clocks (TrueTime) to enforce global ordering
- PostgreSQL in synchronous replication mode
- etcd (Kubernetes’ config store) with default settings

**The cost:** Write latency increases because you’re waiting for acknowledgment across multiple nodes. During network partitions, you lose availability—writes may fail rather than risk inconsistency.

### Eventual Consistency

All replicas eventually converge on the same value, given enough time without new writes. You get temporary inconsistency windows.

**When to use:** Social feeds, DNS, caches, product catalogs. Things where slightly stale reads are tolerable.

**Real examples:**

- DynamoDB (default mode)
- Cassandra (default)
- S3 (between regions)

**The advantage:** Write operations complete locally without waiting for remote nodes. Blazingly fast. **The catch:** Your application must handle temporary contradictions. If two users update the same shopping cart simultaneously, you need conflict resolution logic.

### Read-Your-Writes Consistency

You always see your own writes, but others might not yet. After you write, your subsequent reads return that write.

**When to use:** Web applications where users expect to see their actions reflected immediately (comments, likes, profile updates).

**Real examples:**

- MongoDB sessions with `readConcern: "majority"`
- Most SQL databases with sticky routing to a primary

**Implementation detail:** Typically requires session affinity or a version vector. The client remembers which replica it wrote to and reads from there until it catches up.

### Causal Consistency

Operations that are causally related appear in the same order across all nodes. If operation B depends on operation A (you read A, then write B based on that read), everyone sees A before B.

**When to use:** Collaborative tools, version control systems, comment threads with replies.

**Real examples:**

- Eiger (research system)
- Some configurations of Azure Cosmos DB
- Manual implementation with version vectors

**Trade-off:** Requires tracking dependencies, which adds complexity and storage overhead.

### Monotonic Read Consistency

Once you read a value, you never see an older version in future reads. Prevents regression but allows gaps.

**When to use:** Analytics dashboards, time-series data, any scenario where “going backwards” is worse than being slightly behind.

**Implementation:** Track version numbers per object; if a read returns version 5, subsequent reads must return ≥5.

### Monotonic Write Consistency

Writes from a single process are applied in the order issued. The first write lands before the second, globally.

**When to use:** Append-only logs, audit trails, event streams.

**Real examples:**

- Kafka (per-partition ordering)
- Many databases in primary-replica setups

**Cost:** Requires synchronization of writes, potentially queuing them if they get reordered over the network.

## CAP Theorem

Brewer’s theorem states any distributed system can guarantee only two of:

- **Consistency (C):** Every read reflects the latest write or you get an error
- **Availability (A):** Every request gets a response (even if stale)
- **Partition Tolerance (P):** System works despite network splits

**In practice:** Network partitions happen. Choosing between C and A means:

- **CP systems** (Consistency + Partition tolerance): Block writes when partitioned. Examples: traditional databases in synchronous mode, Spanner
- **AP systems** (Availability + Partition tolerance): Accept writes during partitions, reconcile later. Examples: Cassandra, DynamoDB
- **CA** is not realistic for distributed systems (no partition tolerance = single node, defeats the purpose)

## Practical Comparison

| Model | Latency | Availability | Complexity |
|----|----|----|----|
| Strong | High | Lower (fails on partition) | Low |
| Eventual | Very Low | Very High | Medium-High (conflict resolution) |
| Read-Your-Writes | Medium | High | Medium |
| Causal | Medium | High | High |
| Monotonic (Read/Write) | Medium | High | Medium |

## Choosing a Model

Start with the question: **What breaks if the data is wrong for 5 seconds?**

- **Financial ledgers, payments:** Strong consistency. Latency is acceptable; errors are not.
- **User feeds, notifications:** Eventual consistency. Latency matters; a few stale items don’t.
- **Shopping cart, profile updates:** Read-your-writes. Users see their own changes instantly.
- **Comments with replies:** Causal consistency. Thread order matters.
- **Logs and events:** Monotonic writes. Order is critical.

Most modern systems are hybrid. S3 provides strong consistency within a region (as of 2024), eventual across regions. DynamoDB lets you choose per-request. Cosmos DB offers multiple selectable levels. Build for strong consistency by default, then relax it only where measured performance data justifies the operational complexity.
