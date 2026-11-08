---
title: "How vruntime Changes When Moving Between CPU Run Queues"
date: 2018-03-24 11:51:39 +0000
layout: post
canonical: https://www.systutorials.com/what-is-the-vruntime-of-one-process-after-it-is-moved-into-another-run-queue-in-linux-kernel/
---

When the kernel migrates a process from one CPU’s runqueue to another, the Completely Fair Scheduler (CFS) must adjust the process’s virtual runtime (vruntime) to account for the different scheduling histories of each CPU. This prevents fairness issues where a migrated process could gain an unfair advantage on the destination CPU.

## How vruntime Adjustment Works

The kernel stores `min_vruntime` for each runqueue — a monotonically increasing value that tracks the minimum vruntime of all processes that have run on that CPU. This prevents vruntime from wrapping around and causing scheduling anomalies.

When a process migrates:

1.  **On dequeue (source CPU)**: The process’s vruntime is adjusted downward by subtracting the source runqueue’s `min_vruntime`. This normalizes the vruntime relative to that CPU’s scheduling baseline.

2.  **On enqueue (destination CPU)**: The process’s vruntime is adjusted upward by adding the destination runqueue’s `min_vruntime`. This places the process into the destination CPU’s scheduling timeline.

This two-step normalization ensures the process maintains its fair share position relative to local processes while preventing starvation or unfair scheduling advantages.

## Code Implementation

The relevant kernel code in `kernel/sched/fair.c`:

``` c
// Dequeue from source CPU runqueue
dequeue_entity(struct cfs_rq *cfs_rq, struct sched_entity *se, int flags) {
    ...
    se->vruntime -= cfs_rq->min_vruntime;
    ...
}

// Enqueue to destination CPU runqueue
enqueue_entity(struct cfs_rq *cfs_rq, struct sched_entity *se, int flags) {
    ...
    se->vruntime += cfs_rq->min_vruntime;
    ...
}
```

## Practical Example

Consider two CPUs with different scheduling states:

- **CPU0**: `min_vruntime = 1000000`, process P has `vruntime = 1000500`
- **CPU1**: `min_vruntime = 500000`, initially no waiting processes

When P migrates from CPU0 to CPU1:

1.  Dequeue from CPU0: `vruntime = 1000500 - 1000000 = 500`
2.  Enqueue to CPU1: `vruntime = 500 + 500000 = 500500`

Process P now enters CPU1’s runqueue with a normalized vruntime of 500500, which is fair relative to CPU1’s scheduling baseline.

## Why This Matters

Without this adjustment, two problems occur:

- **Starvation risk**: A migrated process with a high vruntime (in absolute terms) would be starved because it appears to have had more CPU time than local processes
- **Unfair advantage**: A migrated process with a low vruntime would monopolize the CPU because it appears underserved

The normalization ensures migrated processes are scheduled fairly based on their actual CPU consumption, not their position in a different CPU’s timeline.

## Load Balancing Context

Process migration typically occurs during load balancing operations handled by the kernel’s load balancer (scheduler_tick, newidle_balance, idle_balance). The scheduler attempts to distribute processes evenly across CPUs to maximize throughput and minimize latency. The vruntime adjustment is transparent to these load-balancing decisions but critical for maintaining CFS invariants.

Modern kernels (5.10+) also consider cache locality and CPU topology during migration decisions, so not all runqueue imbalances trigger immediate migrations. The vruntime adjustment still applies whenever migration occurs, regardless of the trigger.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers How vruntime Changes When Moving Between CPU Run Queues with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for How vruntime Changes When Moving Between CPU Run Queues. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
