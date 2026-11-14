---
title: "audit_set_backlog_wait_time(3)"
name: "audit_set_backlog_wait_time"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_set_backlog_wait_time/"
description: "audit_set_backlog_wait_time – Set the audit backlog wait time"
---

<h2>NAME</h2>
<p> audit_set_backlog_wait_time &#8211; Set the audit backlog wait time</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_set_backlog_wait_time (int fd, int wait_time); </p>
<h2>DESCRIPTION</h2>
<p> audit_set_backlog_wait_time sets the time that the kernel will wait before attempting to send more audit events to be transferred to the audit daemon when the backlog_limit is reached. This gives the audit daemon a chance to drain the kernel queue. The default value is 60000 or 60 * HZ setting in the kernel. </p>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_set_backlog_limit/">audit_set_backlog_limit</a></code>(3), <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
