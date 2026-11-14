---
title: "ibv_modify_qp(3)"
name: "ibv_modify_qp"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_modify_qp/"
description: "ibv_modify_qp – modify the attributes of a queue pair (QP)"
---

<h2 class="name">NAME</h2>
<p> ibv_modify_qp &#8211; modify the attributes of a queue pair (QP) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_modify_qp(struct ibv_qp *qp, struct ibv_qp_attr *attr,
                  int attr_mask);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_modify_qp()</code> modifies the attributes of QP <i>qp</i> with the attributes in <i>attr</i> according to the mask <i>attr_mask</i>. The argument <i>attr</i> is an ibv_qp_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<p>struct ibv_qp_attr {<br />
    enum ibv_qp_state qp_state;        /* Move the QP to this state */<br />
    enum ibv_qp_state cur_qp_state;    /* Assume this is the current QP state */<br />
    enum ibv_mtu path_mtu;             /* Path MTU (valid only for RC/UC QPs) */<br />
    enum ibv_mig_state path_mig_state; /* Path migration state (valid if HCA supports APM) */<br />
    uint32_t qkey;                     /* Q_Key for the QP (valid only for UD QPs) */<br />
    uint32_t rq_psn;                   /* PSN for receive queue (valid only for RC/UC QPs) */<br />
    uint32_t sq_psn;                   /* PSN for send queue (valid only for RC/UC QPs) */<br />
    uint32_t dest_qp_num;              /* Destination QP number (valid only for RC/UC QPs) */<br />
    int qp_access_flags;               /* Mask of enabled remote access operations (valid only for RC/UC QPs) */<br />
    struct ibv_qp_cap cap;             /* QP capabilities (valid if HCA supports QP resizing) */<br />
    struct ibv_ah_attr ah_attr;        /* Primary path address vector (valid only for RC/UC QPs) */<br />
    struct ibv_ah_attr alt_ah_attr;    /* Alternate path address vector (valid only for RC/UC QPs) */<br />
    uint16_t pkey_index;               /* Primary P_Key index */<br />
    uint16_t alt_pkey_index;           /* Alternate P_Key index */<br />
    uint8_t en_sqd_async_notify;       /* Enable SQD.drained async notification (Valid only if qp_state is SQD) */<br />
    uint8_t sq_draining;               /* Is the QP draining? Irrelevant for ibv_modify_qp() */<br />
    uint8_t max_rd_atomic;             /* Number of outstanding RDMA reads &amp; atomic operations on the destination QP (valid only for RC QPs) */<br />
    uint8_t max_dest_rd_atomic;        /* Number of responder resources for handling incoming RDMA reads &amp; atomic operations (valid only for RC QPs) */<br />
    uint8_t min_rnr_timer;             /* Minimum RNR NAK timer (valid only for RC QPs) */<br />
    uint8_t port_num;                  /* Primary port number */<br />
    uint8_t timeout;                   /* Local ack timeout for primary path (valid only for RC QPs) */<br />
    uint8_t retry_cnt;                 /* Retry count (valid only for RC QPs) */<br />
    uint8_t rnr_retry;                 /* RNR retry (valid only for RC QPs) */<br />
    uint8_t alt_port_num;              /* Alternate port number */<br />
    uint8_t alt_timeout;               /* Local ack timeout for alternate path (valid only for RC QPs) */<br />
    uint32_t rate_limit;               /* Rate limit in kbps for packet pacing */<br />
};</p>
<p> For details on struct ibv_qp_cap see the description of <code>ibv_create_qp()</code>. For details on struct ibv_ah_attr see the description of <code>ibv_create_ah()</code>. </p>
<p> The argument <i>attr_mask</i> specifies the QP attributes to be modified. The argument is either 0 or the bitwise OR of one or more of the following flags: </p>
<dl>
<dt><code>IBV_QP_STATE </code> Modify qp_state</p>
<dd>
<dt><code>IBV_QP_CUR_STATE </code> Set cur_qp_state</p>
<dd>
<dt><code>IBV_QP_EN_SQD_ASYNC_NOTIFY </code> Set en_sqd_async_notify</p>
<dd>
<dt><code>IBV_QP_ACCESS_FLAGS </code> Set qp_access_flags</p>
<dd>
<dt><code>IBV_QP_PKEY_INDEX </code> Set pkey_index</p>
<dd>
<dt><code>IBV_QP_PORT </code> Set port_num</p>
<dd>
<dt><code>IBV_QP_QKEY </code> Set qkey</p>
<dd>
<dt><code>IBV_QP_AV </code> Set ah_attr</p>
<dd>
<dt><code>IBV_QP_PATH_MTU </code> Set path_mtu</p>
<dd>
<dt><code>IBV_QP_TIMEOUT </code> Set timeout</p>
<dd>
<dt><code>IBV_QP_RETRY_CNT </code> Set retry_cnt</p>
<dd>
<dt><code>IBV_QP_RNR_RETRY </code> Set rnr_retry</p>
<dd>
<dt><code>IBV_QP_RQ_PSN </code> Set rq_psn</p>
<dd>
<dt><code>IBV_QP_MAX_QP_RD_ATOMIC </code> Set max_rd_atomic</p>
<dd>
<dt><code>IBV_QP_ALT_PATH </code> Set the alternative path via: alt_ah_attr, alt_pkey_index, alt_port_num, alt_timeout</p>
<dd>
<dt><code>IBV_QP_MIN_RNR_TIMER </code> Set min_rnr_timer</p>
<dd>
<dt><code>IBV_QP_SQ_PSN </code> Set sq_psn</p>
<dd>
<dt><code>IBV_QP_MAX_DEST_RD_ATOMIC </code> Set max_dest_rd_atomic</p>
<dd>
<dt><code>IBV_QP_PATH_MIG_STATE </code> Set path_mig_state</p>
<dd>
<dt><code>IBV_QP_CAP </code> Set cap</p>
<dd>
<dt><code>IBV_QP_DEST_QPN </code> Set dest_qp_num</p>
<dd> <code>IBV_QP_RATE_LIMIT </code> Set rate_limit</dl>
<h2>RETURN VALUE</h2>
<p> <code>ibv_modify_qp()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> If any of the modify attributes or the modify mask are invalid, none of the attributes will be modified (including the QP state). </p>
<p> Not all devices support resizing QPs. To check if a device supports it, check if the <code>IBV_DEVICE_RESIZE_MAX_WR</code> bit is set in the device capabilities flags. </p>
<p> Not all devices support alternate paths. To check if a device supports it, check if the <code>IBV_DEVICE_AUTO_PATH_MIG</code> bit is set in the device capabilities flags. </p>
<p> The following tables indicate for each QP Transport Service Type, the minimum list of attributes that must be changed upon transitioning QP state from: Reset &#8211;&gt; Init &#8211;&gt; RTR &#8211;&gt; RTS. </p>
<p>For QP Transport Service Type IBV_QPT_UD : Next state Required attributes&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Init IBV_QP_STATE, IBV_QP_PKEY_INDEX, IBV_QP_PORT, IBV_QP_QKEY RTR IBV_QP_STATE RTS IBV_QP_STATE, IBV_QP_SQ_PSN</p>
<p>For QP Transport Service Type IBV_QPT_UC : Next state Required attributes&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Init IBV_QP_STATE, IBV_QP_PKEY_INDEX, IBV_QP_PORT, IBV_QP_ACCESS_FLAGS RTR IBV_QP_STATE, IBV_QP_AV, IBV_QP_PATH_MTU, IBV_QP_DEST_QPN, IBV_QP_RQ_PSN RTS IBV_QP_STATE, IBV_QP_SQ_PSN</p>
<p>For QP Transport Service Type IBV_QPT_RC : Next state Required attributes&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Init IBV_QP_STATE, IBV_QP_PKEY_INDEX, IBV_QP_PORT, IBV_QP_ACCESS_FLAGS RTR IBV_QP_STATE, IBV_QP_AV, IBV_QP_PATH_MTU, IBV_QP_DEST_QPN, IBV_QP_RQ_PSN, IBV_QP_MAX_DEST_RD_ATOMIC, IBV_QP_MIN_RNR_TIMER RTS IBV_QP_STATE, IBV_QP_SQ_PSN, IBV_QP_MAX_QP_RD_ATOMIC, IBV_QP_RETRY_CNT, IBV_QP_RNR_RETRY, IBV_QP_TIMEOUT</p>
<pre><code>
For QP Transport Service Type IBV_QPT_RAW_PACKET : Next state Required attributes-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --Init IBV_QP_STATE, IBV_QP_PORT RTR IBV_QP_STATE RTS IBV_QP_STATE
</code></pre>
<p> If port flag IBV_QPF_GRH_REQUIRED is set then ah_attr and alt_ah_attr must be passed with definition of &#8216;struct ibv_ah_attr { .is_global = 1; .grh = {&#8230;}; }&#8217;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_qp/">ibv_create_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_destroy_qp/">ibv_destroy_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_query_qp/">ibv_query_qp</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_ah/">ibv_create_ah</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
