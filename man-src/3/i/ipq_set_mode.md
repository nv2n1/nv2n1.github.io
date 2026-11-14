---
title: "ipq_set_mode(3)"
name: "ipq_set_mode"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipq_set_mode/"
description: "ipq_set_mode — set the ip_queue queuing mode"
---

<h2 class="name">NAME</h2>
<p> ipq_set_mode &#8212; set the ip_queue queuing mode </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/linux/netfilter.h">linux/netfilter.h</a>&gt;</code><br />
 <code>#include &lt;<a href="file:/usr/include/libipq.h">libipq.h</a>&gt;</code> </p>
<p> <code>int ipq_set_mode(const struct ipq_handle *</code><i>h</i><code>, u_int8_t </code><i>mode</i><code>, size_t </code><i>range</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ipq_set_mode</code> function sends a message to the kernel ip_queue module, specifying whether packet metadata only, or packet payloads as well as metadata should be copied to userspace. </p>
<p> The <i>h</i> parameter is a context handle which must previously have been returned successfully from a call to <code>ipq_create_handle</code>. </p>
<p> The <i>mode</i> parameter must be one of:</p>
<dl>
<dt><code>IPQ_COPY_META</code></p>
<dd> Copy only packet metadata to userspace.</p>
<dt><code>IPQ_COPY_PACKET</code></p>
<dd> Copy packet metadata and packet payloads to userspace.</dl>
<p> The <i>range</i> parameter is used to specify how many bytes of the payload to copy to userspace. It is only valid for <code>IPQ_COPY_PACKET</code> mode and is otherwise ignored. The maximum useful value for <i>range</i> is 65535 (greater values will be clamped to this by ip_queue). </p>
<p> <code>ipq_set_mode</code> is usually used immediately following <code>ipq_create_handle</code> to enable the flow of packets to userspace. </p>
<p> Note that as the underlying Netlink messaging transport is connectionless, the ip_queue module does not know that a userspace application is ready to communicate until it receives a message such as this.</p>
<h2>RETURN VALUE</h2>
<p> On failure, -1 is returned.<br />
 On success, a non-zero positive value is returned.</p>
<h2>ERRORS</h2>
<p> On failure, a descriptive error message will be available via the <code>ipq_errstr</code> function.</p>
<h2>DIAGNOSTICS</h2>
<p> A relatively common failure may occur if the ip_queue module is not loaded. In this case, the following code excerpt: </p>
<dl>
<dt>
<dd>
<pre><code>
status = ipq_set_mode(h, IPQ_COPY_META, 0);
if (status &lt; 0) {
    ipq_perror("myapp");
    ipq_destroy_handle(h);
    exit(1);
}
</code></pre>
<p> would generate the following output: </p>
<p> <i>myapp: Failed to send netlink message: Connection refused</i></p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> James Morris &lt;jmorris [at] intercode.com.au&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2001 Netfilter Core Team. </p>
<p> Distributed under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libipq/">libipq</a></code>(3), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8). </p>
<h2>Index</h2>
