---
title: "mlx5dv_create_flow_action_modify_header(3)"
name: "mlx5dv_create_flow_action_modify_header"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_create_flow_action_modify_header/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_create_flow_action_modify_header - Flow action modify header for mlx5 provider 

<h2>SYNOPSIS</h2>

<dl>
<dt>
</dt><dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct ibv_flow_action *
mlx5dv_create_flow_action_modify_header(struct ibv_context *ctx,
                                        size_t actions_sz,
                                        uint64_t actions[],
                                        enum mlx5dv_flow_table_type ft_type)
</code></pre></dd></dl>

<h2>DESCRIPTION</h2>

 

 Create a modify header flow steering action, it allows mutating a packet header.

<h2>ARGUMENTS</h2>

<dl>
<dt>ctx
</dt><dd> RDMA device context to create the action on.
</dd><dt>actions_sz
</dt><dd> The size of actions buffer in bytes.
</dd><dt>actions
</dt><dd> A buffer which contains modify actions provided in device spec format (i.e. be64).
</dd><dt>ft_type
</dt><dd> Defines the flow table type to which the modify header action will be attached.
</dd><dl>
<dt>
</dt><dd> 
 MLX5DV_FLOW_TABLE_TYPE_NIC_RX: RX FLOW TABLE 
 MLX5DV_FLOW_TABLE_TYPE_NIC_TX: TX FLOW TABLE</dd></dl>
</dl>

<h2>RETURN VALUE</h2>

 

 Upon success mlx5dv_create_flow_action_modify_header will return a new struct ibv_flow_action object, on error NULL will be returned and errno will be set.

<h2>SEE ALSO</h2>

 

 ibv_create_flow(3), ibv_create_flow_action(3) 

<h2>Index</h2>


