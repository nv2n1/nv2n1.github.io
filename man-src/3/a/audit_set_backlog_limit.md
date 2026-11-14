---
title: "audit_set_backlog_limit(3)"
name: "audit_set_backlog_limit"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_set_backlog_limit/"
description: "audit_set_backlog_limit – Set the audit backlog limit"
---

<h2>NAME</h2>
<p> audit_set_backlog_limit &#8211; Set the audit backlog limit</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_set_backlog_limit (int fd, int limit); </p>
<h2>DESCRIPTION</h2>
<p> audit_set_backlog_limit sets the queue length for audit events awaiting transfer to the audit daemon. The default value is 64 which can potentially be overrun by bursts of activity. When the backlog limit is reached, the kernel consults the failure_flag to see what action to take. </p>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_set_failure/">audit_set_failure</a></code>(3), <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
