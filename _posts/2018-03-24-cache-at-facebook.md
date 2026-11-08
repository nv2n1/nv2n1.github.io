---
title: "Caching Strategies at Facebook"
date: 2018-03-24 08:16:59 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /cache-at-facebook/
---

Facebook operates two distinct caching systems, each designed for different access patterns and consistency requirements.

**Memcache** serves as a lookaside cache where the intelligence resides primarily on the client side. This architecture means applications are responsible for cache invalidation, consistency checks, and determining what data to cache. Memcache is stateless and horizontally scalable, making it suitable for ephemeral data and objects where eventual consistency is acceptable.

**TAO** (The Association and Origin) functions as a caching graph database with active query capabilities. Unlike Memcache’s passive role, TAO executes its own queries against MySQL and maintains semantic understanding of data relationships. This is particularly valuable for social graph queries where relationships between entities need to be traversed efficiently.

## Key Architectural Differences

The fundamental difference between these systems reflects their design philosophies:

- **Memcache**: Client-driven, minimal server logic, best for key-value lookups and highly cacheable data that rarely needs complex traversal
- **TAO**: Server-aware, maintains MySQL awareness, optimized for graph traversal and relationship queries where data dependencies matter

## Why Dual Systems?

Facebook’s choice to maintain both systems rather than converge on one reflects practical constraints:

1.  **Memcache’s simplicity** makes it lightweight for objects with straightforward cache invalidation patterns
2.  **TAO’s intelligence** eliminates thundering herd problems during cache misses by letting the server handle query logic
3.  **Operational considerations**: Memcache has lighter CPU and memory overhead; TAO can reduce database load for complex queries

## Operational Implications

For most deployments, understanding these architectural tradeoffs matters more than the specific Facebook implementation:

- Use lookaside caches (like Memcache or Redis) for stateless, cacheable data where your application controls freshness
- Use intelligent caching layers for highly connected data or when query-time logic is complex
- Monitor cache hit rates; sustained low hit rates indicate either inadequate TTLs or misaligned data access patterns

The original papers from NSDI’13 and USENIX ATC’13 remain highly relevant for understanding distributed caching at scale, though modern systems like Redis, Dragonfly, and dedicated graph databases have evolved considerably since Facebook published these designs.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
