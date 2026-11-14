---
title: "ibv_create_rwq_ind_table(3)"
name: "ibv_create_rwq_ind_table"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_create_rwq_ind_table/"
description: "ibv_create_rwq_ind_table, ibv_destroy_rwq_ind_table – create or destroy a Receive Work Queue Indirection Table (RWQ IND TBL)."
---

<h2 class="name">NAME</h2>
<p> ibv_create_rwq_ind_table, ibv_destroy_rwq_ind_table &#8211; create or destroy a Receive Work Queue Indirection Table (RWQ IND TBL). </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_rwq_ind_table *ibv_create_rwq_ind_table(struct ibv_context *context,
                                                   struct ibv_rwq_ind_table_init_attr *init_attr);
int ibv_destroy_rwq_ind_table(struct ibv_rwq_ind_table *rwq_ind_table);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_rwq_ind_table()</code> creates a RWQ IND TBL associated with the ibv_context <i>context</i>. The argument <i>init_attr</i> is an ibv_rwq_ind_table_init_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_rwq_ind_table_init_attr {
    uint32_t log_ind_tbl_size; /* Log, base 2, of Indirection table size */
    struct ibv_wq **ind_tbl;   /* Each entry is a pointer to Receive Work Queue */
    uint32_t comp_mask;        /* Identifies valid fields. Use ibv_ind_table_init_attr_mask */
};
</code></pre>
<p> The function <code>ibv_create_rwq_ind_table()</code> will create a RWQ IND TBL that holds a table of Receive Work Queue. For further usage of the created object see below <i>NOTES</i>. </p>
<p> <code>ibv_destroy_rwq_ind_table()</code> destroys the RWQ IND TBL <i>rwq_ind_table</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_rwq_ind_table()</code> returns a pointer to the created RWQ IND TBL, or NULL if the request fails. </p>
<p> <code>ibv_destroy_rwq_ind_table()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p> The created object should be used as part of <i>ibv_create_qp_ex()</i> to enable dispatching of incoming packets based on some RX hash configuration.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_create_wq/">ibv_create_wq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_modify_wq/">ibv_modify_wq</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_qp_ex/">ibv_create_qp_ex</a></code>(3),</p>
<h2>AUTHORS</h2>
<dl>
<dt>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
