---
title: "ibv_post_send(3)"
name: "ibv_post_send"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_post_send/"
description: "ibv_post_send – post a list of work requests (WRs) to a send queue"
---

<h2 class="name">NAME</h2>
<p> ibv_post_send &#8211; post a list of work requests (WRs) to a send queue </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_post_send(struct ibv_qp *qp, struct ibv_send_wr *wr,
                  struct ibv_send_wr **bad_wr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_post_send()</code> posts the linked list of work requests (WRs) starting with <i>wr</i> to the send queue of the queue pair <i>qp</i>. It stops processing WRs from this list at the first failure (that can be detected immediately while requests are being posted), and returns this failing WR through <i>bad_wr</i>. </p>
<p> The argument <i>wr</i> is an ibv_send_wr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<p>struct ibv_send_wr {<br />
    uint64_t wr_id;            /* User defined WR ID */<br />
    struct ibv_send_wr *next;  /* Pointer to next WR in list, NULL if last WR */<br />
    struct ibv_sge *sg_list;   /* Pointer to the s/g array */<br />
    int num_sge;               /* Size of the s/g array */<br />
    enum ibv_wr_opcode opcode; /* Operation type */<br />
    int send_flags;            /* Flags of the WR properties */<br />
    union {<br />
        __be32 imm_data;          /* Immediate data (in network byte order) */<br />
        uint32_t invalidate_rkey; /* Remote rkey to invalidate */<br />
    };<br />
    union {<br />
        struct {<br />
            uint64_t remote_addr; /* Start address of remote memory buffer */<br />
            uint32_t rkey;        /* Key of the remote Memory Region */<br />
        } rdma;<br />
        struct {<br />
            uint64_t remote_addr; /* Start address of remote memory buffer */<br />
            uint64_t compare_add; /* Compare operand */<br />
            uint64_t swap;        /* Swap operand */<br />
            uint32_t rkey;        /* Key of the remote Memory Region */<br />
        } atomic;<br />
        struct {<br />
            struct ibv_ah *ah;    /* Address handle (AH) for the remote node address */<br />
            uint32_t remote_qpn;  /* QP number of the destination QP */<br />
            uint32_t remote_qkey; /* Q_Key number of the destination QP */<br />
        } ud;<br />
    } wr;<br />
    union {<br />
        struct {<br />
            uint32_t remote_srqn; /* Number of the remote SRQ */<br />
        } xrc;<br />
    } qp_type;<br />
    union {<br />
        struct {<br />
            struct ibv_mw *mw;                 /* Memory window (MW) of type 2 to bind */<br />
            uint32_t rkey;                     /* The desired new rkey of the MW */<br />
            struct ibv_mw_bind_info bind_info; /* MW additional bind information */<br />
        } bind_mw;<br />
        struct {<br />
            void *hdr;       /* Pointer address of inline header */<br />
            uint16_t hdr_sz; /* Inline header size */<br />
            uint16_t mss;    /* Maximum segment size for each TSO fragment */<br />
        } tso;<br />
    };<br />
};</p>
<p>struct ibv_mw_bind_info {<br />
    struct ibv_mr *mr;   /* The Memory region (MR) to bind the MW to */<br />
    uint64_t addr;       /* The address the MW should start at */<br />
    uint64_t length;     /* The length (in bytes) the MW should span */<br />
    int mw_access_flags; /* Access flags to the MW. Use ibv_access_flags */<br />
};</p>
<p>struct ibv_sge {<br />
    uint64_t addr;   /* Start address of the local memory buffer or number of bytes from the<br />
                        start of the MR for MRs which are IBV_ZERO_BASED */<br />
    uint32_t length; /* Length of the buffer */<br />
    uint32_t lkey;   /* Key of the local Memory Region */<br />
};</p>
<p> Each QP Transport Service Type supports a specific set of opcodes, as shown in the following table: </p>
<pre><code>
OPCODE | IBV_QPT_UD | IBV_QPT_UC | IBV_QPT_RC | IBV_QPT_XRC_SEND | IBV_QPT_RAW_PACKET-- -- -- -- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- --+-- -- -- -- -- --+-- -- -- -- -- --+-- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- --IBV_WR_SEND | X | X | X | X | X IBV_WR_SEND_WITH_IMM | X | X | X | X |
    IBV_WR_RDMA_WRITE | | X | X | X |
    IBV_WR_RDMA_WRITE_WITH_IMM | | X | X | X |
    IBV_WR_RDMA_READ | | | X | X |
    IBV_WR_ATOMIC_CMP_AND_SWP | | | X | X |
    IBV_WR_ATOMIC_FETCH_AND_ADD | | | X | X |
    IBV_WR_LOCAL_INV | | X | X | X |
    IBV_WR_BIND_MW | | X | X | X |
    IBV_WR_SEND_WITH_INV | | X | X | X |
    IBV_WR_TSO | X | | | | X
</code></pre>
<p> The attribute send_flags describes the properties of the <font SIZE="-1">WR</font>. It is either 0 or the bitwise <font SIZE="-1">OR</font> of one or more of the following flags: </p>
<dl>
<dt><code>IBV_SEND_FENCE </code> Set the fence indicator. Valid only for QPs with Transport Service Type <code>IBV_QPT_RC</code></p>
<dd>
<dt><code>IBV_SEND_SIGNALED </code> Set the completion notification indicator. Relevant only if QP was created with sq_sig_all=0</p>
<dd>
<dt><code>IBV_SEND_SOLICITED </code> Set the solicited event indicator. Valid only for Send and RDMA Write with immediate</p>
<dd>
<dt><code>IBV_SEND_INLINE </code> Send data in given gather list as inline data</p>
<dd> in a send WQE. Valid only for Send and RDMA Write. The L_Key will not be checked.</p>
<dt><code>IBV_SEND_IP_CSUM </code> Offload the IPv4 and TCP/UDP checksum calculation.</p>
<dd> Valid only when <code>device_cap_flags</code> in device_attr indicates current QP is supported by checksum offload.</dl>
<h2>RETURN VALUE</h2>
<p> <code>ibv_post_send()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> The user should not alter or destroy AHs associated with WRs until request is fully executed and a work completion has been retrieved from the corresponding completion queue (CQ) to avoid unexpected behavior. </p>
<p> The buffers used by a WR can only be safely reused after WR the request is fully executed and a work completion has been retrieved from the corresponding completion queue (CQ). However, if the IBV_SEND_INLINE flag was set, the buffer can be reused immediately after the call returns. </p>
<p> IBV_WR_DRIVER1 is an opcode that should be used to issue a specific driver operation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_ah/">ibv_create_ah</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_recv/">ibv_post_recv</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_srq_recv/">ibv_post_srq_recv</a></code>(3), <code><a href="/docs/linux/man/3-ibv_poll_cq/">ibv_poll_cq</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
<dt>Majd Dibbiny &lt;majd [at] mellanox.com&gt;</p>
<dd>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
