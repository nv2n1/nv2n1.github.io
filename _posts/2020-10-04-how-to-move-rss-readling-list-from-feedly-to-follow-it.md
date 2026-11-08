---
title: "Migrating Your Feedly RSS Feeds to Follow.it"
date: 2020-10-04 08:53:30 +0000
author: "David Yang"
layout: post
canonical: https://www.systutorials.com/how-to-move-rss-readling-list-from-feedly-to-follow-it/
---

RSS feed readers have become essential for staying on top of content from multiple sources. If you’re switching from Feedly to Follow.it, the migration is straightforward — both services support OPML (Outline Processor Markup Language), a standard format for exporting and importing feed lists.

## Export Your Feed List from Feedly

Feedly makes exporting your feeds simple:

1.  Log into your Feedly account
2.  Click the gear icon next to “FEEDS” in the left sidebar
3.  Select “Export OPML”
4.  You’ll be redirected to `https://feedly.com/i/opml` where a download button appears
5.  Save the `.opml` file to your computer

The export file is a plain XML document containing all your feed URLs and folder structure. If you have hundreds of feeds, the file may take a moment to generate.

## Verify Your OPML File

Before importing, it’s worth checking the exported file. Open it with a text editor to confirm it contains your feeds:

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
  <head>
    <title>Feedly Subscriptions</title>
  </head>
  <body>
    <outline text="Technology" title="Technology">
      <outline type="rss" text="Example Feed" xmlUrl="https://example.com/feed.xml"/>
    </outline>
  </body>
</opml>
```

If the file is empty or malformed, try exporting again.

## Import Into Follow.it

Follow.it’s import process is equally straightforward:

1.  Log into your Follow.it account
2.  Navigate to the Discovery section or go directly to `https://follow.it/mass-follow`
3.  Click on the “Mass Follow” tab
4.  Look for the OPML upload option — you can either drag and drop your file or click to browse
5.  Select your exported Feedly OPML file
6.  Follow.it will process the file and begin subscribing to all feeds

The import can take several minutes for large feed lists. Follow.it will display progress and notify you when complete. Any feeds that no longer exist or are inaccessible will be flagged so you can remove them manually.

## Post-Migration Cleanup

After importing, check your feeds in Follow.it:

- Verify all feeds imported successfully by reviewing your subscription count
- Organize feeds into Follow.it’s collection system if needed (different from Feedly’s folder structure)
- Test that feeds are actively updating with new content
- Remove any duplicate subscriptions or broken feeds
- Configure Follow.it-specific features like keyword filtering or newsletter settings

## Troubleshooting Common Issues

**Missing feeds after import:** Some feeds may fail to import if Follow.it can’t reach them or if they’re malformed. Check if the feed URL is still valid by pasting it into your browser.

**Folder structure not preserved:** Follow.it may not maintain Feedly’s exact folder hierarchy. You’ll need to reorganize subscriptions manually using Follow.it’s collections feature if organization matters to your workflow.

**Import takes too long:** Large imports (500+ feeds) can take 10-30 minutes. Don’t close the tab or refresh during the process.

## Alternative: Command-Line Approach

For those comfortable with command line, you can parse the OPML file and extract just the feed URLs:

``` bash
grep -oP 'xmlUrl="\K[^"]+' feedly.opml > feeds.txt
```

This creates a simple list of URLs that Follow.it can also import, useful if you need to filter or edit feeds before importing.

The OPML standard ensures you’re never locked into a single reader — switching services is always possible as long as both support this format.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Migrating Your Feedly RSS Feeds to Follow.it with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Migrating Your Feedly RSS Feeds to Follow.it. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
