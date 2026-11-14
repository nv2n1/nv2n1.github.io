---
title: "mlx5dv_alloc_dm(3)"
name: "mlx5dv_alloc_dm"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_alloc_dm/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_alloc_dm - allocates device memory (DM) 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct ibv_dm *mlx5dv_alloc_dm(struct ibv_context *context,
                               struct ibv_alloc_dm_attr *dm_attr,
                               struct mlx5dv_alloc_dm_attr *mlx5_dm_attr)
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 mlx5dv_alloc_dm() allocates device memory (DM) with specific driver properties.

<h2>ARGUMENTS</h2>

 

 Please see <a HREF="/docs/linux/man/3-ibv_alloc_dm/">ibv_alloc_dm</a>(3) man page for context and dm_attr.

<h3>mlx5_dm_attr</h3>

<dl>
<dt>
<dd> <pre><code>
struct mlx5dv_alloc_dm_attr {
    enum mlx5dv_alloc_dm_type type;
    uint64_t comp_mask;
};
</code></pre>
<dt>type
<dd> The device memory type user wishes to allocate:
<dl>
<dt>
<dd> 

 MLX5DV_DM_TYPE_MEMIC Device memory of type MEMIC - On-Chip memory that can be allocated and used as memory region for transmitting/receiving packet directly from/to the memory on the chip. 

 MLX5DV_DM_TYPE_STEERING_SW_ICM Device memory of type STEERING SW ICM - This memory is used by the device to store the packet steering tables and rules. Can be used for direct table and steering rules creation when allocated by a privileged user. 

 MLX5DV_DM_TYPE_HEADER_MODIFY_SW_ICM Device memory of type HEADER MODIFY SW ICM - This memory is used by the device to store the packet header modification tables and rules. Can be used for direct table and header modification rules creation when allocated by a privileged user.</dl>

<dt>comp_mask
<dd> Bitmask specifying what fields in the structure are valid: Currently reserved and should be set to 0.</dl>

<h2>RETURN VALUE</h2>

 

 mlx5dv_alloc_dm() returns a pointer to the created DM, on error NULL will be returned and errno will be set.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-ibv_alloc_dm/">ibv_alloc_dm</a>(3),

<h2>AUTHOR</h2>

 

 Ariel Levkovich &lt;lariel [at] mellanox.com&gt; 

<h2>Index</h2>


