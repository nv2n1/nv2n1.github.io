---
title: "ipq_read(3)"
name: "ipq_read"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipq_read/"
description: "ipq_read — read queue messages from ip_queue and read into supplied buffer"
---

<h2 class="name">NAME</h2>
<p> ipq_read &#8212; read queue messages from ip_queue and read into supplied buffer </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/linux/netfilter.h">linux/netfilter.h</a>&gt;</code><br />
 <code>#include &lt;<a href="file:/usr/include/libipq.h">libipq.h</a>&gt;</code> </p>
<p> <code>ssize_t ipq_read(const struct ipq_handle *</code><i>h</i><code>, unsigned char *</code><i>buf</i><code>, size_t </code><i>len</i><code>, int </code><i>timeout</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ipq_read</code> function reads a queue message from the kernel and copies it to the memory pointed to by <i>buf</i> to a maximum length of <i>len</i>. </p>
<p> The <i>h</i> parameter is a context handle which must previously have been returned successfully from a call to <code>ipq_create_handle</code>. </p>
<p> The caller is responsible for ensuring that the memory pointed to by <i>buf</i> is large enough to contain <i>len</i> bytes. </p>
<p> The <i>timeout</i> parameter may be used to set a timeout for the operation, specified in microseconds. This is implemented internally by the library via the <code>select</code> system call. A value of zero provides normal, backwards-compatible blocking behaviour with no timeout. A negative value causes the function to return immediately. </p>
<p> Data returned via <i>buf</i> should not be accessed directly. Use the <code>ipq_message_type</code>, <code>ipq_get_packet</code>, and <code>ipq_get_msgerr</code> functions to access the queue message in the buffer.</p>
<h2>RETURN VALUE</h2>
<p> On failure, -1 is returned.<br />
 On success, a non-zero positive value is returned when no timeout value is specified.<br />
 On success with a timeout value specified, zero is returned if no data was available to read, or if a non-blocked signal was caught. In the latter case, the global <code>errno</code> value will be set to <code>EINTR</code>.</p>
<h2>ERRORS</h2>
<p> On error, a descriptive error message will be available via the <code>ipq_errstr</code> function.</p>
<h2>DIAGNOSTICS</h2>
<p> While the <code>ipq_read</code> function may return successfully, the queue message copied to the buffer may itself be an error message from a higher level kernel component. Use <code>ipq_message_type</code> to determine if it is an error message, and <code>ipq_get_msgerr</code> to access the value of the message.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> James Morris &lt;jmorris [at] intercode.com.au&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2001 Netfilter Core Team. </p>
<p> Distributed under the GNU General Public License.</p>
<h2>CREDITS</h2>
<p> Joost Remijn implemented the timeout feature, which appeared in the 1.2.4 release of iptables.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/3-libipq/">libipq</a></code>(3), <code><a href="/docs/linux/man/2-select/">select</a></code>(2). </p>
<h2>Index</h2>
