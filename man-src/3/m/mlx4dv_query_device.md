---
title: "mlx4dv_query_device(3)"
name: "mlx4dv_query_device"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx4dv_query_device/"
description: "mlx4dv_query_device – Query device capabilities specific to mlx4"
---

<h2 class="name">NAME</h2>
<p> mlx4dv_query_device &#8211; Query device capabilities specific to mlx4 </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;infiniband/mlx4dv.h&gt;
int mlx4dv_query_device(struct ibv_context *ctx_in,
                        struct mlx4dv_context *attrs_out);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>mlx4dv_query_device()</code> Query mlx4 specific device information that is usable via the direct verbs interface. </p>
<p> This function returns a version and compatibility mask. The version represents the format of the internal hardware structures that mlx4dv.h exposes. Future additions of new fields to the existing structures are handled by the comp_mask field. </p>
<pre><code>
struct mlx4dv_context {
    uint8_t version;
    uint32_t max_inl_recv_sz; /* Maximum supported size of inline receive  */
    uint64_t comp_mask;
};
</code></pre>
<h2>RETURN VALUE</h2>
<p> 0 on success or the value of errno on failure (which indicates the failure reason).</p>
<h2>NOTES</h2>
<p>&nbsp;*&nbsp;Compatibility mask&nbsp;(comp_mask)&nbsp;is an in/out field.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-mlx4dv/">mlx4dv</a></code>(7), <code><a href="/docs/linux/man/3-ibv_query_device/">ibv_query_device</a></code>(3)</p>
<h2>AUTHORS</h2>
<dl>
<dt>Maor Gottlieb &lt;maorg [at] mellanox.com&gt;</p>
<dd>
</dl>
<h2>Index</h2>
