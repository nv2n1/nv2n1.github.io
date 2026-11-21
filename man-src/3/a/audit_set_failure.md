---
title: "audit_set_failure(3)"
name: "audit_set_failure"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_set_failure/"
description: "audit_set_failure – Set audit failure flag"
---

<h2>NAME</h2>
<p> audit_set_failure &#8211; Set audit failure flag</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_set_failure(int fd, int failure); </p>
<h2>DESCRIPTION</h2>
<p> audit_set_failure sets the action that the kernel will perform when the backlog limit is reached or when it encounters an error and cannot proceed. Possible values are: </p>
<dl>
<dt>0 &#8211; AUDIT_FAIL_SILENT</dt>
<dd> Do nothing, report nothing, skip logging the record and continue. </dd>
<dt>1 &#8211; AUDIT_FAIL_PRINTK [default]</dt>
<dd> Log the audit record using printk which will cause subsequent events to get written to syslog. </dd>
<dt>2 &#8211; AUDIT_FAIL_PANIC</dt>
<dd> Call the panic function. This would be used to prevent use of the machine upon loss of audit events. </dd>
</dl>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code>audit_set_backlog</code>(3), <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8), <code><a href="/docs/linux/man/8-auditctl/">auditctl</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
