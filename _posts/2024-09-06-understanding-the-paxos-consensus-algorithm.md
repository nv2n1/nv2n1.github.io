---
title: "Understanding Paxos: Distributed Consensus Made Clear"
date: 2024-09-06 14:19:16 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /understanding-the-paxos-consensus-algorithm/
---

Paxos is a fundamental consensus algorithm for distributed systems that guarantees agreement on a single value even when nodes fail or messages are delayed. Developed by Leslie Lamport in 1998, it remains a cornerstone for building fault-tolerant distributed systems where strong consistency is required.

## The Core Problem

In a distributed system, you need multiple independent nodes to agree on a value despite:

- Asynchronous message delivery (no clock synchronization)
- Node failures and restarts
- Message loss (but not corruption)

A quorum-based approach solves this: if a majority of nodes agree, the value is committed. Even if some nodes fail, you only need half plus one to survive.

## The Three Roles

**Proposers** initiate consensus by proposing values. Multiple proposers can exist, but typically a leader emerges to reduce contention.

**Acceptors** store state and vote on proposals. A quorum (usually n/2 + 1 of them) makes decisions binding.

**Learners** learn the chosen value once consensus completes. These are often client applications or downstream services.

A single process can hold multiple roles simultaneously.

## Two Phases

**Phase 1: Prepare**

A proposer picks a proposal number (higher than any seen before) and sends a prepare request to a quorum of acceptors. The acceptor responds with a promise: “I won’t accept any proposal numbered lower than this one.” If the acceptor has already accepted a proposal, it returns the highest-numbered one seen so far.

**Phase 2: Accept**

Once the proposer receives promises from a quorum, it sends an accept request containing the value. If the proposer learned of an earlier accepted proposal during Phase 1, it must use that value instead of its own (this preserves consistency across rounds). Acceptors accept the request if no higher-numbered proposal was promised.

When a quorum accepts, the value is chosen. Learners are notified asynchronously.

## Why It Works

**Safety**: Only one value can be chosen because:

- To choose a value in round N, you need a quorum to accept it
- To promise in round N+1, a quorum must respond
- These two quorums overlap (that’s the math behind requiring a majority)
- The overlapping node will force round N+1 to use the value from round N

**Liveness**: Progress happens as long as a stable quorum can communicate. If two proposers keep increasing proposal numbers, neither makes progress—this is why leader election matters in practice.

## The Complexity Problem

Basic Paxos is notoriously hard to implement correctly. The state machine requires:

- Persistent storage for proposal numbers and accepted values
- Handling of stale requests after restart
- Timeout logic to detect failure and retry

The algorithm is sound, but the engineering is error-prone. Many production systems use variants or completely different algorithms to avoid this overhead.

## Practical Variants

**Multi-Paxos**: For agreeing on sequences of values (like a log), electing a stable leader eliminates Phase 1 repetition. Only the current leader performs prepare; acceptors skip it for that leader’s proposals. This reduces latency from 2 RTTs to 1 RTT for normal cases.

**Fast Paxos**: Reduces to 1 RTT in the happy path by allowing acceptors to accept proposals directly, but requires additional conflict resolution and more message complexity.

**Egalitarian Paxos (EPaxos)**: Designed for geo-distributed systems where any node can propose without a leader. It reorders commutative commands to reduce coordination, useful for high-contention scenarios.

**Vertical Paxos**: Separates the role of leader election from consensus, making it composable with other leader election mechanisms.

## Real-World Usage

Google Chubby (distributed lock service) uses a Paxos variant for replicating the lock state across data centers.

Etcd, widely used for Kubernetes coordination, implements Raft instead—a consensus algorithm explicitly designed to be more understandable than Paxos while maintaining similar properties.

CockroachDB uses a Paxos-inspired approach for range consensus to replicate database state.

Some blockchain systems reference Paxos concepts, though most use Proof-of-Work or variations of Byzantine consensus (which also handles malicious nodes, a problem Paxos doesn’t address).

## When to Use It

Paxos (or a variant) makes sense if you need:

- Strong consistency across replicas
- Tolerance for minority node failures
- Ability to continue after network partitions affecting minorities

If you can tolerate eventual consistency, simpler replication (like gossip or primary-backup) is more practical. If you need Byzantine fault tolerance (malicious nodes), use algorithms like PBFT or Tendermint instead.

For new systems, seriously consider Raft first—it’s easier to understand, implement, and debug. Paxos remains valuable for understanding distributed consensus theory and for inheriting systems built on it.
