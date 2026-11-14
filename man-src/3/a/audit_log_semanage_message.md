---
title: "audit_log_semanage_message(3)"
name: "audit_log_semanage_message"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_log_semanage_message/"
description: "audit_log_semanage_message – log a semanage message"
---

<h2>NAME</h2>
<p> audit_log_semanage_message &#8211; log a semanage message</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> <code>int audit_log_semanage_message(int audit_fd, int type,</code> <code>const char *pgname, const char *op, const char *name, unsigned int id,</code> <code>const char *new_seuser, const char *new_role, const char *new_range,</code> <code>const char *old_seuser, const char *old_role, const char *old_range,</code> <code>const char *host, const char *addr, const char *tty, int result)</code> </p>
<h2>DESCRIPTION</h2>
<p> This function will log a message to the audit system using a predefined message format. It should be used for all SE linux user and role manipulation operations. The function parameters are as follows: </p>
<pre><code>
audit_fd - The fd returned by audit_open
type - type of message: AUDIT_ROLE_ASSIGN/REMOVE for changing any SE Linux user or role attributes.
pgname - program's name
op  -  operation. "adding-user", "adding-role", "deleting-user", "deleting-role"
name - user's account. If not available use NULL.
id  -  uid that the operation is being performed on. This is used only when name is NULL.
new_seuser - the new seuser that the login user is getting
new_role - the new_role that the login user is getting
new_range - the new mls range that the login user is getting
old_seuser - the old seuser that the login usr had
old_role - the old role that the login user had
old_range - the old mls range that the login usr had
host - The hostname if known
addr - The network address of the user
tty  - The tty of the user
result - 1 is "success" and 0 is "failed"
</code></pre>
<h2>RETURN VALUE</h2>
<p> It returns the sequence number which is &gt; 0 on success or &lt;= 0 on error. </p>
<h2>ERRORS</h2>
<p> This function returns -1 on failure. Examine errno for more info. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_log_user_message/">audit_log_user_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_acct_message/">audit_log_acct_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_avc_message/">audit_log_user_avc_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_comm_message/">audit_log_user_comm_message</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
