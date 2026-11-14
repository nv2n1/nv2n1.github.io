---
title: "ibv_create_cq_ex(3)"
name: "ibv_create_cq_ex"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_create_cq_ex/"
description: "ibv_create_cq_ex – create a completion queue (CQ)"
---

<h2 class="name">NAME</h2>
<p> ibv_create_cq_ex &#8211; create a completion queue (CQ) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_cq_ex *ibv_create_cq_ex(struct ibv_context *context,
                                   struct ibv_cq_init_attr_ex *cq_attr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_cq_ex()</code> creates a completion queue (CQ) for RDMA device context <i>context</i>. The argument <i>cq_attr</i> is a pointer to struct ibv_cq_init_attr_ex as defined in &lt;infiniband/verbs.h&gt;. </p>
<p>struct ibv_cq_init_attr_ex {<br />
    int cqe;                          /* Minimum number of entries required for CQ */<br />
    void *cq_context;                 /* Consumer-supplied context returned for completion events */<br />
    struct ibv_comp_channel *channel; /* Completion channel where completion events will be queued. May be NULL if completion events will not be used. */<br />
    int comp_vector;                  /* Completion vector used to signal completion events. Must be &gt;= 0 and &lt; context-&gt;num_comp_vectors. */<br />
    uint64_t wc_flags;                /* The wc_flags that should be returned in ibv_poll_cq_ex. Or&#8217;ed bit of enum ibv_wc_flags_ex. */<br />
    uint32_t comp_mask;               /* compatibility mask (extended verb). */<br />
    uint32_t flags                    /* One or more flags from enum ibv_create_cq_attr_flags */<br />
};<br />
enum ibv_wc_flags_ex {<br />
    IBV_WC_EX_WITH_BYTE_LEN = 1 &lt;&lt; 0,                        /* Require byte len in WC */<br />
    IBV_WC_EX_WITH_IMM = 1 &lt;&lt; 1,                             /* Require immediate in WC */<br />
    IBV_WC_EX_WITH_QP_NUM = 1 &lt;&lt; 2,                          /* Require QP number in WC */<br />
    IBV_WC_EX_WITH_SRC_QP = 1 &lt;&lt; 3,                          /* Require source QP in WC */<br />
    IBV_WC_EX_WITH_SLID = 1 &lt;&lt; 4,                            /* Require slid in WC */<br />
    IBV_WC_EX_WITH_SL = 1 &lt;&lt; 5,                              /* Require sl in WC */<br />
    IBV_WC_EX_WITH_DLID_PATH_BITS = 1 &lt;&lt; 6,                  /* Require dlid path bits in WC */<br />
    IBV_WC_EX_WITH_COMPLETION_TIMESTAMP = 1 &lt;&lt; 7,            /* Require completion device timestamp in WC /*<br />
             IBV_WC_EX_WITH_CVLAN                 = 1 &lt;&lt; 8,  /* Require VLAN info in WC */<br />
    IBV_WC_EX_WITH_FLOW_TAG = 1 &lt;&lt; 9,                        /* Require flow tag in WC */<br />
    IBV_WC_EX_WITH_COMPLETION_TIMESTAMP_WALLCLOCK = 1 &lt;&lt; 11, /* Require completion wallclock timestamp in WC */<br />
};<br />
enum ibv_cq_init_attr_mask {<br />
    IBV_CQ_INIT_ATTR_MASK_FLAGS = 1 &lt;&lt; 0,<br />
};<br />
enum ibv_create_cq_attr_flags {<br />
    IBV_CREATE_CQ_ATTR_SINGLE_THREADED = 1 &lt;&lt; 0, /* This CQ is used from a single threaded, thus no locking is required */<br />
    IBV_CREATE_CQ_ATTR_IGNORE_OVERRUN = 1 &lt;&lt; 1,  /* This CQ will not pass to error state if overrun, CQE always will be written to next entry.<br />
                                                  * An application must be designed to avoid ever overflowing the CQ, otherwise CQEs might be lost.<br />
                                                  */<br />
};</p>
<h2>Polling an extended CQ</h2>
<p> In order to poll an extended CQ efficiently, a user could use the following functions. </p>
<dl>
<dt><code>Completion iterator functions</code></p>
<dd>
<p> <code>int ibv_start_poll(struct ibv_cq_ex </code><i>*cq</i><code>, struct ibv_poll_cq_attr </code><i>*attr)</i><br />
 Start polling a batch of work completions. <i>attr</i> is given in order to make this function easily extensible in the future. This function either returns 0 on success or an error code otherwise. When no completions are available on the CQ, ENOENT is returned, but the CQ remains in a valid state. On success, querying the completion&#8217;s attribute could be done using the query functions described below. If an error code is given, end_poll shouldn&#8217;t be called. </p>
<p> <code>int ibv_next_poll(struct ibv_cq_ex </code><i>*cq)</i><br />
 This function is called in order to get the next work completion. It has to be called after <i>start_poll</i> and before <i>end_poll</i> are called. This function either returns 0 on success or an error code otherwise. When no completions are available on the CQ, ENOENT is returned, but the CQ remains in a valid state. On success, querying the completion&#8217;s attribute could be done using the query functions described below. If an error code is given, end_poll should still be called, indicating this is the end of the polled batch. </p>
<p> <code>void ibv_end_poll(struct ibv_cq_ex </code><i>*cq)</i><br />
 This function indicates the end of polling batch of work completions. After calling this function, the user should start a new batch by calling <i>start_poll.</i> </p>
<dt><code>Polling fields in the completion</code></p>
<dd> Below members and functions are used in order to poll the current completion. The current completion is the completion which the iterator points to (start_poll and next_poll advances this iterator). Only fields that the user requested via wc_flags in ibv_create_cq_ex could be queried. In addition, some fields are only valid in certain opcodes and status codes. </p>
<p> <code>uint64_t wr_id &#8211; Can be accessed directly from struct ibv_cq_ex.</code> </p>
<p> <code>enum ibv_wc_status &#8211; Can be accessed directly from struct ibv_cq_ex.</code> </p>
<p> <code>enum ibv_wc_opcode ibv_wc_read_opcode(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the opcode from the current completion. </p>
<p> <code>uint32_t ibv_wc_read_vendor_err(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the vendor error from the current completion. </p>
<p> <code>uint32_t ibv_wc_read_byte_len(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the vendor error from the current completion. </p>
<p> <code>__be32 ibv_wc_read_imm_data(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the immediate data field from the current completion. </p>
<p> <code>uint32_t ibv_wc_read_invalidated_rkey(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the rkey invalided by the SEND_INVAL from the current completion. </p>
<p> <code>uint32_t ibv_wc_read_qp_num(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the QP number field from the current completion. </p>
<p> <code>uint32_t ibv_wc_read_src_qp(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the source QP number field from the current completion. </p>
<p> <code>int ibv_wc_read_wc_flags(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the QP flags field from the current completion. </p>
<p> <code>uint16_t ibv_wc_read_pkey_index(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the pkey index field from the current completion. </p>
<p> <code>uint32_t ibv_wc_read_slid(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the slid field from the current completion. </p>
<p> <code>uint8_t ibv_wc_read_sl(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the sl field from the current completion. </p>
<p> <code>uint8_t ibv_wc_read_dlid_path_bits(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the dlid_path_bits field from the current completion. </p>
<p> <code>uint64_t ibv_wc_read_completion_ts(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the completion timestamp from the current completion in HCA clock units. </p>
<p> <code>uint64_t ibv_wc_read_completion_wallclock_ns(struct ibv_cq_ex </code><i>*cq</i><code>);</code> Get the completion timestamp from the current completion and convert it from HCA clock units to wall clock nanoseconds. </p>
<p> <code>uint16_t ibv_wc_read_cvlan(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get the CVLAN field from the current completion. </p>
<p> <code>uint32_t ibv_wc_read_flow_tag(struct ibv_cq_ex </code><i>*cq);</i><br />
&nbsp;Get flow tag from the current completion. </p>
<p> <code>void ibv_wc_read_tm_info(struct ibv_cq_ex </code><i>*cq</i><code>,</code> <code>struct ibv_wc_tm_info </code><i>*tm_info</i><code>); </code><br />
&nbsp;Get tag matching info from the current completion. </p>
<pre><code>
struct ibv_wc_tm_info {
    uint64_t tag;  /* tag from TMH */
    uint32_t priv; /* opaque user data from TMH */
};
</code></pre>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_cq_ex()</code> returns a pointer to the CQ, or NULL if the request fails.</p>
<h2>NOTES</h2>
<p> <code>ibv_create_cq_ex()</code> may create a CQ with size greater than or equal to the requested size. Check the cqe attribute in the returned CQ for the actual size. </p>
<p> CQ should be destroyed with ibv_destroy_cq. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_cq/">ibv_create_cq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_destroy_cq/">ibv_destroy_cq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_resize_cq/">ibv_resize_cq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_req_notify_cq/">ibv_req_notify_cq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_ack_cq_events/">ibv_ack_cq_events</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Matan Barak &lt;matanb [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
