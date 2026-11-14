---
title: "audit_get_reply(3)"
name: "audit_get_reply"
section: "3"
letter: "a"
url: "/docs/linux/man/3-audit_get_reply/"
description: "audit_get_reply – Get the audit system’s reply"
---

<h2>NAME</h2>
<p> audit_get_reply &#8211; Get the audit system&#8217;s reply</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libaudit.h&gt;</code> </p>
<p> int audit_get_reply(int fd, struct audit_reply *rep, reply_t block, int peek); </p>
<h2>DESCRIPTION</h2>
<p> This function gets the next data packet sent on the audit netlink socket. This function is usually called after sending a command to the audit system. fd should be an open file descriptor returned by audit_open. rep should be a data structure to put the reply in. block is of type reply_t which is either: GET_REPLY_BLOCKING and GET_REPLY_NONBLOCKING. peek, if non-zero, gets the data without dequeueing it from the netlink socket. </p>
<h2>RETURN VALUE</h2>
<p> This function returns -1 on error, 0 if error response received, and positive value on success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-audit_open/">audit_open</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
