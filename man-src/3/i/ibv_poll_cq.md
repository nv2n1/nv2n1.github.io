---
title: "ibv_poll_cq(3)"
name: "ibv_poll_cq"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_poll_cq/"
description: "ibv_poll_cq – poll a completion queue (CQ)"
---

<h2 class="name">NAME</h2>
<p> ibv_poll_cq &#8211; poll a completion queue (CQ) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
int ibv_poll_cq(struct ibv_cq *cq, int num_entries,
                struct ibv_wc *wc);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_poll_cq()</code> polls the CQ <i>cq</i> for work completions and returns the first <i>num_entries</i> (or all available completions if the CQ contains fewer than this number) in the array <i>wc</i>. The argument <i>wc</i> is a pointer to an array of ibv_wc structs, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_wc {
    uint64_t wr_id;            /* ID of the completed Work Request (WR) */
    enum ibv_wc_status status; /* Status of the operation */
    enum ibv_wc_opcode opcode; /* Operation type specified in the completed WR */
    uint32_t vendor_err;       /* Vendor error syndrome */
    uint32_t byte_len;         /* Number of bytes transferred */
    union {
        __be32 imm_data;           /* Immediate data (in network byte order) */
        uint32_t invalidated_rkey; /* Local RKey that was invalidated */
    };
    uint32_t qp_num;        /* Local QP number of completed WR */
    uint32_t src_qp;        /* Source QP number (remote QP number) of completed WR (valid only for UD QPs) */
    int wc_flags;           /* Flags of the completed WR */
    uint16_t pkey_index;    /* P_Key index (valid only for GSI QPs) */
    uint16_t slid;          /* Source LID */
    uint8_t sl;             /* Service Level */
    uint8_t dlid_path_bits; /* DLID path bits (not applicable for multicast messages) */
};
</code></pre>
<p> The attribute wc_flags describes the properties of the work completion. It is either 0 or the bitwise OR of one or more of the following flags: </p>
<dl>
<dt><code>IBV_WC_GRH </code> GRH is present (valid only for UD QPs)</p>
<dd>
<dt><code>IBV_WC_WITH_IMM </code> Immediate data value is valid</p>
<dd>
<dt><code>IBV_WC_WITH_INV </code> Invalidated RKey data value is valid (cannot be combined with IBV_WC_WITH_IMM)</p>
<dd>
<dt><code>IBV_WC_IP_CSUM_OK </code> TCP/UDP checksum over IPv4 and IPv4 header checksum are</p>
<dd> verified. Valid only when <code>device_cap_flags</code> in device_attr indicates current QP is supported by checksum offload.</dl>
<p> Not all <i>wc</i> attributes are always valid. If the completion status is other than <code>IBV_WC_SUCCESS</code>, only the following attributes are valid: wr_id, status, qp_num, and vendor_err.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>ibv_poll_cq()</code> returns a non-negative value equal to the number of completions found. On failure, a negative value is returned.</p>
<h2>NOTES</h2>
<p> Each polled completion is removed from the CQ and cannot be returned to it. </p>
<p> The user should consume work completions at a rate that prevents CQ overrun from occurrence. In case of a CQ overrun, the async event <code>IBV_EVENT_CQ_ERR</code> will be triggered, and the CQ cannot be used. </p>
<p> IBV_WC_DRIVER1 will be reported as a response to IBV_WR_DRIVER1 opcode.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a></code>(3), <code><a href="/docs/linux/man/3-ibv_post_recv/">ibv_post_recv</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
