---
title: "Distributed Consensus Algorithms: Paxos vs. Raft"
date: 2018-03-24 11:45:09 +0000
layout: post
canonical: https://www.systutorials.com/how-to-understand-some-key-system-consistency-algorithoms/
---

Distributed systems need consensus — a way for multiple nodes to agree on state despite failures and network partitions. Understanding the key algorithms behind consensus is essential for anyone designing reliable systems.

## Paxos and Its Variants

Paxos is the foundational consensus algorithm, proven to tolerate Byzantine failures. It works in three phases: prepare, accept, and learn. A proposer sends a prepare request with a proposal number, acceptors promise not to accept lower-numbered proposals, and once a majority accepts the proposal value, learners can be notified.

The algorithm guarantees safety (only one value is chosen) and liveness (a value will eventually be chosen if enough nodes are working). However, Paxos is notoriously difficult to implement correctly.

**Multi-Paxos** optimizes the basic algorithm by electing a leader to propose values, reducing message rounds. **Fast Paxos** allows bypassing the leader in some cases. **Egalitarian Paxos** removes the leader entirely for lower latency but increases coordination overhead.

## Raft: Practical Consensus

Raft was designed as a more understandable alternative to Paxos. It separates the problem into three subproblems: leader election, log replication, and safety. One node becomes the leader and handles all replication; followers append entries to their logs in the same order.

Key differences from Paxos:

- Simpler leader-based approach
- Stronger restrictions (e.g., only the leader can propose)
- More straightforward implementation in production systems
- Used by etcd, Consul, and many modern databases

Raft also defines membership changes and log compaction, making it practical for real deployments.

## Replicated State Machine

A replicated state machine applies the same sequence of commands to identical state machines across multiple nodes. If all nodes start in the same initial state and process the same commands in the same order, they will reach identical final states.

Consensus algorithms like Paxos and Raft ensure that all nodes agree on the log of commands before applying them. This transforms the consensus problem into a state machine replication problem.

## Quorum-Based Consistency

Quorum systems use voting to guarantee consistency without consensus algorithms. A quorum is a majority of nodes (typically N/2 + 1). Write operations succeed when a quorum acknowledges; read operations must consult a quorum to guarantee seeing the latest write.

Examples:

- **Read-Write Quorum**: Write to a quorum, read from a quorum. Guarantees consistency but higher latency.
- **Read-One Write-All**: Reads are fast, writes coordinate with all replicas. Fails if any replica is unavailable.
- **Read-All Write-One**: Opposite tradeoff.

Quorum systems are simpler than full consensus but offer weaker guarantees during partitions.

## Other Notable Algorithms

**PBFT (Practical Byzantine Fault Tolerance)**: Handles malicious nodes, not just failures. Requires 3f+1 nodes to tolerate f Byzantine faults. More complex than crash-fault-tolerant algorithms.

**Virtual Synchrony**: Provides group communication where all processes see the same sequence of membership and message events. Used in Spread and other group communication systems.

**Eventual Consistency**: Not consensus-based, but important for high-availability systems. Guarantees that without new writes, all replicas eventually converge. Used in DynamoDB, Cassandra.

**CRDTs (Conflict-free Replicated Data Types)**: Enable replication without coordination. Each node can write independently; conflict resolution is deterministic. Practical for collaborative applications.

## Practical Guidance

Choose based on your requirements:

- **Need strong consistency?** Use Raft (etcd, Consul) or Paxos variants (Zookeeper uses Zookeeper Atomic Broadcast, a Paxos variant)
- **Need high availability over strong consistency?** Consider quorum systems or eventual consistency
- **Need to handle Byzantine faults?** PBFT or similar, but accept higher overhead
- **Building collaborative/offline-first apps?** CRDTs offer compelling benefits

For implementation, study existing systems: etcd and Consul for Raft, Zookeeper for Paxos variants, or Redis Cluster for quorum-based approaches.

The best way to understand these algorithms is through papers combined with reading production implementations. Start with Raft’s paper and the etcd codebase — both are more accessible than classical Paxos literature.
