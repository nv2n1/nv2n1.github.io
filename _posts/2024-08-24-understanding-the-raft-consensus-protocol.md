---
title: "Understanding the Raft Consensus Protocol"
date: 2024-08-24 04:24:24 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/understanding-the-raft-consensus-protocol/
---

Raft is a consensus algorithm designed to be more understandable than alternatives like Paxos. It ensures a cluster of servers can agree on system state even when some nodes fail. The core insight is breaking consensus into independent, manageable subproblems rather than treating it as one complex whole.

## Core Subproblems

Raft splits consensus into three areas:

**Leader Election** — Exactly one leader exists per term. If the leader fails or becomes unreachable, the cluster elects a replacement.

**Log Replication** — The leader accepts client commands, appends them to its log, and replicates entries across followers. All committed entries eventually exist on all nodes.

**Safety** — Logs remain consistent across nodes despite failures. Uncommitted entries may be lost, but committed entries are never lost or overwritten.

## Node Roles

Every Raft node is in exactly one of three states:

**Leader** — Accepts client requests, replicates log entries, sends periodic heartbeats. There’s one leader per term.

**Follower** — Receives AppendEntries RPCs from the leader and RequestVote RPCs from candidates. Followers are passive—they don’t initiate communication.

**Candidate** — A follower that initiates an election. It increments the term, votes for itself, and requests votes from peers.

## Leader Election

Raft uses randomized election timeouts to ensure liveness. Each follower picks a random timeout between 150-300ms (values vary by implementation). If no heartbeat arrives before this timeout expires, the follower becomes a candidate.

When a node becomes a candidate, it:

1.  Increments its current term
2.  Votes for itself
3.  Sends RequestVote RPCs to all other nodes in parallel
4.  Waits for responses

A node grants its vote to the first candidate requesting it within a term. It denies subsequent vote requests in that same term. This prevents multiple leaders from being elected in one term.

A candidate wins the election by receiving votes from a majority of the cluster. On winning, it becomes the leader and sends heartbeat AppendEntries RPCs to all followers to suppress further elections.

If the candidate doesn’t win (split vote), it waits for a new election timeout and tries again. The randomized timeouts prevent repeated splits—statistically, one candidate will timeout first and win before others can start an election.

## Log Replication

The leader is the only node that accepts client requests. When a client submits a command:

1.  The leader appends a log entry containing the command, the current term, and a unique log index
2.  The leader sends AppendEntries RPCs to all followers, including the new entry
3.  Followers append the entry to their logs and acknowledge
4.  Once a majority of nodes have the entry, the leader marks it as committed
5.  The leader applies the committed entry to its state machine and returns the result to the client
6.  The leader notifies followers of the new commitIndex; followers apply committed entries to their state machines

If a follower is slow or crashes, the leader retries AppendEntries indefinitely until the follower catches up.

## Consistency Guarantees

Raft maintains consistency through several mechanisms:

**Term Numbers** — Each term is uniquely numbered and monotonically increases. A node always uses the highest term it has seen. If a candidate or leader receives a higher term from any peer, it immediately becomes a follower. This prevents old leaders from committing entries.

**Log Matching Property** — If two log entries exist with the same index and term on different servers, they are identical, and all entries before them are identical.

**Leader Completeness** — A newly elected leader is guaranteed to contain all entries committed in previous terms. This is enforced by vote restrictions—a candidate only wins if its log is at least as up-to-date as a majority of voters.

## Failure Scenarios

**Follower Failure** — If a follower crashes, the leader detects this when AppendEntries RPCs fail. The leader continues operating as long as a majority remains healthy. When the follower recovers, the leader replicates missing entries to bring it up-to-date.

**Leader Failure** — If the leader crashes, followers detect this via missing heartbeats. After an election timeout, one follower becomes a candidate and starts an election. The cluster elects a new leader and continues. Uncommitted entries from the old leader may be lost, but committed entries are preserved—the new leader contains all committed entries by the Leader Completeness property.

**Network Partition** — Raft handles arbitrary network delays and message loss. Only the partition containing a majority of nodes can elect a leader. The minority partition cannot commit new entries (its leader candidates fail to achieve majority votes). When the partition heals, the minority partition catches up. This sacrifices availability in the minority partition to ensure consistency.

## Practical Considerations

Raft is widely used in systems like etcd, Consul, and LiteFS. When implementing or deploying Raft:

- Election timeouts directly impact recovery time but must be high enough to avoid spurious elections on slow networks. 150-300ms is common for LAN deployments; adjust for higher latency networks.
- Batch AppendEntries RPCs to reduce network load and improve throughput.
- Persist term and vote state to disk before responding to RPCs—this ensures safety across restarts.
- The state machine applies committed entries sequentially. If your application requires strong linearizability, apply entries in order and use request deduplication to handle retries.
- Monitor leader election frequency and log replication lag. High election rates indicate timeout mistuning.

Raft’s strength is clarity and practicality. The algorithm is straightforward to reason about and implement correctly, which has made it the standard choice for new distributed systems.
