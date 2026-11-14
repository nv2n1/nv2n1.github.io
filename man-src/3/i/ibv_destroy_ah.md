---
title: "ibv_destroy_ah(3)"
name: "ibv_destroy_ah"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ibv_destroy_ah/"
description: "ibv_create_ah, ibv_destroy_ah – create or destroy an address handle (AH)"
---

<h2 class="name">NAME</h2>
<p> ibv_create_ah, ibv_destroy_ah &#8211; create or destroy an address handle (AH) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/verbs.h&gt;
struct ibv_ah *ibv_create_ah(struct ibv_pd *pd,
                             struct ibv_ah_attr *attr);
int ibv_destroy_ah(struct ibv_ah *ah);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ibv_create_ah()</code> creates an address handle (AH) associated with the protection domain <i>pd</i>. The argument <i>attr</i> is an ibv_ah_attr struct, as defined in &lt;infiniband/verbs.h&gt;. </p>
<pre><code>
struct ibv_ah_attr {
    struct ibv_global_route grh; /* Global Routing Header (GRH) attributes */
    uint16_t dlid;               /* Destination LID */
    uint8_t sl;                  /* Service Level */
    uint8_t src_path_bits;       /* Source path bits */
    uint8_t static_rate;         /* Maximum static rate */
    uint8_t is_global;           /* GRH attributes are valid */
    uint8_t port_num;            /* Physical port number */
};
struct ibv_global_route {
    union ibv_gid dgid;    /* Destination GID or MGID */
    uint32_t flow_label;   /* Flow label */
    uint8_t sgid_index;    /* Source GID index */
    uint8_t hop_limit;     /* Hop limit */
    uint8_t traffic_class; /* Traffic class */
};
</code></pre>
<p> <code>ibv_destroy_ah()</code> destroys the AH <i>ah</i>.</p>
<h2>RETURN VALUE</h2>
<p> <code>ibv_create_ah()</code> returns a pointer to the created AH, or NULL if the request fails.</p>
<h2>NOTES</h2>
<p> If port flag IBV_QPF_GRH_REQUIRED is set then <code>ibv_create_ah()</code> must be created with definition of &#8216;struct ibv_ah_attr { .is_global = 1; .grh = {&#8230;}; }&#8217;. </p>
<p> <code>ibv_destroy_ah()</code> returns 0 on success, or the value of errno on failure (which indicates the failure reason).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ibv_alloc_pd/">ibv_alloc_pd</a></code>(3), <code><a href="/docs/linux/man/3-ibv_init_ah_from_wc/">ibv_init_ah_from_wc</a></code>(3), <code><a href="/docs/linux/man/3-ibv_create_ah_from_wc/">ibv_create_ah_from_wc</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Dotan Barak &lt;dotanba [at] gmail.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
