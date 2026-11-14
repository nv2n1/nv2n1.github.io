---
title: "ipq_set_verdict(3)"
name: "ipq_set_verdict"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipq_set_verdict/"
description: "ipq_set_verdict — issue verdict and optionally modified packet to kernel"
---

<h2 class="name">NAME</h2>
<p> ipq_set_verdict &#8212; issue verdict and optionally modified packet to kernel </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/linux/netfilter.h">linux/netfilter.h</a>&gt;</code><br />
 <code>#include &lt;<a href="file:/usr/include/libipq.h">libipq.h</a>&gt;</code> </p>
<p> <code>int ipq_set_verdict(const struct ipq_handle *</code><i>h</i><code>, ipq_id_t </code><i>id</i><code>, unsigned int </code><i>verdict</i><code>, size_t </code><i>data_len</i><code>, unsigned char *</code><i>buf</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ipq_set_verdict</code> function issues a verdict on a packet previously obtained with <code>ipq_read</code>, specifing the intended disposition of the packet, and optionally supplying a modified version of the payload data. </p>
<p> The <i>h</i> parameter is a context handle which must previously have been returned successfully from a call to <code>ipq_create_handle</code>. </p>
<p> The <i>id</i> parameter is the packet identifier obtained via <code>ipq_get_packet</code>. </p>
<p> The <i>verdict</i> parameter must be one of:</p>
<dl>
<dt><code>NF_ACCEPT</code></p>
<dd> Accept the packet and continue traversal within the kernel. </p>
<dt><code>NF_DROP</code></p>
<dd> Drop the packet.</p>
<dt><code>NF_QUEUE</code></p>
<dd> Requeue the packet.</dl>
<p> <code>NF_STOLEN</code> and <code>NF_REPEAT</code> are kernel-internal constants and should not be used from userspace as their exact side effects have not been investigated. </p>
<p> The <i>data_len</i> parameter is the length of the data pointed to by <i>buf</i>, the optional replacement payload data. </p>
<p> If simply setting a verdict without modifying the payload data, use zero for <i>data_len</i> and NULL for <i>buf</i>. </p>
<p> The application is responsible for recalculating any packet checksums when modifying packets.</p>
<h2>RETURN VALUE</h2>
<p> On failure, -1 is returned.<br />
 On success, a non-zero positive value is returned.</p>
<h2>ERRORS</h2>
<p> On error, a descriptive error message will be available via the <code>ipq_errstr</code> function.</p>
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
