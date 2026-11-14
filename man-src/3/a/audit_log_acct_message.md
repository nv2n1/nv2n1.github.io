---
title: "audit_log_acct_message(3)"
name: "audit_log_acct_message"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_log_acct_message/"
description: "audit_log_acct_message – log a user account message"
---

<h2>NAME</h2>
<p> audit_log_acct_message &#8211; log a user account message</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_log_acct_message(int audit_fd, int type, const char *pgname, const char *op, const char *name, unsigned int id, const char *host, const char *addr, const char *tty, int result) </p>
<h2>DESCRIPTION</h2>
<p> This function will log a message to the audit system using a predefined message format. It should be used for all account manipulation operations. The function parameters are as follows: </p>
<dl>
<dt>
<dd>
<dl>
<dt>audit_fd &#8211; The fd returned by audit_open</p>
<dd>
<dt>type &#8211; type of message: AUDIT_USER_CHAUTHTOK for changing any account attributes.</p>
<dd>
<dt>pgname &#8211; program&#8217;s name, if NULL will attempt to figure out</p>
<dd>
<dt>op &#8211; operation. Ex: &quot;adding-user&quot;, &quot;changing-finger-info&quot;, &quot;deleting-group&quot;. This value should have a dash or underscore between the words so that report parsers group them together.</p>
<dd>
<dt>name &#8211; user&#8217;s account or group name. If not available use NULL.</p>
<dd>
<dt>id &#8211; uid or gid that the operation is being performed on. If the user is unknown, pass a -1 and fill in the name parameter. This is used only when user is NULL.</p>
<dd>
<dt>host &#8211; The hostname if known. If not available pass a NULL.</p>
<dd>
<dt>addr &#8211; The network address of the user. If not available pass a NULL.</p>
<dd>
<dt>tty &#8211; The tty of the user, if NULL will attempt to figure out</p>
<dd>
<dt>result &#8211; 1 is &quot;success&quot; and 0 is &quot;failed&quot;</p>
<dd></dl>
</dl>
<h2>RETURN VALUE</h2>
<p> It returns the sequence number which is &gt; 0 on success or &lt;= 0 on error. </p>
<h2>ERRORS</h2>
<p> This function returns -1 on failure. Examine errno for more info. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_log_user_message/">audit_log_user_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_comm_message/">audit_log_user_comm_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_user_avc_message/">audit_log_user_avc_message</a></code>(3), <code><a href="/docs/linux/man/3-audit_log_semanage_message/">audit_log_semanage_message</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
