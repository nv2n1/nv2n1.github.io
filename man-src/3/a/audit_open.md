---
title: "audit_open(3)"
name: "audit_open"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_open/"
description: "audit_open – Open a audit netlink socket connection"
---

<h2>NAME</h2>
<p> audit_open &#8211; Open a audit netlink socket connection</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_open (void); </p>
<h2>DESCRIPTION</h2>
<p> audit_open creates a NETLINK_AUDIT socket for communication with the kernel part of the Linux Audit Subsystem. The audit system uses the ACK feature of netlink. This means that every message to the kernel will return a netlink status packet even if the operation succeeds. </p>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs; otherwise, the return value is a descriptor referencing the socket. </p>
<h2>ERRORS</h2>
<p> The <code>audit_open</code>() function may fail and set <i>errno</i> for any of the errors specified for the <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) and <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) routines. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
