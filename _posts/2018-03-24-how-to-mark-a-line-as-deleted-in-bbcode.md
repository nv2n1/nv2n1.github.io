---
title: "BBCode Strikethrough: Syntax and Best Practices"
date: 2018-03-24 11:41:17 +0000
layout: post
canonical: https://www.systutorials.com/how-to-mark-a-line-as-deleted-in-bbcode/
---

To mark text as deleted or struck through in BBCode, use the `[s]` tag:

    [s]strikethrough text[/s]

This renders as strikethrough text with a horizontal line through the middle. Some platforms also support the longer `[strike]` alias:

    [strike]strikethrough text[/strike]

Both tags are functionally equivalent — the choice depends on your platform’s BBCode parser.

## HTML Output and Semantic Markup

When a BBCode parser processes strikethrough tags, it converts them to HTML. Which element it uses matters for accessibility and document semantics:

### The `<s>` Element (Standard)

``` html
<s>strikethrough text</s>
```

The `<s>` element is the semantic HTML5 standard for struck-through content. Use this for general strikethrough without implying deletion or removal.

### The `<del>` Element (Semantic Deletion)

``` html
<del>strikethrough text</del>
```

The `<del>` element semantically indicates deleted or removed content. Use this when strikethrough represents text that’s no longer accurate, has been removed, or needs to be distinguished as a change. Pair it with `<ins>` to show replacements:

``` html
The command is <del>ifconfig</del> <ins>ip addr</ins>
```

### CSS Fallback

``` html
<span style="text-decoration: line-through;">strikethrough text</span>
```

Generic span with inline CSS provides styling without semantic meaning. Older or minimal BBCode parsers use this approach, but avoid it in new implementations — semantic markup is better for accessibility and screen readers.

## Common Use Cases in Technical Communities

Strikethrough is widely used in sysadmin and technical forums for:

- **Marking deprecated commands or syntax** — showing what users should stop using while keeping the history visible
- **Indicating corrections** — removing incorrect information without deleting it, preserving discussion context
- **Collaborative editing** — tracking changes in wikis, documentation, or issue trackers
- **Representing rollbacks** — marking decisions or deployments that were undone

## Browser Rendering and Accessibility

All modern browsers render strikethrough consistently across `<s>`, `<del>`, and CSS `text-decoration: line-through`. The visual appearance is identical — a horizontal line through text at approximately the middle height.

However, screen readers handle these differently:

- `<del>` is announced as “deleted” text, providing context to visually impaired users
- `<s>` is typically not announced separately
- CSS-only strikethrough carries no semantic information

**Choose your markup based on intent**: use `<del>` for content removal or changes, `<s>` for general strikethrough, and CSS only when semantic markup isn’t available or applicable.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.

## Comprehensive Guide: 2026 Best Practices

This article provides foundational knowledge for working with BBCode Strikethrough: Syntax and Best Practices. In 2026, modern best practices emphasize security, reproducibility, and automation. Following these guidelines helps maintain clean, maintainable systems.

## Advanced Techniques and Alternatives

While the core commands and methods described in this article work well for most scenarios, advanced users often explore alternative tools for specific edge cases. Always document your custom configurations and configurations to help with troubleshooting and knowledge sharing within your team.

## Troubleshooting Common Issues

When encountering problems, follow a systematic debugging approach. Start with the simplest possible test case to isolate the issue. Check logs and error messages carefully—they often contain direct hints about what went wrong. For system-level issues, verify dependencies are correctly installed and configured before attempting complex workarounds.

## Performance Optimization Tips

- Monitor resource usage regularly to identify bottlenecks
- Use caching strategies where appropriate to reduce redundant computation
- Keep software updated to benefit from security patches and performance improvements
- Profile your code or configuration before applying optimizations
- Document performance baselines to measure the impact of changes

## Related Commands and Tools

These complementary tools and commands are frequently used alongside the topic of this article. Learning them expands your toolkit and makes you more efficient in daily workflows.

- System monitoring: top, htop, iotop for resource tracking
- File operations: find, locate, fd for efficient searching
- Network diagnostics: ping, traceroute, mtr, ss for connectivity checks
- Log analysis: journalctl, dmesg, tail for real-time log monitoring
- Package management: dnf history, apt list –installed, rpm -qa for inventory

## Integration with Modern Workflows

Consider how this technique integrates with modern automation and DevOps practices. Container-based deployments provide consistency across environments. Infrastructure as code tools like Terraform and Ansible enable reproducible configurations. Monitoring and alerting systems ensure timely notification of issues before they impact users.

## 2026 Updates and Changes

As of 2026, many tools and frameworks have introduced new features and deprecated old approaches. Always consult official documentation for your specific version when planning implementations. Community forums and Q&A sites can provide practical workarounds for edge cases not covered in official guides.

## Quick Reference Summary

This article covered essential concepts and practical examples. For deep dives, refer to official documentation or specialized guides. Practice in a test environment before applying changes to production systems.
