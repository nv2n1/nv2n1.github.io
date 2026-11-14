---
title: "ibv_attach_mcast(3)"
name: "ibv_attach_mcast"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_attach_mcast/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_attach_mcast, ibv_detach_mcast - attach and detach a queue pair (QPs) to/from a multicast group 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_attach_mcast(struct ibv_qp *qp, const union ibv_gid *gid, uint16_t lid);
int ibv_detach_mcast(struct ibv_qp *qp, const union ibv_gid *gid, uint16_t lid);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 ibv_attach_mcast() attaches the QP qp to the multicast group having MGID gid and MLID lid. 

 ibv_detach_mcast() detaches the QP qp to the multicast group having MGID gid and MLID lid.

<h2>RETURN VALUE</h2>

 

 ibv_attach_mcast() and ibv_detach_mcast() returns 0 on success, or the value of errno on failure (which indicates the failure reason).

<h2>NOTES</h2>

 

 Only QPs of Transport Service Type IBV_QPT_UD may be attached to multicast groups. 

 If a QP is attached to the same multicast group multiple times, the QP will still receive a single copy of a multicast message. 

 In order to receive multicast messages, a join request for the multicast group must be sent to the subnet administrator (SA), so that the fabric's multicast routing is configured to deliver messages to the local port.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a>(3)

<h2>AUTHOR</h2>

 

 Dotan Barak &lt;dotanba [at] gmail.com&gt; 

<h2>Index</h2>


