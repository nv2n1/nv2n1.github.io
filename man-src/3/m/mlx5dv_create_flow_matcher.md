---
title: "mlx5dv_create_flow_matcher(3)"
name: "mlx5dv_create_flow_matcher"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_create_flow_matcher/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_create_flow_matcher - creates a matcher to be used with 

 <a HREF="/docs/linux/man/3-mlx5dv_create_flow/">mlx5dv_create_flow</a>(3)

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct mlx5dv_flow_matcher *
mlx5dv_create_flow_matcher(struct ibv_context *context,
                           struct mlx5dv_flow_matcher_attr *attr)
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 mlx5dv_create_flow_matcher() creates a flow matcher (mask) to be used with <a HREF="/docs/linux/man/3-mlx5dv_create_flow/">mlx5dv_create_flow</a>(3).

<h2>ARGUMENTS</h2>

 

 Please see <a HREF="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a>(3) for context.

<h3>attr</h3>

<dl>
<dt>
<dd> 
struct mlx5dv_flow_matcher_attr {
    enum ibv_flow_attr_type type;
    uint32_t flags; /* From enum ibv_flow_flags */
    uint16_t priority;
    uint8_t match_criteria_enable; /* Device spec format */
    struct mlx5dv_flow_match_parameters *match_mask;
    uint64_t comp_mask;
    enum mlx5dv_flow_table_type ft_type;
};

<dt>type
<dd> Type of matcher to be created: IBV_FLOW_ATTR_NORMAL: Normal rule according to specification.
<dt>flags
<dd> special flags to control rule: 0: Nothing or zero value means matcher will store ingress flow rules. IBV_FLOW_ATTR_FLAGS_EGRESS: Specified this matcher will store egress flow rules.
<dt>priority
<dd> See <a HREF="/docs/linux/man/3-ibv_create_flow/">ibv_create_flow</a>(3).
<dt>match_criteria_enable
<dd> What match criteria is configured in match_mask, passed in device spec format.</dl>

<h3>match_mask</h3>

<dl>
<dt>
<dd> <pre><code>
struct mlx5dv_flow_match_parameters {
    size_t match_sz;
    uint64_t match_buf[]; /* Device spec format */
};
</code></pre>
<dt>match_sz
<dd> Size in bytes of match_buf.
<dt>match_buf
<dd> Set which mask to be used, passed in device spec format.
<dt>comp_mask
<dd> MLX5DV_FLOW_MATCHER_MASK_FT_TYPE for ft_type</dl>

<h3>ft_type</h3>

 

 Specified in which flow table type, the matcher will store the flow rules: MLX5DV_FLOW_TABLE_TYPE_NIC_RX: Specified this matcher will store ingress flow rules. MLX5DV_FLOW_TABLE_TYPE_NIC_TX Specified this matcher will store egress flow rules. MLX5DV_FLOW_TABLE_TYPE_FDB : Specified this matcher will store FDB rules. MLX5DV_FLOW_TABLE_TYPE_RDMA_RX: Specified this matcher will store ingress RDMA flow rules.

<h2>RETURN VALUE</h2>

 

 mlx5dv_create_flow_matcher returns a pointer to mlx5dv_flow_matcher, on error NULL will be returned and errno will be set.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a>(3), <a HREF="/docs/linux/man/3-ibv_create_flow/">ibv_create_flow</a>(3)

<h2>AUTHOR</h2>

 

 Mark Bloch &lt;markb [at] mellanox.com&gt; 

<h2>Index</h2>


