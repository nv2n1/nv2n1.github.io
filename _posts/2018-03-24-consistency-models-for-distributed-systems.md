---
title: "Consistency Models in Distributed Systems"
date: 2018-03-24 08:15:46 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/consistency-models-for-distributed-systems/
---

Consistency models define the guarantees that a distributed system makes about the order and visibility of data modifications across nodes. Understanding these models is essential when designing systems, choosing databases, or debugging data anomalies in production.

## Strong Consistency Models

**Strict Consistency** is the ideal but rarely achievable model. It guarantees that reads always reflect the most recent write globally, with instantaneous propagation across all nodes. Physical constraints make this impractical in real systems.

[**Linearizability** (atomic consistency)](/linear-consistency-model-for-computer-systems/) is the strongest practical model. It ensures that operations appear to execute in some total order, and each operation takes effect instantaneously between its invocation and response. This is what most developers intuitively expect. Systems like Consul, etcd, and Zookeeper provide linearizable operations for critical data, though at the cost of coordination overhead.

**Sequential Consistency** requires that all operations appear in the same order to all processes, but not necessarily in real-time order. Reads may see stale data, but the sequence is consistent globally. This is weaker than linearizability but often sufficient for many applications.

## Weak Consistency Models

**Causal Consistency** preserves causality—if operation B depends on operation A, then all processes will see A before B. This is stronger than FIFO ordering but weaker than sequential consistency. It’s useful for systems where dependency tracking is feasible.

**FIFO Consistency** (also called PRAM consistency) guarantees that writes from a single process are seen in order by all other processes, but writes from different processes may be seen in different orders. This is a reasonable model for eventually consistent systems with per-client ordering guarantees.

**Eventual Consistency** is the weakest model: if no new writes occur, all replicas will converge to the same state. There’s no bound on how long this takes. Modern distributed databases like DynamoDB, Cassandra, and Riak use eventual consistency by default to maximize availability. However, applications must handle temporary inconsistencies and read-your-own-writes guarantees typically require application logic.

**Session Consistency** is a practical middle ground that guarantees read-your-own-writes and monotonic reads within a client session. The client sees effects of its own operations immediately, but may see stale data from other clients. Many cloud databases offer this as a configurable option.

## Consistency in Database Transactions

Transaction isolation levels are related but distinct from distributed system consistency models:

- **Serializable**: Transactions execute as if they ran sequentially. Equivalent to linearizable transactions.
- **Repeatable Read**: A transaction won’t see phantom rows, but may see uncommitted data from concurrent transactions.
- **Read Committed**: Transactions only see committed data, but may see non-repeatable reads.
- **Read Uncommitted**: The weakest level; transactions may see uncommitted changes from other transactions.

The gap between isolation levels and consistency models is important: a database might provide serializable isolation but not linearizable consistency across multiple database instances in a cluster.

## Practical Trade-offs

Strong consistency requires coordination, reducing availability and increasing latency. Systems like PostgreSQL with synchronous replication prioritize consistency. Weak consistency trades consistency for availability and partition tolerance—distributed caches and event logs often operate this way.

Most production systems operate in the middle: they provide strong consistency for critical operations (user authentication, financial transactions) and eventual consistency for best-effort operations (caching, analytics, logging). Redis can offer strong consistency with Sentinel or Cluster mode, while still accepting weaker reads when appropriate.

When evaluating or building systems, document which consistency model applies to each data category. A single “consistency level” setting often masks complexity—you may need linearizable consistency for one table and eventual consistency for another.

## References

- Steinke, R. C., & Nutt, G. J. (2004). A unified theory of shared memory consistency. *Journal of the ACM*, 51(5), 800-849.
- Mosberger, D. (1993). Memory consistency models. *ACM SIGOPS Operating Systems Review*, 27(1), 18-26.
- Adve, S. V., & Gharachorloo, K. (1996). Shared memory consistency models: A tutorial. *ACM SIGARCH Computer Architecture News*, 24(1), 66-76.
- Berenson, H., et al. (1995). A critique of ANSI SQL isolation levels. *Proceedings of the 1995 ACM SIGMOD International Conference*.
- Gray, J. N., et al. (1998). Granularity of locks and degrees of consistency in a shared data base. In *Readings in Database Systems* (3rd ed.).
