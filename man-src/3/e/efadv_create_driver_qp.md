---
title: "efadv_create_driver_qp(3)"
name: "efadv_create_driver_qp"
section: "3"
letter: "e"
url: "/docs/linux/man/3-efadv_create_driver_qp/"
---

<h2 class="name">NAME</h2>
 

 

 efadv_create_driver_qp - Create EFA specific Queue Pair # SYNOPSIS
<dl>
<dt>
<dd> <pre><code>
#include &lt;
infiniband / efadv.h &gt;
    struct ibv_qp *efadv_create_driver_qp(struct ibv_pd *ibvpd,
                                          struct ibv_qp_init_attr *attr,
                                          uint32_t driver_qp_type);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 efadv_create_driver_qp() Create device-specific Queue Pairs. 

 Scalable Reliable Datagram (SRD) transport provides reliable out-of-order delivery, transparently utilizing multiple network paths to reduce network tail latency. Its interface is similar to UD, in particular it supports message size up to MTU, with error handling extended to support reliable communication.
<dl>
<dt>driver_qp_type
<dd> The type of QP to be created:
<dl>
<dt>
<dd> 

 EFADV_QP_DRIVER_TYPE_SRD: Create an SRD QP.</dl>
</dl>

<h2>RETURN VALUE</h2>

 

 efadv_create_driver_qp() returns a pointer to the created QP, or NULL if the request fails.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/7-efadv/">efadv</a>(7)

<h2>AUTHORS</h2>

 

 Gal Pressman &lt;galpress [at] amazon.com&gt; 

<h2>Index</h2>


