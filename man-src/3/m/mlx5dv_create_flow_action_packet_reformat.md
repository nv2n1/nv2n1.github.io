---
title: "mlx5dv_create_flow_action_packet_reformat(3)"
name: "mlx5dv_create_flow_action_packet_reformat"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_create_flow_action_packet_reformat/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_create_flow_action_packet_reformat - Flow action reformat packet for mlx5 provider 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct ibv_flow_action *
mlx5dv_create_flow_action_packet_reformat(struct ibv_context *ctx,
                                          size_t data_sz,
                                          void *data,
                                          enum mlx5dv_flow_action_packet_reformat_type reformat_type,
                                          enum mlx5dv_flow_table_type ft_type)
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Create a packet reformat flow steering action. It allows adding/removing packet headers.

<h2>ARGUMENTS</h2>

<dl>
<dt>ctx
<dd>
<dt>
<dd> <pre>
RDMA device context to create the action on.
</pre>
<dt>data_sz
<dd>
<dt>
<dd> <pre>
The size of *data* buffer.
</pre>
<dt>data
<dd>
<dt>
<dd> <pre>
A buffer which contains headers in case the actions requires them.
</pre>
<dt>reformat_type
<dd>
<dt>
<dd> <pre>
The reformat type to be create. Use enum mlx5dv_flow_action_packet_reformat_type.
</pre>
<dl>
<dt>
<dd> 

 MLX5DV_FLOW_ACTION_PACKET_REFORMAT_TYPE_L2_TUNNEL_TO_L2: Decap a generic L2 tunneled packet up to inner L2. 

 MLX5DV_FLOW_ACTION_PACKET_REFORMAT_TYPE_L2_TO_L2_TUNNEL: Generic encap, data should contain the encapsulating headers. 

 MLX5DV_FLOW_ACTION_PACKET_REFORMAT_TYPE_L3_TUNNEL_TO_L2: Will do decap where the inner packet starts from L3. data should be MAC or MAC + vlan (14 or 18 bytes) to be appended to the packet after the decap action. 

 MLX5DV_FLOW_ACTION_PACKET_REFORMAT_TYPE_L2_TO_L3_TUNNEL: Will do encap where is L2 of the original packet will not be included. data should be the encapsulating header.</dl>

<dt>ft_type
<dd>
<dt>
<dd> <pre>
It defines the flow table type to which the packet reformat action
</pre>
<dl>
<dt>
<dd> will be attached.</dl>
</dl>

<h2>RETURN VALUE</h2>

 

 Upon success mlx5dv_create_flow_action_packet_reformat will return a new struct ibv_flow_action object, on error NULL will be returned and errno will be set.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_create_flow/">ibv_create_flow</a>(3), <a HREF="/docs/linux/man/3-ibv_create_flow_action/">ibv_create_flow_action</a>(3) 

<h2>Index</h2>


