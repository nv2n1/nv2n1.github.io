---
title: "ibv_get_srq_num(3)"
name: "ibv_get_srq_num"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_get_srq_num/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_get_srq_num - return srq number associated with the given shared receive queue (SRQ) 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_get_srq_num(struct ibv_srq *srq, uint32_t *srq_num);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_get_srq_num() return srq number associated with the given shared receive queue The argument srq is an ibv_srq struct, as defined in &lt;infiniband/verbs.h&gt;. srq_num is an output parameter that holds the returned srq number.

<h2>RETURN VALUE</h2>

 

 ibv_get_srq_num() returns 0 on success, or the value of errno on failure (which indicates the failure reason).

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a>(3), <a HREF="/docs/linux/man/3-ibv_create_srq_ex/">ibv_create_srq_ex</a>(3), <a HREF="/docs/linux/man/3-ibv_modify_srq/">ibv_modify_srq</a>(3)

<h2>AUTHOR</h2>

 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


