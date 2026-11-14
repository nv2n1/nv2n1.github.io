---
title: "audit_log_user_avc_message(3)"
name: "audit_log_user_avc_message"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_log_user_avc_message/"
description: "audit_log_user_avc_message – log a user avc message"
---

<h2>NAME</h2>
<p> audit_log_user_avc_message &#8211; log a user avc message</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> <code>int audit_log_user_avc_message(int audit_fd, int type, const char *message,</code> const char *hostname, const char *addr, const char *tty, uid_t uid) </p>
<h2>DESCRIPTION</h2>
<p> This function will log a message to the audit system using a predefined message format. This function should be used by all apps that are SE Linux object managers. The function parameters are as follows: </p>
<pre>
audit_fd - The fd returned by audit_open
type - type of message, ex: AUDIT_USER_AVC
message - the message being sent
hostname - the hostname if known
addr - The network address of the user
tty - The tty of the user, if NULL will attempt to figure out
uid - The auid of the person related to the avc message
</pre>
<h2>RETURN VALUE</h2>
<p> It returns the sequence number which is &gt; 0 on success or &lt;= 0 on error. </p>
<h2>ERRORS</h2>
<p> This function returns -1 on failure. Examine errno for more info. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_log_user_message/">audit_log_user_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_acct_message/">audit_log_acct_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_avc_message/">audit_log_user_avc_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_semanage_message/">audit_log_semanage_message</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
