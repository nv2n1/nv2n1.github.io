---
title: "Enabling Email Auto-Completion in Evolution"
date: 2018-03-24 11:55:04 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-email-email-address-auto-completion-in-evolution/
---

GNOME Evolution’s email address auto-completion works by querying your local address books and, optionally, external sources. Here’s how to get it working properly.

## Check Your Address Books

Evolution pulls auto-completion suggestions from multiple sources:

- Personal address book (local contacts you’ve added)
- On This Computer (system-wide contacts)
- Synced contact sources (Google, CalDAV, CardDAV, LDAP)

To see what address books Evolution is currently using, navigate to **Contacts** in the sidebar and verify which books appear. If you’re missing contacts, they might be in a source that’s not enabled for auto-completion.

## Enable Auto-completion in Preferences

1.  Open **Edit → Preferences**
2.  Go to the **Composer** section
3.  Look for the option **“Check for recipients in external address books”** and ensure it’s enabled
4.  In the same section, you can control which address books Evolution searches during composition

If you’re using Evolution 3.50 or later, there’s also a search ranking option that weights which address books to check first—useful when you have multiple sources.

## Sync Contacts from Online Accounts

For cloud-based contacts, use GNOME Online Accounts to integrate them directly into Evolution:

1.  Open **Settings → Online Accounts**
2.  Add your Google, Microsoft, or other supported account
3.  Toggle **Contacts** to enable syncing
4.  Evolution will automatically sync those contacts into its database

This approach is more reliable than IMAP-only setups because Evolution maintains a local copy of contacts, making auto-completion instant even during network latency.

## LDAP Directory Search

For corporate environments, Evolution can query LDAP directories during composition:

1.  Go to **Preferences → Composer**
2.  Enable **“Autocomplete from LDAP address books”**
3.  Configure your LDAP server details in **Preferences → Calendar and Tasks** (LDAP settings are shared across Evolution)

Common LDAP configuration:

- Server: your-company-ldap.example.com
- Port: 389 (or 636 for TLS)
- Bind DN: Leave empty for anonymous searches (if allowed)
- Base DN: ou=people,dc=company,dc=com

## Troubleshooting Auto-completion Issues

**Auto-completion is slow:** This typically happens with large address books or when querying remote LDAP servers. Evolution caches results, so the first search is slower but subsequent ones are faster.

**Contacts not appearing:** Verify the address book is actually synced. Check **Contacts** sidebar—if a source shows zero entries, the sync failed. Try disconnecting and re-adding the account in GNOME Online Accounts.

**Duplicate suggestions:** If Evolution suggests the same contact multiple times, you likely have duplicates across address books. Use the **Contacts** application to merge duplicates before re-enabling auto-completion.

## Evolution Exchange Support

If you’re using Microsoft Exchange, Evolution’s native EWS (Exchange Web Services) support means auto-completion works directly from your server’s GAL (Global Address List) when properly configured. Set up your Exchange account through **Online Accounts**, and the GAL automatically becomes available during composition.

## Performance Tips

- Keep your primary address book under 5000 contacts for snappy auto-completion
- If using multiple LDAP servers, disable ones you rarely query
- Evolution’s auto-completion is single-threaded, so very large LDAP queries can briefly freeze the compose window—this is expected behavior

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Enabling Email Auto-Completion in Evolution with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Enabling Email Auto-Completion in Evolution. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
