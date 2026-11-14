---
title: "ibv_create_qp_ex(3)"
name: "ibv_create_qp_ex"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_create_qp_ex/"
description: "ibv_create_qp_ex, ibv_destroy_qp – create or destroy a queue pair (QP)"
---

<h2 class="name">NAME</h2>
<p> ibv_create_qp_ex, ibv_destroy_qp &#8211; create or destroy a queue pair (QP) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_qp *ibv_create_qp_ex(struct ibv_context *context,
                                struct ibv_qp_init_attr_ex *qp_init_attr);
int ibv_destroy_qp(struct ibv_qp *qp);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_qp_ex()</code> creates a queue pair (QP) associated with the protection domain <i>pd</i>. The argument <i>qp_init_attr_ex</i> is an ibv_qp_init_attr_ex struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<p>struct ibv_qp_init_attr_ex {<br />
    void *qp_context;                      /* Associated context of the QP */<br />
    struct ibv_cq *send_cq;                /* CQ to be associated with the Send Queue (SQ) */<br />
    struct ibv_cq *recv_cq;                /* CQ to be associated with the Receive Queue (RQ) */<br />
    struct ibv_srq *srq;                   /* SRQ handle if QP is to be associated with an SRQ, otherwise NULL */<br />
    struct ibv_qp_cap cap;                 /* QP capabilities */<br />
    enum ibv_qp_type qp_type;              /* QP Transport Service Type: IBV_QPT_RC, IBV_QPT_UC, IBV_QPT_UD, IBV_QPT_RAW_PACKET or IBV_QPT_DRIVER */<br />
    int sq_sig_all;                        /* If set, each Work Request (WR) submitted to the SQ generates a completion entry */<br />
    uint32_t comp_mask;                    /* Identifies valid fields */<br />
    struct ibv_pd *pd;                     /* PD to be associated with the QP */<br />
    struct ibv_xrcd *xrcd;                 /* XRC domain to be associated with the target QP */<br />
    enum ibv_qp_create_flags create_flags; /* Creation flags for this QP */<br />
    uint16_t max_tso_header;               /* Maximum TSO header size */<br />
    struct ibv_rwq_ind_table *rwq_ind_tbl; /* Indirection table to be associated with the QP */<br />
    struct ibv_rx_hash_conf rx_hash_conf;  /* RX hash configuration to be used */<br />
    uint32_t source_qpn;                   /* Source QP number, creation flag IBV_QP_CREATE_SOURCE_QPN should be set, few NOTEs below */<br />
    uint64_t send_ops_flags;               /* Select which QP send ops will be defined in struct ibv_qp_ex. Use enum ibv_qp_create_send_ops_flags */<br />
};<br />
struct ibv_qp_cap {<br />
    uint32_t max_send_wr;     /* Requested max number of outstanding WRs in the SQ */<br />
    uint32_t max_recv_wr;     /* Requested max number of outstanding WRs in the RQ */<br />
    uint32_t max_send_sge;    /* Requested max number of scatter/gather (s/g) elements in a WR in the SQ */<br />
    uint32_t max_recv_sge;    /* Requested max number of s/g elements in a WR in the SQ */<br />
    uint32_t max_inline_data; /* Requested max number of data (bytes) that can be posted inline to the SQ, otherwise 0 */<br />
};<br />
enum ibv_qp_create_flags {<br />
    IBV_QP_CREATE_BLOCK_SELF_MCAST_LB = 1 &lt;&lt; 1,    /* Prevent self multicast loopback */<br />
    IBV_QP_CREATE_SCATTER_FCS = 1 &lt;&lt; 8,            /* FCS field will be scattered to host memory */<br />
    IBV_QP_CREATE_CVLAN_STRIPPING = 1 &lt;&lt; 9,        /* CVLAN field will be stripped from incoming packets */<br />
    IBV_QP_CREATE_SOURCE_QPN = 1 &lt;&lt; 10,            /* The created QP will use the source_qpn as its wire QP number */<br />
    IBV_QP_CREATE_PCI_WRITE_END_PADDING = 1 &lt;&lt; 11, /* Incoming packets will be padded to cacheline size */<br />
};</p>
<p>struct ibv_rx_hash_conf {<br />
    uint8_t rx_hash_function;     /* RX hash function, use enum ibv_rx_hash_function_flags */<br />
    uint8_t rx_hash_key_len;      /* RX hash key length */<br />
    uint8_t *rx_hash_key;         /* RX hash key data */<br />
    uint64_t rx_hash_fields_mask; /* RX fields that should participate in the hashing, use enum ibv_rx_hash_fields */<br />
};</p>
<p>enum ibv_rx_hash_fields {<br />
    IBV_RX_HASH_SRC_IPV4 = 1 &lt;&lt; 0,<br />
    IBV_RX_HASH_DST_IPV4 = 1 &lt;&lt; 1,<br />
    IBV_RX_HASH_SRC_IPV6 = 1 &lt;&lt; 2,<br />
    IBV_RX_HASH_DST_IPV6 = 1 &lt;&lt; 3,<br />
    IBV_RX_HASH_SRC_PORT_TCP = 1 &lt;&lt; 4,<br />
    IBV_RX_HASH_DST_PORT_TCP = 1 &lt;&lt; 5,<br />
    IBV_RX_HASH_SRC_PORT_UDP = 1 &lt;&lt; 6,<br />
    IBV_RX_HASH_DST_PORT_UDP = 1 &lt;&lt; 7,<br />
    IBV_RX_HASH_IPSEC_SPI = 1 &lt;&lt; 8,<br />
    /* When using tunneling protocol, e.g. VXLAN, then we have an inner (encapsulated packet) and outer.<br />
     * For applying RSS on the inner packet, then the following field should be set with one of the L3/L4 fields.<br />
     */<br />
    IBV_RX_HASH_INNER = (1UL &lt;&lt; 31),<br />
};</p>
<pre><code>
struct ibv_qp_create_send_ops_flags {
    IBV_QP_EX_WITH_RDMA_WRITE = 1 &lt;&lt; 0,
    IBV_QP_EX_WITH_RDMA_WRITE_WITH_IMM = 1 &lt;&lt; 1,
    IBV_QP_EX_WITH_SEND = 1 &lt;&lt; 2,
    IBV_QP_EX_WITH_SEND_WITH_IMM = 1 &lt;&lt; 3,
    IBV_QP_EX_WITH_RDMA_READ = 1 &lt;&lt; 4,
    IBV_QP_EX_WITH_ATOMIC_CMP_AND_SWP = 1 &lt;&lt; 5,
    IBV_QP_EX_WITH_ATOMIC_FETCH_AND_ADD = 1 &lt;&lt; 6,
    IBV_QP_EX_WITH_LOCAL_INV = 1 &lt;&lt; 7,
    IBV_QP_EX_WITH_BIND_MW = 1 &lt;&lt; 8,
    IBV_QP_EX_WITH_SEND_WITH_INV = 1 &lt;&lt; 9,
    IBV_QP_EX_WITH_TSO = 1 &lt;&lt; 10,
};
</code></pre>
<p> The function <code>ibv_create_qp_ex()</code> will update the <i>qp_init_attr_ex</i>-&gt;cap struct with the actual <font SIZE="-1">QP</font> values of the QP that was created; the values will be greater than or equal to the values requested. </p>
<p> <code>ibv_destroy_qp()</code> destroys the QP <i>qp</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_qp_ex()</code> returns a pointer to the created QP, or NULL if the request fails. Check the QP number (<code>qp_num</code>) in the returned QP. </p>
<p> <code>ibv_destroy_qp()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> The attributes max_recv_wr and max_recv_sge are ignored by <code>ibv_create_qp_ex()</code> if the QP is to be associated with an SRQ. </p>
<p> The attribute source_qpn is supported only on UD QP, without flow steering RX should not be possible. </p>
<p> Use <code>ibv_qp_to_qp_ex()</code> to get the <i>ibv_qp_ex</i> for accessing the send ops iterator interface, when QP create attr IBV_QP_INIT_ATTR_SEND_OPS_FLAGS is used. </p>
<p> <code>ibv_destroy_qp()</code> fails if the QP is attached to a multicast group. </p>
<p> <code>IBV_QPT_DRIVER</code> does not represent a specific service and is used for vendor specific QP logic.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_modify_qp/">ibv_modify_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_qp/">ibv_query_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_rwq_ind_table/">ibv_create_rwq_ind_table</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
