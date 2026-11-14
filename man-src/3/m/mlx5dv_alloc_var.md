---
title: "mlx5dv_alloc_var(3)"
name: "mlx5dv_alloc_var"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_alloc_var/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_alloc_var - Allocates a VAR 

 mlx5dv_free_var - Frees a VAR 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct mlx5dv_var *
mlx5dv_alloc_var(struct ibv_context *context, uint32_t flags);
void mlx5dv_free_var(struct mlx5dv_var *dv_var);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Create / free a VAR which can be used for some device commands over the DEVX interface. 

 The DEVX API enables direct access from the user space area to the mlx5 device driver, the VAR information is needed for few commands related to Virtio.

<h2>ARGUMENTS</h2>

<dl>
<dt>context
<dd> RDMA device context to work on.
<dt>flags
<dd> Allocation flags for the UAR.</dl>

<h3>dv_var</h3>

<dl>
<dt>
<dd> <pre><code>
struct mlx5dv_var {
    uint32_t page_id;
    uint32_t length;
    off_t mmap_off;
    uint64_t comp_mask;
};
</code></pre>
<dt>page_id
<dd> The device page id to be used.
<dt>length
<dd> The mmap length parameter to be used for mapping a VA to the allocated VAR entry.
<dt>mmap_off
<dd> The mmap offset parameter to be used for mapping a VA to the allocated VAR entry.</dl>

<h2>RETURN VALUE</h2>

 

 Upon success mlx5dv_alloc_var returns a pointer to the created VAR ,on error NULL will be returned and errno will be set.

<h2>SEE ALSO</h2>

 

 mlx5dv_open_device, mlx5dv_devx_obj_create

<h2>AUTHOR</h2>

 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


