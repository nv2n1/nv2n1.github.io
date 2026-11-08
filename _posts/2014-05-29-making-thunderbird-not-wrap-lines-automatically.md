---
title: "Disable Auto Line Wrapping in Thunderbird"
date: 2014-05-29 07:30:30 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/making-thunderbird-not-wrap-lines-automatically/
---

Thunderbird wraps lines at 72 characters by default—a sensible standard from the SMTP era, but one that can break formatting when sending code, logs, or plain text that needs to stay on single lines. The fix is straightforward: tell Thunderbird to let the recipient’s client handle line breaking instead.

## Access the Config Editor

1.  Open **Preferences** (Linux/Windows) or **Settings** (macOS)
2.  Navigate to the **Advanced** tab
3.  Select the **General** subtab
4.  Click **Config Editor…**

A warning dialog appears. Click through it to access the advanced configuration interface.

## Configure the Wrapping Settings

Search for these two preferences in the config editor and modify them:

**`mail.compose.wrap_to_window_width`** — Set to `true`

This wraps text *visually* to your composer window width during editing for readability, but doesn’t insert hard line breaks into the message. This is purely a visual convenience while you’re drafting.

**`mailnews.wraplength`** — Set to `0`

This prevents hard line breaks from being inserted when the message is sent. A value of `0` disables wrapping entirely; the default is `72`. This is the critical setting for preserving long lines.

## Why This Matters

Different email clients render text differently. A 72-character wrap imposed by the sender can create awkward breaks on mobile clients, web interfaces, terminal emulators, or markdown renderers. By disabling sender-side wrapping, you preserve the original structure and let each recipient’s application decide how to display the content.

This is especially important when:

- Sending code snippets or terminal output
- Sharing configuration files or logs
- Working with monospaced text that relies on alignment
- Communicating with systems that parse email bodies programmatically

**Plain text only**: These settings apply only to plain-text composition. HTML mail uses different rendering rules and these settings have minimal effect. For technical communication, plain-text mode with wrapping disabled gives you the most predictable control.

## Verify the Change

After modifying these values:

1.  Restart Thunderbird
2.  Compose a new plain-text email with a long line (at least 80+ characters, no manual line breaks)
3.  Send it to yourself or a test account
4.  Open the received message and verify the long line remains unbroken

Check both the message body and any quoted text. If wrapping still occurs, confirm both settings are correct and restart Thunderbird again.

## Reverting to Defaults

If you need to restore default behavior:

- Set `mailnews.wraplength` back to `72`
- Set `mail.compose.wrap_to_window_width` back to `false`

These settings take effect immediately; no restart is required to change them, only to change the sending behavior.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
