---
title: "ibv_open_xrcd(3)"
name: "ibv_open_xrcd"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_open_xrcd/"
description: "ibv_open_xrcd, ibv_close_xrcd – open or close an XRC protection domain (XRCDs)"
---

<h2 class="name">NAME</h2>
<p> ibv_open_xrcd, ibv_close_xrcd &#8211; open or close an XRC protection domain (XRCDs) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_xrcd *ibv_open_xrcd(struct ibv_context *context,
                               struct ibv_xrcd_init_attr *xrcd_init_attr);
int ibv_close_xrcd(struct ibv_xrcd *xrcd);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_open_xrcd()</code> open an XRC domain for the RDMA device context <i>context</i> <i>xrcd_init_attr</i> is an ibv_xrcd_init_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_xrcd_init_attr {
    uint32_t comp_mask; /* Identifies valid fields */
    int fd;
    int oflag;
</code></pre>
<p> <i>fd</i> is the file descriptor to associate with the XRCD. <i>oflag</i> describes the desired creation attributes. It is a bitwise OR of zero or more of the following flags: </p>
<dl>
<dt><code>O_CREAT</code></p>
<dd> Indicates that an XRCD should be created and associated with the inode referenced by the given fd. If the XRCD exists, this flag has no effect except as noted under <code>O_EXCL</code> below.</p>
<dt><code>O_EXCL</code></p>
<dd> If <code>O_EXCL</code> and <code>O_CREAT</code> are set, open will fail if an XRCD associated with the inode exists.</dl>
<p> If <i>fd</i> equals -1, no inode is associated with the XRCD. To indicate that XRCD should be created, use <i>oflag</i> = <code>O_CREAT</code>. </p>
<p> <code>ibv_close_xrcd()</code> closes the XRCD <i>xrcd</i>. If this is the last reference, the XRCD will be destroyed.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_open_xrcd()</code> returns a pointer to the opened XRCD, or NULL if the request fails. </p>
<p> <code>ibv_close_xrcd()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> <code>ibv_close_xrcd()</code> may fail if any other resource is still associated with the XRCD being closed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_srq_ex/">ibv_create_srq_ex</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_qp_ex/">ibv_create_qp_ex</a></code>(3),</p>
<h2>AUTHORS</h2>
<dl>
<dt>Sean Hefty &lt;sean.hefty [at] intel.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
