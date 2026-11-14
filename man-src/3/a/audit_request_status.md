---
title: "audit_request_status(3)"
name: "audit_request_status"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_request_status/"
description: "audit_request_status – Request status of the audit system"
---

<h2>NAME</h2>
<p> audit_request_status &#8211; Request status of the audit system</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_request_status (int fd); </p>
<h2>DESCRIPTION</h2>
<p> audit_request_status requests that the kernel send status structure describing various settings. The audit_status structure is as follows: </p>
<dl>
<dt>
<dd>
<pre><code>
struct audit_status {
    __u32 mask;          /* Bit mask for valid entries */
    __u32 enabled;       /* 1 = enabled, 0 = disabled */
    __u32 failure;       /* Failure-to-log action */
    __u32 pid;           /* pid of auditd process */
    __u32 rate_limit;    /* messages rate limit (per second) */
    __u32 backlog_limit; /* waiting messages limit */
    __u32 lost;          /* messages lost */
    __u32 backlog;       /* messages waiting in queue */
};
</code></pre>
</dl>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3), <code><a href="/docs/linux/man/3-audit_get_reply/">audit_get_reply</a></code>(3), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
