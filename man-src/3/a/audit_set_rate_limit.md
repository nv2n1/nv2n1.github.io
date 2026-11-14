---
title: "audit_set_rate_limit(3)"
name: "audit_set_rate_limit"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_set_rate_limit/"
description: "audit_set_rate_limit – Set audit rate limit"
---

<h2>NAME</h2>
<p> audit_set_rate_limit &#8211; Set audit rate limit</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_set_rate_limit (int fd, int limit); </p>
<h2>DESCRIPTION</h2>
<p> audit_set_rate_limit will set the maximum number of messages that the kernel will send per second. This can be used to throttle the rate if systems become unresponsive. Of course the trade off is that events will be dropped. The default value is 0, meaning no limit. </p>
<h2>RETURN VALUE</h2>
<p> The return value is &lt;= 0 on error, otherwise it is the netlink sequence id number. This function can have any error that sendto would encounter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
