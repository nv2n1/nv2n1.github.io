---
title: "Importing Evolution Mail to Thunderbird via IMAP"
date: 2018-03-24 08:19:32 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/import-evolution-mail-directory-to-thunderbird-imap-account/
---

If you have emails stuck in Evolution’s local directory structure that you want to move to an IMAP account via Thunderbird, you’ll need to convert them to a format Thunderbird can import, then push them to your mail server.

## Step 1: Prepare Your Evolution Mail Directory

Evolution typically stores mail in a Maildir format with this structure:

    folder/
    ├── cur/
    ├── new/
    └── tmp/

If your emails are scattered in Evolution’s mail directory but not in this structure, organize them first. Copy all individual email files into the `new/` subdirectory:

``` bash
mkdir -p evolution_export/new
cp /path/to/evolution/mail/*.mbox evolution_export/new/ 2>/dev/null || true
# Or if individual message files:
cp /path/to/evolution/mail/your_folder/* evolution_export/new/
```

## Step 2: Convert Maildir to mbox Format

Modern tooling makes this straightforward. You have several options:

**Using Python (recommended for accuracy):**

``` bash
# Install mailbox conversion utility
pip install maildir2mbox

# Convert the directory
maildir2mbox evolution_export output.mbox
```

**Using Thunderbird’s built-in tools (Thunderbird 78+):**

Thunderbird now includes native Maildir import capabilities. Import directly without conversion in some cases, but mbox remains more reliable for complex migrations.

**Manual conversion with a simple script:**

``` bash
#!/bin/bash
# Convert Maildir to mbox format
MAILDIR="$1"
OUTPUT="$2"

> "$OUTPUT"
for file in "$MAILDIR"/new/*; do
    if [ -f "$file" ]; then
        echo "From - $(date -r "$file" '+%a %b %d %H:%M:%S %Y')" >> "$OUTPUT"
        cat "$file" >> "$OUTPUT"
        echo "" >> "$OUTPUT"
    fi
done
```

## Step 3: Import mbox into Thunderbird

**For Thunderbird 115+ (2024 and later):**

Thunderbird removed ImportExportTools support due to API changes. Use these alternatives:

1.  **Native import method:**

    - File \> Import \> Mail from backup
    - Or: File \> Import \> Import mail from file
    - Select your .mbox file

2.  **ImportExportTools NG** (actively maintained fork):

    - Install from: <a href="https://addons.thunderbird.net/en-US/thunderbird/addon/importexporttools-ng/" rel="nofollow noopener" target="_blank">https://addons.thunderbird.net/en-US/thunderbird/addon/importexporttools-ng/</a>
    - Right-click any folder \> ImportExportTools NG \> Import mbox file

3.  **Automatic method using command line:**

``` bash
# Use Thunderbird's profile backend directly
importmail="${HOME}/.thunderbird/default.xyz/ImapMail/your_server.imap/Trash"
cat output.mbox > "$importmail"
```

## Step 4: Sync Imported Messages to IMAP Server

Once imported into a local Thunderbird folder:

1.  Create a corresponding folder on your IMAP account server (or use existing)
2.  Select all messages in your local folder (Ctrl+A)
3.  Drag them to the IMAP folder, or right-click \> Copy to \> \[IMAP folder\]
4.  Thunderbird will upload them to the server

For bulk operations with many messages, disable Thunderbird’s message threading temporarily to speed up the drag-and-drop process:

    View > Threads > Unthreaded

## Verify the Migration

After syncing, confirm messages reached the IMAP server:

``` bash
# Using IMAP command-line tools (if available)
openssl s_client -connect mail.example.com:993 -crlf
# Then: A001 LOGIN user@example.com password
# A002 SELECT "INBOX"
# A003 SEARCH ALL
```

Or simply check in your mail client’s IMAP folder—new messages should appear within seconds.

## Troubleshooting

- **Duplicate messages:** Thunderbird may create duplicates if messages already exist on the IMAP server. Delete or filter them after sync.
- **Encoding issues:** Some legacy emails may have character encoding problems. mbox conversion tools usually handle this, but check critical messages post-import.
- **Large files:** For mbox files over 500MB, import in batches to avoid memory issues.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Importing Evolution Mail to Thunderbird via IMAP with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Importing Evolution Mail to Thunderbird via IMAP. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
