---
title: "Paxos vs. Raft: Consensus Algorithms Compared"
date: 2024-09-06 14:19:36 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /comparing-paxos-and-raft/
---

Paxos and Raft are foundational consensus algorithms for distributed systems. Both solve the same core problem — achieving agreement across multiple nodes despite failures — but take fundamentally different approaches.

## Paxos

Paxos operates around three distinct roles:

- **Proposers** submit values
- **Acceptors** store and respond to requests
- **Learners** observe the final decision

The algorithm proceeds in two main phases:

1.  **Prepare Phase**: Proposers send prepare requests with increasing proposal numbers to all acceptors. Acceptors promise not to accept lower-numbered proposals.
2.  **Accept Phase**: Upon receiving promises from a majority, proposers send accept requests containing the actual value. Acceptors acknowledge if no higher proposal arrived.

A majority must agree in both phases for consensus. The algorithm guarantees safety (never accepting conflicting values) but requires two full round-trip times (RTTs) per consensus round.

**Production examples**: Google’s Chubby lock service, Apache ZooKeeper’s implementation variants.

**Trade-offs**:

- Strong theoretical guarantees and flexible under arbitrary failure scenarios
- Implementation complexity — the original paper’s ambiguity spawned years of debate and refinements like Multi-Paxos
- Without optimizations, message complexity is O(2N) per round

## Raft

Raft simplifies consensus through explicit roles and a leader-based design:

- **Leader** manages all log replication
- **Followers** replicate entries and vote during elections
- **Candidates** transition state during elections

Raft divides consensus into three independent subproblems:

1.  **Leader Election**: Followers wait for heartbeats. Timeout triggers candidates requesting votes from all nodes. First candidate achieving majority becomes leader.
2.  **Log Replication**: Leader appends entries to followers’ logs, retrying failed replication until success.
3.  **Safety**: New leaders only append entries from previous terms after their own term’s commit, preventing uncommitted data from becoming permanent.

One RTT for election, one RTT for replication while leader is stable. Message complexity is O(N) per round.

**Production examples**: etcd, Consul, CoreDNS, Kubernetes ETCD backend.

**Trade-offs**:

- Designed for understandability — straightforward state transitions and roles
- Efficient leader-based log replication minimizes latency for subsequent entries
- Primarily optimized for state machine replication, not general consensus problems

## Practical Comparison

| Aspect | Paxos | Raft |
|----|----|----|
| **Roles** | Proposer, Acceptor, Learner (distributed) | Leader, Follower, Candidate (hierarchical) |
| **Phases per round** | 2 (Prepare, Accept) | 1 (once leader stable) |
| **Leader explicit** | No (Multi-Paxos adds this) | Yes, always |
| **Message complexity** | O(2N) baseline | O(N) baseline |
| **Implementation effort** | High — significant protocol subtleties | Low — clear state machine |
| **Flexibility** | High — handles arbitrary topologies | Lower — optimized for single-leader |

## When to Use What

**Choose Raft** for:

- Building distributed coordination services
- State machine replication (consensus for logs)
- Teams prioritizing implementation correctness over theoretical flexibility
- Systems like database replication, configuration management, or key-value stores

Most modern open-source projects (etcd, Consul) use Raft because the implementation correctness advantage outweighs theoretical flexibility.

**Choose Paxos** (or variants) for:

- Academic research or complex distributed scenarios
- Systems where multiple concurrent proposers without a leader simplify architecture
- Existing codebases already using Paxos variants
- Problems requiring consensus beyond single-leader replication

## Implementation Reality

In 2026, you’re far more likely to encounter Raft in production systems. The algorithm’s clarity directly translates to fewer bugs. Reference implementations exist in Go, Rust, and Java. The main Raft variants (like Etcd’s implementation with strict leader restrictions) continue to prove robust.

Paxos remains theoretically important and underpins some critical systems, but Multi-Paxos needed significant clarification work (see Paxos Made Practical by Google researchers) to become production-viable.

If you’re building a distributed system from scratch today, Raft is the pragmatic choice. You’ll ship faster, debug easier, and the available tooling and community knowledge is substantially deeper.
