---
title: "ibv_bind_mw(3)"
name: "ibv_bind_mw"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_bind_mw/"
description: "ibv_bind_mw – post a request to bind a type 1 memory window to a memory region"
---

<h2 class="name">NAME</h2>
<p> ibv_bind_mw &#8211; post a request to bind a type 1 memory window to a memory region </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_bind_mw(struct ibv_qp *qp, struct ibv_mw *mw,
                struct ibv_mw_bind *mw_bind);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_bind_mw()</code> posts to the queue pair <i>qp</i> a request to bind the memory window <i>mw</i> according to the details in <i>mw_bind</i>. </p>
<p> The argument <i>mw_bind</i> is an ibv_mw_bind struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<p>struct ibv_mw_bind {<br />
    uint64_t wr_id;                    /* User defined WR ID */<br />
    int send_flags;                    /* Use ibv_send_flags */<br />
    struct ibv_mw_bind_info bind_info; /* MW bind information */<br />
}</p>
<pre><code>
struct ibv_mw_bind_info {
    struct ibv_mr *mr;   /* The MR to bind the MW to */
    uint64_t addr;       /* The address the MW should start at */
    uint64_t length;     /* The length (in bytes) the MW should span */
    int mw_access_flags; /* Access flags to the MW. Use ibv_access_flags */
};
</code></pre>
<p> The QP Transport Service Type must be either UC, RC or XRC_SEND for bind operations. </p>
<p> The attribute send_flags describes the properties of the <font SIZE="-1">WR</font>. It is either 0 or the bitwise <font SIZE="-1">OR</font> of one or more of the following flags: </p>
<dl>
<dt><code>IBV_SEND_FENCE </code> Set the fence indicator.</p>
<dd>
<dt><code>IBV_SEND_SIGNALED </code> Set the completion notification indicator. Relevant only if QP was created with sq_sig_all=0</p>
<dd></dl>
<p> The mw_access_flags define the allowed access to the MW after the bind completes successfully. It is either 0 or the bitwise <font SIZE="-1">OR</font> of one or more of the following flags:</p>
<dl>
<dt><code>IBV_ACCESS_REMOTE_WRITE </code> Enable Remote Write Access. Requires local write access to the MR.</p>
<dd>
<dt><code>IBV_ACCESS_REMOTE_READ</code> Enable Remote Read Access</p>
<dd>
<dt><code>IBV_ACCESS_REMOTE_ATOMIC</code> Enable Remote Atomic Operation Access (if supported). Requires local write access to the MR.</p>
<dd>
<dt><code>IBV_ACCESS_ZERO_BASED</code> If set, the address set on the &#8216;remote_addr&#8217; field on the WR will be an offset from the MW&#8217;s start address.</p>
<dd></dl>
<h2>RETURN VALUE</h2>
<p> <code>ibv_bind_mw()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason). In case of a success, the R_key of the memory window after the bind is returned in the mw_bind-&gt;mw-&gt;rkey field.</p>
<h2>NOTES</h2>
<p> The bind does not complete when the function return &#8211; it is merely posted to the QP. The user should keep a copy of the old R_key, and fix the mw structure if the subsequent CQE for the bind operation indicates a failure. The user may safely send the R_key using a send request on the same QP, (based on QP ordering rules: a send after a bind request on the same QP are always ordered), but must not transfer it to the remote in any other manner before reading a successful CQE. </p>
<p> Note that for type 2 MW, one should directly post bind WR to the QP, using ibv_post_send.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_mw/">ibv_alloc_mw</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a></code>(3), <code><a href="/docs/linux/man/3-ibv_poll_cq/">ibv_poll_cq</a></code>(3) <code><a href="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a></code>(3),</p>
<h2>AUTHORS</h2>
<dl>
<dt>Majd Dibbiny &lt;majd [at] mellanox.com&gt;</p>
<dd>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
