---
title: "audit_set_pid(3)"
name: "audit_set_pid"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_set_pid/"
description: "audit_set_pid – Set audit daemon process ID"
---

<h2>NAME</h2>
<p> audit_set_pid &#8211; Set audit daemon process ID</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_set_pid (int fd, int pid); </p>
<h2>DESCRIPTION</h2>
<p> audit_set_pid tells the kernel what the pid is of the audit daemon. When the pid is set to 0, the kernel will log all events to syslog. Otherwise it will try to send events to the netlink connection that has the same pid given by this function. If for some reason the process goes away, the kernel will automatically set the value to 0 itself. Usually this function is called by the audit daemon and not an external program. </p>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
