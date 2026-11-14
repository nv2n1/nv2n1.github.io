---
title: "audit_log_user_command(3)"
name: "audit_log_user_command"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_log_user_command/"
description: "audit_log_user_command – log a user command"
---

<h2>NAME</h2>
<p> audit_log_user_command &#8211; log a user command</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> <code>int audit_log_user_command(int audit_fd, int type, const char *command, const char *tty, int result);</code> </p>
<h2>DESCRIPTION</h2>
<p> This function will log a command to the audit system using a predefined message format. It encodes the command as the audit system expects for untrusted strings. This function should be used by all apps need to record commands. The function parameters are as follows: </p>
<pre>
audit_fd - The fd returned by audit_open
type - type of message, ex: AUDIT_USYS_CONFIG, AUDIT_USER_LOGIN
command - the command being logged
tty - The tty of the user, if NULL will attempt to figure out
result - 1 is &quot;success&quot; and 0 is &quot;failed&quot;
</pre>
<h2>RETURN VALUE</h2>
<p> It returns the sequence number which is &gt; 0 on success or &lt;= 0 on error. </p>
<h2>ERRORS</h2>
<p> This function returns -1 on failure. Examine errno for more info. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_log_user_message/">audit_log_user_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_comm_message/">audit_log_user_comm_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_acct_message/">audit_log_acct_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_avc_message/">audit_log_user_avc_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_semanage_message/">audit_log_semanage_message</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
