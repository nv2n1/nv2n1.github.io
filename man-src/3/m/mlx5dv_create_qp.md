---
title: "mlx5dv_create_qp(3)"
name: "mlx5dv_create_qp"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_create_qp/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_create_qp - creates a queue pair (QP) 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct ibv_qp *mlx5dv_create_qp(struct ibv_context *context,
                                struct ibv_qp_init_attr_ex *qp_attr,
                                struct mlx5dv_qp_init_attr *mlx5_qp_attr)
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 mlx5dv_create_qp() creates a queue pair (QP) with specific driver properties.

<h2>ARGUMENTS</h2>

 

 Please see <a HREF="/docs/linux/man/3-ibv_create_qp_ex/">ibv_create_qp_ex</a>(3) man page for context and qp_attr.

<h3>mlx5_qp_attr</h3>

<dl>
<dt>
<dd> 
struct mlx5dv_qp_init_attr {
    uint64_t comp_mask;
    uint32_t create_flags;
    struct mlx5dv_dc_init_attr dc_init_attr;
    uint64_t send_ops_flags;
};

<dt>comp_mask
<dd> Bitmask specifying what fields in the structure are valid: MLX5DV_QP_INIT_ATTR_MASK_QP_CREATE_FLAGS: valid values in create_flags MLX5DV_QP_INIT_ATTR_MASK_DC: valid values in dc_init_attr MLX5DV_QP_INIT_ATTR_MASK_SEND_OPS_FLAGS: valid values in send_ops_flags
<dt>create_flags
<dd> A bitwise OR of the various values described below.
<dl>
<dt>
<dd> 

 MLX5DV_QP_CREATE_TUNNEL_OFFLOADS: Enable offloading such as checksum and LRO for incoming tunneling traffic. 

 MLX5DV_QP_CREATE_TIR_ALLOW_SELF_LOOPBACK_UC: Allow receiving loopback unicast traffic. 

 MLX5DV_QP_CREATE_TIR_ALLOW_SELF_LOOPBACK_MC: Allow receiving loopback multicast traffic. 

 MLX5DV_QP_CREATE_DISABLE_SCATTER_TO_CQE: Disable scatter to CQE feature which is enabled by default. 

 MLX5DV_QP_CREATE_ALLOW_SCATTER_TO_CQE: Allow scatter to CQE for requester even if the qp was not configured to signal all WRs. 

 MLX5DV_QP_CREATE_PACKET_BASED_CREDIT_MODE: Set QP to work in end-to-end packet-based credit, instead of the default message-based credits (IB spec. section 9.7.7.2). 

 It is the applications responsibility to make sure that the peer QP is configured with same mode.</dl>

<dt>dc_init_attr
<dd> DC init attributes.</dl>

<h3>dc_init_attr</h3>

<dl>
<dt>
<dd> <pre><code>
struct mlx5dv_dc_init_attr {
    enum mlx5dv_dc_type dc_type;
    uint64_t dct_access_key;
};
</code></pre>
<dt>dc_type
<dd> MLX5DV_DCTYPE_DCT QP type: Target DC. MLX5DV_DCTYPE_DCI QP type: Initiator DC.
<dt>dct_access_key
<dd> used to create a DCT QP.
<dt>send_ops_flags
<dd> A bitwise OR of the various values described below.
<dl>
<dt>
<dd> 

 MLX5DV_QP_EX_WITH_MR_INTERLEAVED: Enables the mlx5dv_wr_mr_interleaved() work requset on this QP. 

 MLX5DV_QP_EX_WITH_MR_LIST: Enables the mlx5dv_wr_mr_list() work requset on this QP.</dl>
</dl>

<h2>NOTES</h2>

 

 mlx5dv_qp_ex_from_ibv_qp_ex() is used to get struct mlx5dv_qp_ex for accessing the send ops interfaces when IBV_QP_INIT_ATTR_SEND_OPS_FLAGS is used.

<h2>RETURN VALUE</h2>

 

 mlx5dv_create_qp() returns a pointer to the created QP, on error NULL will be returned and errno will be set.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_query_device_ex/">ibv_query_device_ex</a>(3), <a HREF="/docs/linux/man/3-ibv_create_qp_ex/">ibv_create_qp_ex</a>(3),

<h2>AUTHOR</h2>

 

 Yonatan Cohen &lt;yonatanc [at] mellanox.com&gt; 

<h2>Index</h2>


