---
title: "Comments in Page Margins: Printing with LibreOffice"
date: 2020-10-18 00:20:46 +0000
author: "David Wong"
layout: post
categories: [programming-languages]
canonical: /how-to-print-comments-in-page-margins-in-libreoffice/
---

Comments and tracked changes are essential features for collaborative document work in LibreOffice. Both ODT and DOCX/DOC formats preserve comments and revisions, but controlling how they appear in printed output requires specific configuration.

## Accessing the Print Comments Settings

To print comments in the page margins:

1.  Open your document in LibreOffice Writer
2.  Go to **File \> Print** (or press Ctrl+P)
3.  Click the **LibreOffice Writer** tab in the Print dialog
4.  Locate the **Comments** dropdown field
5.  Select **Place in margins** from the available options
6.  Print to your printer or export as PDF

The comments will now appear in the document margins when printed, making them visible alongside the document text.

## Comment Display Options

The **Comments** dropdown in the LibreOffice Writer print tab offers several options:

- **Do not print**: Comments are excluded from the printed output (default for most users)
- **Place in margins**: Comments appear in the page margins with reference marks pointing to their locations in the text
- **Place at end of document**: All comments are collected and printed after the main document content
- **Only marks**: Displays only the comment markers without the actual comment text

Choose the option that best fits your workflow. For most collaborative editing scenarios, “Place in margins” provides the clearest visual context.

## Working with Tracked Changes

If your document also contains tracked changes (insertions, deletions, formatting changes), the print dialog has a separate section for controlling their appearance:

- **Show changes**: Prints the document with tracked changes visible using markup
- **Hide changes**: Prints the final document as if all changes were accepted
- **Show only**: Lets you print only the changes without the document body (useful for review)

## Practical Example

When reviewing a document with multiple reviewers:

1.  Ensure tracked changes are enabled: **Edit \> Track Changes \> Record**
2.  Make your edits and add comments as needed
3.  When ready to print for a meeting: **File \> Print**
4.  Set Comments to **Place in margins**
5.  Set Changes to **Show changes**
6.  Export as PDF to maintain formatting and share with others

This combination ensures reviewers see exactly where changes occur and can read associated comments without switching between screens.

## Export Considerations

When exporting to PDF with comments in margins:

- Use **File \> Export as PDF** instead of printing to a PDF printer for better formatting control
- The PDF will preserve margin layout exactly as configured
- Comments remain interactive in the PDF if you choose to embed them in the export settings

## Format Compatibility

Comments and margin placement work consistently across:

- Native ODF formats (ODT, ODS)
- Microsoft Office formats (DOCX, XLSX)
- Legacy formats (DOC, XLS)

However, some specialized comment properties may not transfer perfectly between formats. Test your workflow with the formats you actually use before relying on it for critical reviews.

## 2026 Best Practices and Advanced Techniques

For Comments in Page Margins: Printing with LibreOffice, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
