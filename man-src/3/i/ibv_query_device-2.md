---
title: "ibv_query_device-2(3)"
name: "ibv_query_device-2"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_query_device-2/"
description: "ibv_query_device – query an RDMA device’s attributes"
---

<p>ibv_query_device &#8211; query an RDMA device&#8217;s attributes </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/verbs.h&gt;</code>
<code>int ibv_query_device(struct ibv_context </code><i>*context,</i>
<code> struct ibv_device_attr </code><i>*device_attr</i><code>);</code></pre>
<h2>Description</h2>
<p><code>ibv_query_device()</code> returns the attributes of the device with context <i>context</i>. The argument <i>device_attr</i> is a pointer to an ibv_device_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre>struct ibv_device_attr {
char fw_ver[64]; /* FW version */
uint64_t node_guid; /* Node GUID (in network byte order) */
uint64_t sys_image_guid; /* System image GUID (in network byte order) */
uint64_t max_mr_size; /* Largest contiguous block that can be registered */
uint64_t page_size_cap; /* Supported memory shift sizes */
uint32_t vendor_id; /* Vendor ID, per IEEE */
uint32_t vendor_part_id; /* Vendor supplied part ID */
uint32_t hw_ver; /* Hardware version */
int max_qp; /* Maximum number of supported QPs */
int max_qp_wr; /* Maximum number of outstanding WR on any work queue */
unsigned int device_cap_flags; /* HCA capabilities mask */
int max_sge; /* Maximum number of s/g per WR for SQ &amp; RQ of QP for non RDMA Read operations */
int max_sge_rd; /* Maximum number of s/g per WR for RDMA Read operations */
int max_cq; /* Maximum number of supported CQs */
int max_cqe; /* Maximum number of CQE capacity per CQ */
int max_mr; /* Maximum number of supported MRs */
int max_pd; /* Maximum number of supported PDs */
int max_qp_rd_atom; /* Maximum number of RDMA Read &amp; Atomic operations that can be outstanding per QP */
int max_ee_rd_atom; /* Maximum number of RDMA Read &amp; Atomic operations that can be outstanding per EEC */
int max_res_rd_atom; /* Maximum number of resources used for RDMA Read &amp; Atomic operations by this HCA as the Target */
int max_qp_init_rd_atom; /* Maximum depth per QP for initiation of RDMA Read &amp; Atomic operations */ 
int max_ee_init_rd_atom; /* Maximum depth per EEC for initiation of RDMA Read &amp; Atomic operations */
enum ibv_atomic_cap atomic_cap; /* Atomic operations support level */
int max_ee; /* Maximum number of supported EE contexts */
int max_rdd; /* Maximum number of supported RD domains */
int max_mw; /* Maximum number of supported MWs */
int max_raw_ipv6_qp; /* Maximum number of supported raw IPv6 datagram QPs */
int max_raw_ethy_qp; /* Maximum number of supported Ethertype datagram QPs */
int max_mcast_grp; /* Maximum number of supported multicast groups */
int max_mcast_qp_attach; /* Maximum number of QPs per multicast group which can be attached */
int max_total_mcast_qp_attach;/* Maximum number of QPs which can be attached to multicast groups */
int max_ah; /* Maximum number of supported address handles */
int max_fmr; /* Maximum number of supported FMRs */
int max_map_per_fmr; /* Maximum number of (re)maps per FMR before an unmap operation in required */
int max_srq; /* Maximum number of supported SRQs */
int max_srq_wr; /* Maximum number of WRs per SRQ */
int max_srq_sge; /* Maximum number of s/g per SRQ */
uint16_t max_pkeys; /* Maximum number of partitions */
uint8_t local_ca_ack_delay; /* Local CA ack delay */
uint8_t phys_port_cnt; /* Number of physical ports */
};</pre>
<h2>Return Value</h2>
<p><code>ibv_query_device()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>Notes</h2>
<p>The maximum values returned by this function are the upper limits of supported resources by the device. However, it may not be possible to use these maximum values, since the actual number of any resource that can be created may be limited by the machine configuration, the amount of host memory, user permissions, and the amount of resources already in use by other users/processes.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_port/">ibv_query_port</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_pkey/">ibv_query_pkey</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_gid/">ibv_query_gid</a></code>(3)</p>
<h2>Authors</h2>
<dl COMPACT>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd></dl>
