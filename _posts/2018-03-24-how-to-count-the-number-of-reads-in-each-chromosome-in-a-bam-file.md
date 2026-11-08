---
title: "Counting reads per chromosome in BAM files"
date: 2018-03-24 11:53:27 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-count-the-number-of-reads-in-each-chromosome-in-a-bam-file/
---

BAM files store aligned sequence reads in a compressed binary format. Counting reads by chromosome is a common task in genomics workflows—useful for quality control, coverage analysis, and identifying potential sequencing biases.

## Using samtools idxstats

The fastest and most straightforward approach is `samtools idxstats`, which requires an indexed BAM file:

``` bash
samtools index reads.bam
samtools idxstats reads.bam
```

Output format:

    chr1    248956422    1000    50
    chr2    242193529    2000    75
    chrX    155270560    500     10
    *       0            0       100

Columns are: reference sequence name, reference length, mapped reads, unmapped reads.

To sort by read count (descending):

``` bash
samtools idxstats reads.bam | sort -k3 -rn
```

To extract just chromosome names and counts:

``` bash
samtools idxstats reads.bam | cut -f1,3
```

## Using samtools flagstat for Overall Statistics

If you need aggregate read statistics across all chromosomes:

``` bash
samtools flagstat reads.bam
```

This shows total reads, properly paired reads, singletons, duplicates, and other QC metrics, but doesn’t break down by chromosome.

## Filtering and Counting Specific Chromosomes

To count reads mapping to a specific chromosome:

``` bash
samtools view -c reads.bam chr1
```

For multiple chromosomes:

``` bash
samtools view -c reads.bam chr1 chr2 chr3
```

To count only properly paired, mapped reads:

``` bash
samtools view -c -F 4 reads.bam chr1
```

The `-F 4` flag excludes unmapped reads. Use `-f 2` to count only properly paired reads.

## Advanced: Using samtools coverage

For a more detailed view of read distribution across chromosomes:

``` bash
samtools coverage reads.bam
```

This provides per-region coverage statistics including average depth and percentage covered.

## Counting Reads in Shell Scripts

For automated pipelines, combine `samtools view` with awk or Python:

``` bash
samtools view reads.bam | \
  awk '{print $3}' | \
  sort | uniq -c | \
  awk '{print $2, $1}'
```

This extracts chromosome names (column 3), counts occurrences, and formats output as `chromosome read_count`.

Or using a Python one-liner:

``` bash
python3 -c "
import sys
from collections import defaultdict
counts = defaultdict(int)
for line in sys.stdin:
    chrom = line.split('\t')[2]
    counts[chrom] += 1
for chrom in sorted(counts.keys()):
    print(f'{chrom} {counts[chrom]}')
" < <(samtools view reads.bam)
```

## Performance Considerations

- **idxstats** is fastest for indexed BAM files (O(1) lookup)
- **view + counting** scans the entire file and is slower for large BAMs
- Always index your BAM files: `samtools index reads.bam` creates a `.bai` file
- For remote BAM files (S3, HTTP), ensure your indexing tool supports the storage backend

## Handling Edge Cases

Unmapped reads in BAM files appear with chromosome name `*`. The `idxstats` output includes these separately in the fourth column, so filter them out if needed:

``` bash
samtools idxstats reads.bam | grep -v '^\*'
```

For reads aligned to secondary or supplementary alignments, use appropriate SAM flags:

``` bash
samtools view -F 2048 reads.bam chr1 | wc -l
```

The `-F 2048` flag excludes supplementary alignments.

## Verifying Results

Cross-check your counts:

``` bash
samtools view -c reads.bam  # Total mapped reads
samtools idxstats reads.bam | awk '{sum+=$3} END {print sum}'  # Should match above
```

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Counting reads per chromosome in BAM files with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Counting reads per chromosome in BAM files. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
