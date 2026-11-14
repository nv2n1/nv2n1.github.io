---
title: "ibv_reg_mr(3)"
name: "ibv_reg_mr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_reg_mr/"
description: "ibv_reg_mr, ibv_reg_mr_iova, ibv_dereg_mr – register or deregister a memory region (MR)"
---

<h2 class="name">NAME</h2>
<p> ibv_reg_mr, ibv_reg_mr_iova, ibv_dereg_mr &#8211; register or deregister a memory region (MR) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_mr *ibv_reg_mr(struct ibv_pd *pd, void *addr,
                          size_t length, int access);
struct ibv_mr *ibv_reg_mr_iova(struct ibv_pd *pd, void *addr,
                               size_t length, uint64_t hca_va,
                               int access);
int ibv_dereg_mr(struct ibv_mr *mr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_reg_mr()</code> registers a memory region (MR) associated with the protection domain <i>pd</i>. The MR&#8217;s starting address is <i>addr</i> and its size is <i>length</i>. The argument <i>access</i> describes the desired memory protection attributes; it is either 0 or the bitwise OR of one or more of the following flags: </p>
<dl>
<dt><code>IBV_ACCESS_LOCAL_WRITE </code> Enable Local Write Access</p>
<dd>
<dt><code>IBV_ACCESS_REMOTE_WRITE </code> Enable Remote Write Access</p>
<dd>
<dt><code>IBV_ACCESS_REMOTE_READ</code> Enable Remote Read Access</p>
<dd>
<dt><code>IBV_ACCESS_REMOTE_ATOMIC</code> Enable Remote Atomic Operation Access (if supported)</p>
<dd>
<dt><code>IBV_ACCESS_MW_BIND</code> Enable Memory Window Binding</p>
<dd>
<dt><code>IBV_ACCESS_ZERO_BASED</code> Use byte offset from beginning of MR to access this MR, instead of a pointer address</p>
<dd>
<dt><code>IBV_ACCESS_ON_DEMAND</code> Create an on-demand paging MR</p>
<dd>
<dt><code>IBV_ACCESS_HUGETLB</code> Huge pages are guaranteed to be used for this MR, applicable with IBV_ACCESS_ON_DEMAND in explicit mode only</p>
<dd>
<dt><code>IBV_ACCESS_RELAXED_ORDERING</code> Allow system to reorder accesses to the MR to improve performance</p>
<dd></dl>
<p> If <code>IBV_ACCESS_REMOTE_WRITE</code> or <code>IBV_ACCESS_REMOTE_ATOMIC</code> is set, then <code>IBV_ACCESS_LOCAL_WRITE</code> must be set too. </p>
<p> Local read access is always enabled for the MR. </p>
<p> To create an implicit ODP MR, IBV_ACCESS_ON_DEMAND should be set, addr should be 0 and length should be SIZE_MAX. </p>
<p> If <code>IBV_ACCESS_HUGETLB</code> is set, then application awares that for this MR all pages are huge and must promise it will never do anything to break huge pages. </p>
<p> <code>ibv_reg_mr_iova()</code> ibv_reg_mr_iova is the same as the normal reg_mr, except that the user is allowed to specify the virtual base address of the MR when accessed through a lkey or rkey. The offset in the memory region is computed as &#8216;addr + (iova &#8211; hca_va)&#8217;. Specifying 0 for hca_va has the same effect as IBV_ACCESS_ZERO_BASED. </p>
<p> <code>ibv_dereg_mr()</code> deregisters the MR <i>mr</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_reg_mr() / ibv_reg_mr_iova()</code> returns a pointer to the registered MR, or NULL if the request fails. The local key (<code>L_Key</code>) field <code>lkey</code> is used as the lkey field of struct ibv_sge when posting buffers with ibv_post_* verbs, and the the remote key (<code>R_Key</code>) field <code>rkey</code> is used by remote processes to perform Atomic and RDMA operations. The remote process places this <code>rkey</code> as the rkey field of struct ibv_send_wr passed to the ibv_post_send function. </p>
<p> <code>ibv_dereg_mr()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> <code>ibv_dereg_mr()</code> fails if any memory window is still bound to this MR.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_recv/">ibv_post_recv</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_srq_recv/">ibv_post_srq_recv</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
