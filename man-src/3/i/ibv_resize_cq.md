---

title: "ibv_resize_cq(3)"
name: "ibv_resize_cq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_resize_cq/"
---

ibv_resize_cq - resize a completion queue (CQ) 

<h2>SYNOPSIS</h2>

<dl>
<dt>
</dt><dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_resize_cq(struct ibv_cq *cq, int cqe);
</code></pre></dd></dl>

<h2>DESCRIPTION</h2>

 

 ibv_resize_cq() resizes the completion queue (CQ) cq to have at least cqe entries. cqe must be at least the number of unpolled entries in the CQ cq. If cqe is a valid value less than the current CQ size, ibv_resize_cq() may not do anything, since this function is only guaranteed to resize the CQ to a size at least as big as the requested size.

<h2>RETURN VALUE</h2>

 

 ibv_resize_cq() returns 0 on success, or the value of errno on failure (which indicates the failure reason).

<h2>NOTES</h2>

 

 ibv_resize_cq() may assign a CQ size greater than or equal to the requested size. The cqe member of cq will be updated to the actual size.

<h2>SEE ALSO</h2>

 

 ibv_create_cq(3), ibv_destroy_cq(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt;
