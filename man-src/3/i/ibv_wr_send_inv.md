---
title: "ibv_wr_send_inv(3)"
name: "ibv_wr_send_inv"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_wr_send_inv/"
---

<h2 class="name">NAME</h2>
 

 

 ibv_wr_abort, ibv_wr_complete, ibv_wr_start - Manage regions allowed to post work 

 ibv_wr_atomic_cmp_swp, ibv_wr_atomic_fetch_add - Post remote atomic operation work requests 

 ibv_wr_bind_mw, ibv_wr_local_inv - Post work requests for memory windows 

 ibv_wr_rdma_read, ibv_wr_rdma_write, ibv_wr_rdma_write_imm - Post RDMA work requests 

 ibv_wr_send, ibv_wr_send_imm, ibv_wr_send_inv - Post send work requests 

 ibv_wr_send_tso - Post segmentation offload work requests 

 ibv_wr_set_inline_data, ibv_wr_set_inline_data_list - Attach inline data to the last work request 

 ibv_wr_set_sge, ibv_wr_set_sge_list - Attach data to the last work request 

 ibv_wr_set_ud_addr - Attach UD addressing info to the last work request 

 ibv_wr_set_xrc_srqn - Attach an XRC SRQN to the last work request 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/verbs.h&gt;
void ibv_wr_abort(struct ibv_qp_ex *qp);
int ibv_wr_complete(struct ibv_qp_ex *qp);
void ibv_wr_start(struct ibv_qp_ex *qp);
void ibv_wr_atomic_cmp_swp(struct ibv_qp_ex *qp, uint32_t rkey,
                           uint64_t remote_addr, uint64_t compare,
                           uint64_t swap);
void ibv_wr_atomic_fetch_add(struct ibv_qp_ex *qp, uint32_t rkey,
                             uint64_t remote_addr, uint64_t add);
void ibv_wr_bind_mw(struct ibv_qp_ex *qp, struct ibv_mw *mw, uint32_t rkey,
                    const struct ibv_mw_bind_info *bind_info);
void ibv_wr_local_inv(struct ibv_qp_ex *qp, uint32_t invalidate_rkey);
void ibv_wr_rdma_read(struct ibv_qp_ex *qp, uint32_t rkey,
                      uint64_t remote_addr);
void ibv_wr_rdma_write(struct ibv_qp_ex *qp, uint32_t rkey,
                       uint64_t remote_addr);
void ibv_wr_rdma_write_imm(struct ibv_qp_ex *qp, uint32_t rkey,
                           uint64_t remote_addr, __be32 imm_data);
void ibv_wr_send(struct ibv_qp_ex *qp);
void ibv_wr_send_imm(struct ibv_qp_ex *qp, __be32 imm_data);
void ibv_wr_send_inv(struct ibv_qp_ex *qp, uint32_t invalidate_rkey);
void ibv_wr_send_tso(struct ibv_qp_ex *qp, void *hdr, uint16_t hdr_sz,
                     uint16_t mss);
void ibv_wr_set_inline_data(struct ibv_qp_ex *qp, void *addr, size_t length);
void ibv_wr_set_inline_data_list(struct ibv_qp_ex *qp, size_t num_buf,
                                 const struct ibv_data_buf *buf_list);
void ibv_wr_set_sge(struct ibv_qp_ex *qp, uint32_t lkey, uint64_t addr,
                    uint32_t length);
void ibv_wr_set_sge_list(struct ibv_qp_ex *qp, size_t num_sge,
                         const struct ibv_sge *sg_list);
void ibv_wr_set_ud_addr(struct ibv_qp_ex *qp, struct ibv_ah *ah,
                        uint32_t remote_qpn, uint32_t remote_qkey);
void ibv_wr_set_xrc_srqn(struct ibv_qp_ex *qp, uint32_t remote_srqn);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 The verbs work request API (ibv_wr_*) allows efficient posting of work to a send queue using function calls instead of the struct based ibv_post_send() scheme. This approach is designed to minimize CPU branching and locking during the posting process. 

 This API is intended to be used to access additional functionality beyond what is provided by ibv_post_send(). 

 WRs batches of ibv_post_send() and this API WRs batches can interleave together just if they are not posted within the critical region of each other. (A critical region in this API formed by ibv_wr_start() and ibv_wr_complete()/ibv_wr_abort())

<h2>USAGE</h2>

 

 To use these APIs the QP must be created using ibv_create_qp_ex() which allows setting the IBV_QP_INIT_ATTR_SEND_OPS_FLAGS in comp_mask. The send_ops_flags should be set to the OR of the work request types that will be posted to the QP. 

 If the QP does not support all the requested work request types then QP creation will fail. 

 Posting work requests to the QP is done within the critical region formed by ibv_wr_start() and ibv_wr_complete()/ibv_wr_abort() (see CONCURRENCY below). 

 Each work request is created by calling a WR builder function (see the table column WR builder below) to start creating the work request, followed by allowed/required setter functions described below. 

 The WR builder and setter combination can be called multiple times to efficiently post multiple work requests within a single critical region. 

 Each WR builder will use the wr_id member of struct ibv_qp_ex to set the value to be returned in the completion. Some operations will also use the wr_flags member to influence operation (see Flags below). These values should be set before invoking the WR builder function. 

 For example a simple send could be formed as follows:
<dl>
<dt>
<dd> 
qpx-&gt;wr_id = 1;
ibv_wr_send(qpx);
ibv_wr_set_sge(qpx, lkey, &amp;data, sizeof(data));
</dl>
 

 The section WORK REQUESTS describes the various WR builders and setters in details. 

 Posting work is completed by calling ibv_wr_complete() or ibv_wr_abort(). No work is executed to the queue until ibv_wr_complete() returns success. ibv_wr_abort() will discard all work prepared since ibv_wr_start().

<h2>WORK REQUESTS</h2>

 

 Many of the operations match the opcodes available for ibv_post_send(). Each operation has a WR builder function, a list of allowed setters, and a flag bit to request the operation with send_ops_flags in struct ibv_qp_init_attr_ex (see the EXAMPLE below). 

 <table> <tr VALIGN=top><td> Operation </td><td> WR builder </td><td> QP Type Supported </td><td> setters 
</td></tr> <tr VALIGN=top><td COLSPAN=4><hr></td></tr> <tr VALIGN=top><td> ATOMIC_CMP_AND_SWP </td><td> ibv_wr_atomic_cmp_swp() </td><td> RC, XRC_SEND </td><td> DATA, QP 
</td></tr> <tr VALIGN=top><td> ATOMIC_FETCH_AND_ADD </td><td> ibv_wr_atomic_fetch_add() </td><td> RC, XRC_SEND </td><td> DATA, QP 
</td></tr> <tr VALIGN=top><td> BIND_MW </td><td> ibv_wr_bind_mw() </td><td> UC, RC, XRC_SEND </td><td> NONE 
</td></tr> <tr VALIGN=top><td> LOCAL_INV </td><td> ibv_wr_local_inv() </td><td> UC, RC, XRC_SEND </td><td> NONE 
</td></tr> <tr VALIGN=top><td> RDMA_READ </td><td> ibv_wr_rdma_read() </td><td> RC, XRC_SEND </td><td> DATA, QP 
</td></tr> <tr VALIGN=top><td> RDMA_WRITE </td><td> ibv_wr_rdma_write() </td><td> UC, RC, XRC_SEND </td><td> DATA, QP 
</td></tr> <tr VALIGN=top><td> RDMA_WRITE_WITH_IMM </td><td> ibv_wr_rdma_write_imm() </td><td> UC, RC, XRC_SEND </td><td> DATA, QP 
</td></tr> <tr VALIGN=top><td> SEND </td><td> ibv_wr_send() </td><td> UD, UC, RC, XRC_SEND, RAW_PACKET </td><td> DATA, QP 
</td></tr> <tr VALIGN=top><td> SEND_WITH_IMM </td><td> ibv_wr_send_imm() </td><td> UD, UC, RC, SRC SEND </td><td> DATA, QP 
</td></tr> <tr VALIGN=top><td> SEND_WITH_INV </td><td> ibv_wr_send_inv() </td><td> UC, RC, XRC_SEND </td><td> DATA, QP 
</td></tr> <tr VALIGN=top><td> TSO </td><td> ibv_wr_send_tso() </td><td> UD, RAW_PACKET </td><td> DATA, QP 
</td></tr> </table>

<h3>Atomic operations</h3>

 

 Atomic operations are only atomic so long as all writes to memory go only through the same RDMA hardware. It is not atomic with writes performed by the CPU, or by other RDMA hardware in the system.
<dl>
<dt>ibv_wr_atomic_cmp_swp()
<dd> If the remote 64 bit memory location specified by rkey and remote_addr equals compare then set it to swap.
<dt>ibv_wr_atomic_fetch_add()
<dd> Add add to the 64 bit memory location specified rkey and remote_addr.</dl>

<h3>Memory Windows</h3>

 

 Memory window type 2 operations (See man page for ibv_alloc_mw).
<dl>
<dt>ibv_wr_bind_mw()
<dd> Bind a MW type 2 specified by mw, set a new rkey and set its properties by bind_info.
<dt>ibv_wr_local_inv()
<dd> Invalidate a MW type 2 which is associated with rkey.</dl>

<h3>RDMA</h3>

<dl>
<dt>ibv_wr_rdma_read()
<dd> Read from the remote memory location specified rkey and remote_addr. The number of bytes to read, and the local location to store the data, is determined by the DATA buffers set after this call.
<dt>ibv_wr_rdma_write(), ibv_wr_rdma_write_imm()
<dd> Write to the remote memory location specified rkey and remote_addr. The number of bytes to read, and the local location to get the data, is determined by the DATA buffers set after this call.
<dl>
<dt>
<dd> 

 The _imm version causes the remote side to get a IBV_WC_RECV_RDMA_WITH_IMM containing the 32 bits of immediate data.</dl>
</dl>

<h3>Message Send</h3>

<dl>
<dt>ibv_wr_send(), ibv_wr_send_imm()
<dd> Send a message. The number of bytes to send, and the local location to get the data, is determined by the DATA buffers set after this call.
<dl>
<dt>
<dd> 

 The _imm version causes the remote side to get a IBV_WC_RECV_RDMA_WITH_IMM containing the 32 bits of immediate data.</dl>

<dt>ibv_wr_send_inv()
<dd> The data transfer is the same as for ibv_wr_send(), however the remote side will invalidate the MR specified by invalidate_rkey before delivering a completion.
<dt>ibv_wr_send_tso()
<dd> Produce multiple SEND messages using TCP Segmentation Offload. The SGE points to a TCP Stream buffer which will be segmented into MSS size SENDs. The hdr includes the entire network headers up to and including the TCP header and is prefixed before each segment.</dl>

<h3>QP Specific setters</h3>

 

 Certain QP types require each post to be accompanied by additional setters, these setters are mandatory for any operation listing a QP setter in the above table.
<dl>
<dt>UD QPs
<dd> ibv_wr_set_ud_addr() must be called to set the destination address of the work.
<dt>XRC_SEND QPs
<dd> ibv_wr_set_xrc_srqn() must be called to set the destination SRQN field.</dl>

<h3>DATA transfer setters</h3>

 

 For work that requires to transfer data one of the following setters should be called once after the WR builder:
<dl>
<dt>ibv_wr_set_sge()
<dd> Transfer data to/from a single buffer given by the lkey, addr and length. This is equivalent to ibv_wr_set_sge_list() with a single element.
<dt>ibv_wr_set_sge_list()
<dd> Transfer data to/from a list of buffers, logically concatenated together. Each buffer is specified by an element in an array of struct ibv_sge.</dl>
 

 Inline setters will copy the send data during the setter and allows the caller to immediately re-use the buffer. This behavior is identical to the IBV_SEND_INLINE flag. Generally this copy is done in a way that optimizes SEND latency and is suitable for small messages. The provider will limit the amount of data it can support in a single operation. This limit is requested in the max_inline_data member of struct ibv_qp_init_attr. Valid only for SEND and RDMA_WRITE.
<dl>
<dt>ibv_wr_set_inline_data()
<dd> Copy send data from a single buffer given by the addr and length. This is equivalent to ibv_wr_set_inline_data_list() with a single element.
<dt>ibv_wr_set_inline_data_list()
<dd> Copy send data from a list of buffers, logically concatenated together. Each buffer is specified by an element in an array of struct ibv_inl_data.</dl>

<h3>Flags</h3>

 

 A bit mask of flags may be specified in wr_flags to control the behavior of the work request.
<dl>
<dt>IBV_SEND_FENCE
<dd> Do not start this work request until prior work has completed.
<dt>IBV_SEND_IP_CSUM
<dd> Offload the IPv4 and TCP/UDP checksum calculation
<dt>IBV_SEND_SIGNALED
<dd> A completion will be generated in the completion queue for the operation.
<dt>IBV_SEND_SOLICTED
<dd> Set the solicted bit in the RDMA packet. This informs the other side to generate a completion event upon receiving the RDMA operation.</dl>

<h2>CONCURRENCY</h2>

 

 The provider will provide locking to ensure that ibv_wr_start() and ibv_wr_complete()/abort() form a per-QP critical section where no other threads can enter. 

 If an ibv_td is provided during QP creation then no locking will be performed and it is up to the caller to ensure that only one thread can be within the critical region at a time.

<h2>RETURN VALUE</h2>

 

 Applications should use this API in a way that does not create failures. The individual APIs do not return a failure indication to avoid branching. 

 If a failure is detected during operation, for instance due to an invalid argument, then ibv_wr_complete() will return failure and the entire posting will be aborted.

<h2>EXAMPLE</h2>

<dl>
<dt>
<dd> <pre><code>
/* create RC QP type and specify the required send opcodes */
qp_init_attr_ex.qp_type = IBV_QPT_RC;
qp_init_attr_ex.comp_mask |= IBV_QP_INIT_ATTR_SEND_OPS_FLAGS;
qp_init_attr_ex.send_ops_flags |= IBV_QP_EX_WITH_RDMA_WRITE;
qp_init_attr_ex.send_ops_flags |= IBV_QP_EX_WITH_RDMA_WRITE_WITH_IMM;
ibv_qp *qp = ibv_create_qp_ex(ctx, qp_init_attr_ex);
ibv_qp_ex *qpx = ibv_qp_to_qp_ex(qp);
ibv_wr_start(qpx);
/* create 1st WRITE WR entry */
qpx-&gt;wr_id = my_wr_id_1;
ibv_wr_rdma_write(qpx, rkey, remote_addr_1);
ibv_wr_set_sge(qpx, lkey, local_addr_1, length_1);
/* create 2nd WRITE_WITH_IMM WR entry */
qpx-&gt;wr_id = my_wr_id_2;
qpx-&gt;wr_flags = IBV_SEND_SIGNALED;
ibv_wr_rdma_write_imm(qpx, rkey, remote_addr_2, htonl(0x1234));
ibv_set_wr_sge(qpx, lkey, local_addr_2, length_2);
/* Begin processing WRs */
ret = ibv_wr_complete(qpx);
</code></pre></dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a>(3), <a HREF="/docs/linux/man/3-ibv_create_qp_ex/">ibv_create_qp_ex</a>(3).

<h2>AUTHOR</h2>

 

 Jason Gunthorpe &lt;jgg [at] mellanox.com&gt; Guy Levi &lt;guyle [at] mellanox.com&gt; 

<h2>Index</h2>


