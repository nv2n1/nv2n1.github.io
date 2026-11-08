---
title: "Redis Architecture and Consistency Models Explained"
date: 2018-03-24 08:17:45 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/redis-architecture-consistency-model-etc/
---

Redis is an in-memory data structure store designed for speed and simplicity. Understanding its architecture and consistency guarantees is essential for deploying it correctly in production systems.

## Core Architecture

Redis operates as a single-threaded, event-driven server that uses an in-memory data store with optional persistence. The single-threaded nature simplifies reasoning about concurrent access — all commands execute atomically without locks, making race conditions impossible at the Redis level.

The server handles multiple client connections using multiplexing, typically via epoll on Linux or similar mechanisms on other systems. This allows Redis to serve thousands of concurrent clients efficiently despite the single-threaded execution model.

Data lives entirely in RAM, which provides microsecond-level latency for most operations. Redis includes optional persistence mechanisms:

- **RDB snapshots**: Point-in-time dumps of the entire dataset, useful for backups and disaster recovery
- **AOF (Append-Only File)**: Logs every write operation, allowing fine-grained recovery and better durability at the cost of higher disk I/O

You can combine both mechanisms or use neither, depending on your consistency requirements.

## Data Structures and Operations

Redis supports atomic operations on rich data structures: strings, hashes, lists, sets, sorted sets, streams, and others. Each operation on these structures is atomic — there’s no partial state visible to other clients.

For example, INCR on a counter is guaranteed to be atomic, as is LPUSH on a list. However, operations spanning multiple keys require Lua scripting or transactions for consistency guarantees.

## Consistency Model

Redis provides **strong consistency within a single instance**. All reads reflect the effects of previously completed writes, with no stale reads possible when accessing the same instance.

### Single-Instance Consistency

Operations execute in the order received, and the effects are immediately visible to subsequent operations. Persistence (RDB or AOF) ensures durability depending on configuration:

- **No persistence**: Fast but data loss on shutdown
- **AOF with fsync=always**: Durable but slower
- **AOF with fsync=everysec**: Good compromise between durability and performance
- **RDB snapshots**: Periodic durability with faster writes but potential data loss window

### Replication Consistency

Redis supports master-replica replication for high availability. Replicas apply commands from the master asynchronously, introducing a replication lag where replicas may temporarily serve stale data.

This is **eventual consistency**: replicas eventually converge on the master’s state, but there’s no guarantee of strong consistency in the replication topology. If the master fails before a write reaches replicas, that write is lost even if acknowledged to the client.

For applications requiring strong consistency across multiple nodes, consider:

- Using Redis Cluster with proper quorum acknowledgment
- Accepting the tradeoffs of eventual consistency
- Implementing application-level consensus mechanisms
- Using Redis Sentinel with careful failover procedures

### Redis Cluster

Redis Cluster provides horizontal scaling by partitioning data across multiple nodes using consistent hashing. Each key maps to a specific slot and primary node. Cluster maintains replica nodes for each partition to handle failover.

Cluster provides per-key strong consistency but not across keys stored on different nodes. Multi-key operations within a single slot remain atomic, but operations spanning slots lack transactional guarantees.

## Transactions and Scripting

Redis MULTI/EXEC transactions provide ACID semantics for command sequences, but only when commands target keys within a single slot (in Cluster) or the single instance (in standalone mode).

Lua scripts execute atomically as a single operation from the server’s perspective. Clients cannot interleave operations into a running script, making Lua useful for ensuring consistency across multiple keys:

``` lua
local current = redis.call('GET', KEYS[1])
if current == ARGV[1] then
  redis.call('SET', KEYS[1], ARGV[2])
  return 1
end
return 0
```

Script atomicity applies only within a single Redis instance, not across replication or cluster boundaries.

## Practical Deployment Considerations

- **Standalone with AOF**: Simple, single point of failure, good for non-critical caching
- **Master-replica with Sentinel**: Automatic failover, eventual consistency, requires operational overhead
- **Cluster**: Horizontal scaling, but complexity increases significantly and some operations become more expensive
- **Hybrid approaches**: Use Redis for caching with a durable database as source of truth

Choose your consistency model based on what data you’re storing. Cache misses are acceptable; losing payment data is not. Design your application accordingly rather than expecting Redis to provide guarantees it doesn’t offer.
