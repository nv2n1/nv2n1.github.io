---
title: "Configuring Thunderbird\u2019s Default Sort Order and Reply Quoting"
date: 2013-07-12 16:54:48 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /default-descending-sort-order-and-inline-quote-when-reply-in-thunderbird/
---

Thunderbird’s most powerful settings live outside the UI—buried in the config editor or preferences file. This guide covers setting emails to sort newest-first by default and enabling inline quoting for replies, two changes that significantly improve daily usability.

## Accessing the Config Editor

Open the config editor at **Edit → Preferences → Advanced → Config Editor**, or search “config” in the preferences search bar. Dismiss the warning and proceed.

## Set Default Descending Sort Order

To display emails newest-first by default across all folders:

    mailnews.default_sort_order = 2

Values:

- `1` = ascending (oldest first)
- `2` = descending (newest first)

This applies only to folders without an explicit manual sort preference. Once you manually sort a folder, it retains that preference independently. To reset all folders to the default, you’ll need to edit `prefs.js` directly or clear the folder cache.

## Enable Inline Quoting for Replies

By default, Thunderbird blocks quoted text at the top of replies. To switch to inline quoting—inserting the original message throughout your response so you can reply point-by-point:

    mail.reply_quote_inline = true

Set to `false` to revert to block quoting. This only affects new replies; existing emails don’t change retroactively.

## Related Reply Settings

Fine-tune other reply behavior with these options:

**Quote prefix for plain text:**

    mail.compose.quoteprefixes.plain_text = >

Default is `>`. Change to `|`, `>>`, `---`, or any custom string.

**Include original message by default:**

    mail.identity.default.quote_original = true

Set to `false` for blank replies; manually add quotes when needed.

**Prevent self-reply loops with multiple accounts:**

    mail.compose.reply_to_self_check_all_identities = true

Stops accidental circular replies when replying to emails from your own addresses.

**Disable false-positive attachment warnings:**

    mail.compose.warn_on_send_outside_attachment = true

Toggle to `false` if you’re tired of warnings about mentioned-but-missing attachments.

## Creating New Config Values

If a preference doesn’t exist, create it. Right-click in the config editor, select **New**, and choose:

- **Boolean** for true/false values
- **String** for text values
- **Integer** for numeric values

Enter the preference name and value, then restart Thunderbird.

## Applying Changes

Close and restart Thunderbird after any config modification. Changes don’t take effect while the application runs. Be aware that major version upgrades can reset or override custom settings—if preferences revert after updating, reapply them using the same process.

## Editing prefs.js Directly

For bulk changes, backups, or multi-machine deployments, edit the preferences file directly.

**Close Thunderbird completely**, then navigate to your profile:

- **Linux:** `~/.thunderbird/[profile-name]/`
- **macOS:** `~/Library/Thunderbird/Profiles/[profile-name]/`
- **Windows:** `%APPDATA%\Thunderbird\Profiles\[profile-name]\`

Open `prefs.js` in a text editor and add or modify lines:

    user_pref("mailnews.default_sort_order", 2);
    user_pref("mail.reply_quote_inline", true);
    user_pref("mail.compose.quoteprefixes.plain_text", ">");
    user_pref("mail.identity.default.quote_original", true);

Save the file, restart Thunderbird, and changes apply immediately. This method is ideal for managing Thunderbird across multiple machines or automating deployment configs.

## 2026 Best Practices and Advanced Techniques

For Configuring Thunderbird’s Default Sort Order and Reply Quoting, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
