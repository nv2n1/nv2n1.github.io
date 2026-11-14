---
title: "audit_log_user_message(3)"
name: "audit_log_user_message"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_log_user_message/"
description: "audit_log_user_message – log a general user message"
---

<h2>NAME</h2>
<p> audit_log_user_message &#8211; log a general user message</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_log_user_message(int audit_fd, int type, const char *message, const char *hostname, const char *addr, const char *tty, int result) </p>
<h2>DESCRIPTION</h2>
<p> This function will log a message to the audit system using a predefined message format. This function should be used by all ELF console apps that do not manipulate accounts or groups. If the application is written in Python or another interpreter, then use the <i>audit_log_user_comm_message</i> function instead. The function parameters are as follows: </p>
<pre><code>
audit_fd - The fd returned by audit_open type - type of message, ex : AUDIT_USYS_CONFIG, AUDIT_USER_LOGIN message - the message text being sent hostname - the hostname if known, NULL if unknown addr - The network address of the user, NULL if unknown tty - The tty of the user, if NULL will attempt to figure out result - 1 is "success" and 0 is "failed"
</code></pre>
<h2>RETURN VALUE</h2>
<p> It returns the sequence number which is &gt; 0 on success or &lt;= 0 on error. </p>
<h2>ERRORS</h2>
<p> This function returns -1 on failure. Examine errno for more info. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_log_user_comm_message/">audit_log_user_comm_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_acct_message/">audit_log_acct_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_avc_message/">audit_log_user_avc_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_semanage_message/">audit_log_semanage_message</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
