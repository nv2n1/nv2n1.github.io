---

title: "mlx5dv_create_cq(3)"
name: "mlx5dv_create_cq"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_create_cq/"
---

mlx5dv_create_cq - creates a completion queue (CQ) 

<h2>SYNOPSIS</h2>

<dl>
<dt>
</dt><dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct ibv_cq_ex *mlx5dv_create_cq(struct ibv_context *context,
                                   struct ibv_cq_init_attr_ex *cq_attr,
                                   struct mlx5dv_cq_init_attr *mlx5_cq_attr);
</code></pre></dd></dl>

<h2>DESCRIPTION</h2>

 

 mlx5dv_create_cq() creates a completion queue (CQ) with specific driver properties.

<h2>ARGUMENTS</h2>

 

 Please see ibv_create_cq_ex(3) man page for context and cq_attr

<h3>mlx5_cq_attr</h3>

<dl>
<dt>
</dt><dd> <pre><code>
struct mlx5dv_cq_init_attr {
    uint64_t comp_mask;
    uint8_t cqe_comp_res_format;
    uint32_t flags;
    uint16_t cqe_size;
};
</code></pre>
</dd><dt>comp_mask
</dt><dd> Bitmask specifying what fields in the structure are valid:
</dd><dl>
<dt>
</dt><dd> 
 MLX5DV_CQ_INIT_ATTR_MASK_COMPRESSED_CQE enables creating a CQ in a mode that few CQEs may be compressed into a single CQE, valid values in cqe_comp_res_format 
 MLX5DV_CQ_INIT_ATTR_MASK_FLAGS valid values in flags 
 MLX5DV_CQ_INIT_ATTR_MASK_CQE_SIZE valid values in cqe_size</dd></dl>

<dt>cqe_comp_res_format
</dt><dd> A bitwise OR of the various CQE response formats of the responder side:
</dd><dl>
<dt>
</dt><dd> 
 MLX5DV_CQE_RES_FORMAT_HASH CQE compression with hash 
 MLX5DV_CQE_RES_FORMAT_CSUM CQE compression with RX checksum 
 MLX5DV_CQE_RES_FORMAT_CSUM_STRIDX CQE compression with stride index</dd></dl>

<dt>flags
</dt><dd> A bitwise OR of the various values described below:
</dd><dl>
<dt>
</dt><dd> 
 MLX5DV_CQ_INIT_ATTR_FLAGS_CQE_PAD create a padded 128B CQE</dd></dl>

<dt>cqe_size
</dt><dd> configure the CQE size to be 64 or 128 bytes other values will fail mlx5dv_create_cq.</dd></dl>

<h2>RETURN VALUE</h2>

 

 mlx5dv_create_cq() returns a pointer to the created CQ, or NULL if the request fails and errno will be set.

<h2>SEE ALSO</h2>

 

 ibv_create_cq_ex(3),

<h2>AUTHOR</h2>

 

 Yonatan Cohen &lt;yonatanc [at] mellanox.com&gt;
