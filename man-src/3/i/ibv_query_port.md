---
title: "ibv_query_port(3)"
name: "ibv_query_port"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_query_port/"
description: "ibv_query_port – query an RDMA port’s attributes"
---

<h2 class="name">NAME</h2>
<p> ibv_query_port &#8211; query an RDMA port&#8217;s attributes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_query_port(struct ibv_context *context, uint8_t port_num,
                   struct ibv_port_attr *port_attr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_query_port()</code> returns the attributes of port <i>port_num</i> for device context <i>context</i> through the pointer <i>port_attr</i>. The argument <i>port_attr</i> is an ibv_port_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_port_attr {
    enum ibv_port_state state; /* Logical port state */
    enum ibv_mtu max_mtu;      /* Max MTU supported by port */
    enum ibv_mtu active_mtu;   /* Actual MTU */
    int gid_tbl_len;           /* Length of source GID table */
    uint32_t port_cap_flags;   /* Port capabilities */
    uint32_t max_msg_sz;       /* Maximum message size */
    uint32_t bad_pkey_cntr;    /* Bad P_Key counter */
    uint32_t qkey_viol_cntr;   /* Q_Key violation counter */
    uint16_t pkey_tbl_len;     /* Length of partition table */
    uint16_t lid;              /* Base port LID */
    uint16_t sm_lid;           /* SM LID */
    uint8_t lmc;               /* LMC of LID */
    uint8_t max_vl_num;        /* Maximum number of VLs */
    uint8_t sm_sl;             /* SM service level */
    uint8_t subnet_timeout;    /* Subnet propagation delay */
    uint8_t init_type_reply;   /* Type of initialization performed by SM */
    uint8_t active_width;      /* Currently active link width */
    uint8_t active_speed;      /* Currently active link speed */
    uint8_t phys_state;        /* Physical port state */
    uint8_t link_layer;        /* link layer protocol of the port */
    uint8_t flags;             /* Port flags */
    uint16_t port_cap_flags2;  /* Port capabilities */
};
possible values for the link layer field are IBV_LINK_LAYER_INFINIBAND,
IBV_LINK_LAYER_ETHERNET, or IBV_LINK_LAYER_UNSPECIFIED.
supported port flags:
IBV_QPF_GRH_REQUIRED - When this flag is set, the applications must create all AH with GRH configured.
</code></pre>
<h2>RETURN VALUE</h2>
<p> <code>ibv_query_port()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_destroy_qp/">ibv_destroy_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_qp/">ibv_query_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_ah/">ibv_create_ah</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
