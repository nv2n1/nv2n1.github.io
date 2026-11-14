---
title: "mlx5dv_devx_free_uar(3)"
name: "mlx5dv_devx_free_uar"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_devx_free_uar/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_devx_alloc_uar - Allocates a DEVX UAR 

 mlx5dv_devx_free_uar - Frees a DEVX UAR 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct mlx5dv_devx_uar *mlx5dv_devx_alloc_uar(struct ibv_context *context,
                                              uint32_t flags);
void mlx5dv_devx_free_uar(struct mlx5dv_devx_uar *devx_uar);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Create / free a DEVX UAR which is needed for other device commands over the DEVX interface. 

 The DEVX API enables direct access from the user space area to the mlx5 device driver, the UAR information is needed for few commands as of QP creation.

<h2>ARGUMENTS</h2>

<dl>
<dt>context
<dd> RDMA device context to work on.
<dt>flags
<dd> Allocation flags for the UAR.</dl>

<h3>devx_uar</h3>

<dl>
<dt>
<dd> <pre><code>
struct mlx5dv_devx_uar {
    void *reg_addr;
    void *base_addr;
    uint32_t page_id;
    off_t mmap_off;
    uint64_t comp_mask;
};
</code></pre>
<dt>reg_addr
<dd> The write address of DB/BF.
<dt>base_addr
<dd> The base address of the UAR.
<dt>page_id
<dd> The device page id to be used.
<dt>mmap_off
<dd> The mmap offset parameter to be used for re-mapping, to be used by a secondary process.</dl>

<h2>RETURN VALUE</h2>

 

 Upon success mlx5dv_devx_alloc_uar will return a new struct mlx5dv_devx_uar, on error NULL will be returned and errno will be set.

<h2>SEE ALSO</h2>

 

 mlx5dv_open_device, mlx5dv_devx_obj_create 

 #AUTHOR 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


