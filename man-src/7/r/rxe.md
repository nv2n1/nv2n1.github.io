---
title: "rxe(7)"
name: "rxe"
section: "7"
letter: "r"
url: "/docs/linux/man/7-rxe/"
description: "rxe – Software RDMA over Ethernet"
---

<p>rxe &#8211; Software RDMA over Ethernet</p>
<h2>Synopsis</h2>
<p><code>modprobe rdma_rxe</code><br />
 This is usually performed by a configuration utility (see <code><a href="/docs/linux/man/8-rxe_cfg/">rxe_cfg</a></code>(8).) </p>
<h2>Description</h2>
<p>The rdma_rxe kernel module provides a software implementation of the RoCEv2 protocol. The RoCEv2 protocol is an RDMA transport protocol that exists on top of UDP/IPv4 or UDP/IPv6. The InfiniBand (IB) Base Transport Header (BTH) is encapsulated in the UDP packet. Once a RXE instance has been created, communicating via RXE is the same as communicating via any OFED compatible Infiniband HCA, albeit in some cases with addressing implications. In particular, while the use of a GRH header is optional within IB subnets, it is mandatory with RoCE. Verbs applications written over IB verbs should work seamlessly, but they require provisioning of GRH information when creating address vectors. The library and driver are modified to provide for mapping from GID to MAC addresses required by the hardware. </p>
<h2>Files</h2>
<dl>
<dt><code>/sys/class/infiniband/rxe[0,1,&#8230;]</code></p>
<dd>Directory that holds RDMA device information. The format is the same as other RDMA devices. </p>
<dt><code>/sys/module/rdma_rxe_net/parameters/add</code></p>
<dd>Write only file used by <code><a href="/docs/linux/man/8-rxe_cfg/">rxe_cfg</a>(8)</code> to add new RXE devices to existing Ethernet devices. </p>
<dt><code>/sys/module/rdma_rxe_net/parameters/remove</code></p>
<dd>Write only file used by <code><a href="/docs/linux/man/8-rxe_cfg/">rxe_cfg</a>(8)</code> to remove RXE devices. </p>
<dt><code>/sys/module/rdma_rxe_net/parameters/mtu</code></p>
<dd>Write only file used by <code><a href="/docs/linux/man/8-rxe_cfg/">rxe_cfg</a>(8)</code> to configure RoCE and Ethernet MTU values. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_ucontext</code></p>
<dd>Read/Write file that sets a limit on the number of UCs allowed per RXE device. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_qp</code></p>
<dd>Read/Write file that sets a limit on the number of QPs allowed per RXE device. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_qp_wr</code></p>
<dd>Read/Write file that sets a limit on the number of WRs per QP allowed per RXE device. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_mr</code></p>
<dd>Read/Write file that sets a limit on the number of MRs allowed per RXE device. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_fmr</code></p>
<dd>Read/Write file that sets a limit on the number of FMRs allowed per RXE device. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_cq</code></p>
<dd>Read/Write file that sets a limit on the number of CQs allowed per RXE device. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_log_cqe</code></p>
<dd>Read/Write file that sets a limit on the log base 2 of the number of CQEs per CQ allowed per RXE device. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_inline_data</code></p>
<dd>Read/Write file that sets a limit on the maximum amount of inline data per WR allowed per RXE device. </p>
<p> The above configuration parameters only affect a new RXE instance when it is created not afterwards. </p>
<dt><code>/sys/module/rdma_rxe/parameters/crc_disable</code></p>
<dd>Read/Write file that controls the disabling of ICRC computation. Set to a nonzero value for TRUE. Zero for FALSE. </p>
<dt><code>/sys/module/rdma_rxe/parameters/fast_comp|req|resp|arb</code></p>
<dd>Read/Write file that enables calling kernel tasklets as subroutines to reduce latency. </p>
<dt><code>/sys/module/rdma_rxe/parameters/nsec_per_packet|kbyte</code></p>
<dd>Read/Write file that controls static rate pacing for output packets. If set to nonzero values the minimum delay to the next packet is set to nsec_per_kbyte * sizeof(current packet in KBytes) or nsec_per_packet which ever is less. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_packet_per_ack</code></p>
<dd>Read/Write file that controls the issuing of acks by the responder during a long message. If set additional acks will be generated every max_pkt_per_ack packets. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_skb_per_qp</code></p>
<dd>Read/Write file that controls the number of skbs (packets) that a requester can queue for sending internally. </p>
<dt><code>/sys/module/rdma_rxe/parameters/max_req_comp_gap</code></p>
<dd>Read/Write file that controls the maximum gap between the PSN of request packets send and ack packets received. </p>
<dt><code>/sys/module/rdma_rxe/parameters/default_mtu</code></p>
<dd>Read/Write file that controls the default mtu used for UD packets. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rxe_cfg/">rxe_cfg</a></code>(8), <code><a href="/docs/linux/man/7-verbs/">verbs</a></code>(7), </p>
<h2>Authors</h2>
<p>Written by John Groves, Frank Zago and Bob Pearson at System Fabric Works.</p>
