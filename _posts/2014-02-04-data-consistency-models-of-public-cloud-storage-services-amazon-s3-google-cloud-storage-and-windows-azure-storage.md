---
title: "Cloud Storage Consistency Models: S3, GCS, and Azure Storage"
date: 2014-02-04 13:48:31 +0000
layout: post
canonical: https://www.systutorials.com/data-consistency-models-of-public-cloud-storage-services-amazon-s3-google-cloud-storage-and-windows-azure-storage/
---

Choosing the right cloud storage service requires understanding how each platform handles data consistency. This post covers the current consistency guarantees from the three major providers and how they affect your application design.

## Amazon S3

S3 is a key-based object store built for Internet-scale workloads. The consistency model is now straightforward across all operations.

S3 provides **strong read-after-write consistency** for:

- PUTs of new objects
- Overwrites of existing objects
- DELETE operations
- Both initial and subsequent requests to the same object

All updates to a single object key are atomic. The exceptions that existed in earlier S3 documentation—regarding HEAD or GET requests before object creation—have been eliminated. S3 now guarantees strong consistency uniformly.

List operations behave differently. The `ListObjects` and `ListObjectsV2` APIs are **eventually consistent by default**, meaning they may temporarily miss recently added or deleted objects. If you need immediate consistency on list results, you’ll need to track object keys separately or use DynamoDB for metadata.

**Practical impact:** Most applications can rely on strong consistency for individual object operations. Plan for eventual consistency on list operations and implement polling or event notifications (via S3 Event Notifications or EventBridge) if you need to detect changes immediately.

## DynamoDB

DynamoDB is a fully managed NoSQL database with explicit consistency options per read operation.

**Read consistency options:**

- **Strongly consistent reads:** Guaranteed to reflect all successful writes before the read. Costs 2× read capacity units.
- **Eventually consistent reads (default):** May return stale data immediately after a write. Uses standard read capacity.

Write operations always provide strong consistency—all writes are immediately durable and visible to subsequent reads. You don’t choose consistency for writes.

**When to use each:**

- Inventory systems, bank account balances, or any operation where stale reads cause problems: use strong consistency
- Analytics, reporting, caches, or user session data: use eventual consistency to reduce costs
- Hybrid approaches: perform strongly consistent reads for critical path operations and eventually consistent reads for secondary data

DynamoDB’s flexible model lets you optimize cost per operation. However, this requires disciplined application code—developers must understand why each read uses its chosen consistency level.

## Google Cloud Storage

Google Cloud Storage provides strong consistency for most operations within regions, with some nuances around access control and caching.

**Consistency guarantees:**

- Strong consistency for upload and delete operations (within and across regions as of 2025)
- Strong consistency for object list operations within a region
- Eventual consistency for cross-region object list operations
- Strong consistency for access control grants
- Eventual consistency for access control revocations (permission removals may take several minutes to propagate globally)
- All upload operations are atomic

**Caching caveat:** When objects are cached—particularly publicly readable objects served through CDN or Google’s own edge caches—the cache layer serves data according to its TTL and invalidation policy. This is separate from storage consistency. A cached object may be stale relative to the current version in GCS, but that’s expected CDN behavior, not a storage consistency issue.

**Practical impact:** Cloud Storage is reliable for applications needing strong read-after-write semantics. Access control changes take time to propagate, so plan for gradual permission updates in security-sensitive workflows.

## Azure Storage

Azure Storage guarantees strong consistency across all operations—a design that balances the CAP theorem constraints through careful replication.

**Azure provides:**

- Strong consistency for all read operations after writes complete
- Atomic operations on individual blobs
- High availability through zone and region redundancy
- Partition tolerance via geo-replication

Azure achieves this through synchronous replication within a region, making strong consistency the default behavior without performance tradeoffs that other systems face.

**Replication options:**

- **Locally redundant storage (LRS):** Cost-effective, strong consistency, single region
- **Geo-redundant storage (GRS):** Cross-region durability, but secondary regions offer only eventual consistency (read-only until failover)
- **Zone-redundant storage (ZRS):** Strong consistency across availability zones within a region
- **Geo-zone-redundant storage (GZRS):** Zone redundancy in primary region, geo-replication to secondary

Choose LRS or ZRS if your workload requires guaranteed strong consistency everywhere. Use GRS if you tolerate eventual consistency in secondary regions or only need the secondary for disaster recovery.

## Comparison and Selection

| Service | Object Writes | Object Reads | List Operations | Cost Consistency |
|----|----|----|----|----|
| S3 | Strong | Strong | Eventually consistent | Standard billing |
| Cloud Storage | Strong | Strong | Strong (same region) | Standard billing |
| Azure Storage | Strong | Strong | Strong | Strong consistency is default |
| DynamoDB | Strong | Strong or eventual (your choice) | Eventually consistent by default | Pay per consistency level |

**Selection guidance:**

- **S3:** Default for object storage. Strong consistency on objects, eventual consistency on lists. Integrate with SNS/SQS for change notifications if you need immediate awareness of new/deleted objects.
- **Cloud Storage:** Tighter integration with Google services (BigQuery, Dataflow, Vertex AI). Strong regional consistency out of the box.
- **Azure Storage:** When strong consistency everywhere matters and you’re committed to the Azure ecosystem. Avoids consistency-related bugs in distributed systems.
- **DynamoDB:** When you need structured data with fine-grained consistency control per operation. Higher operational complexity but better cost optimization for read-heavy workloads.

The consistency choice impacts latency, cost, and application complexity. Weak consistency reduces latency and cost but requires defensive application code to handle stale reads. Strong consistency simplifies application logic but may increase latency on secondary regions or cost more. Understand your tolerance for stale data before committing to a service.
