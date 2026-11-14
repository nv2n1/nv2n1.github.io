---
title: "ipq_destroy_handle(3)"
name: "ipq_destroy_handle"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipq_destroy_handle/"
description: "ipq_create_handle, ipq_destroy_handle — create and destroy libipq handles."
---

<h2 class="name">NAME</h2>
<p> ipq_create_handle, ipq_destroy_handle &#8212; create and destroy libipq handles. </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/linux/netfilter.h">linux/netfilter.h</a>&gt;</code><br />
 <code>#include &lt;<a href="file:/usr/include/libipq.h">libipq.h</a>&gt;</code> </p>
<p> <code>struct ipq_handle *ipq_create_handle(u_int32_t </code><i>flags</i><code>, u_int32_t </code><i>protocol</i><code>);</code><br />
 <code>int ipq_destroy_handle(struct ipq_handle *</code><i>h</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ipq_create_handle</code> function initialises libipq for an application, attempts to bind to the Netlink socket used by ip_queue, and returns an opaque context handle. It should be the first libipq function to be called by an application. The handle returned should be used in all subsequent library calls which require a handle parameter. </p>
<p> The <i>flags</i> parameter is not currently used and should be set to zero by the application for forward compatibility. </p>
<p> The <i>protocol</i> parameter is used to specify the protocol of the packets to be queued. Valid values are NFPROTO_IPV4 for IPv4 and NFPROTO_IPV6 for IPv6. Currently, only one protocol may be queued at a time for a handle. </p>
<p> The <code>ipq_destroy_handle</code> function frees up resources allocated by <code>ipq_create_handle</code>, and should be used when the handle is no longer required by the application.</p>
<h2>RETURN VALUES</h2>
<p> On success, <code>ipq_create_handle</code> returns a pointer to a context handle.<br />
 On failure, NULL is returned. </p>
<p> On success, <code>ipq_destroy_handle</code> returns zero.<br />
 On failure, -1 is returned.</p>
<h2>ERRORS</h2>
<p> On failure, a descriptive error message will be available via the <code>ipq_errstr</code> function.</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> James Morris &lt;jmorris [at] intercode.com.au&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2001 Netfilter Core Team. </p>
<p> Distributed under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/3-libipq/">libipq</a></code>(3). </p>
<h2>Index</h2>
