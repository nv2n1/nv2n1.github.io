---
title: "mlx5dv_devx_umem_dereg(3)"
name: "mlx5dv_devx_umem_dereg"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_devx_umem_dereg/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_devx_umem_reg - Register a user memory to be used by the devx interface 

 mlx5dv_devx_umem_dereg - Deregister a devx umem object 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct mlx5dv_devx_umem {
    uint32_t umem_id;
};
struct mlx5dv_devx_umem *
mlx5dv_devx_umem_reg(struct ibv_context *context, void *addr, size_t size,
                     uint32_t access) int mlx5dv_devx_umem_dereg(struct mlx5dv_devx_umem *dv_devx_umem)
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Register or deregister a user memory to be used by the devx interface. 

 The register verb exposes a UMEM DEVX object for user memory registration for DMA. The API to register the user memory gets as input the user address, length and access flags, and provides to the user as output an object which holds the UMEM ID returned by the firmware to this registered memory. 

 The user will use that UMEM ID in device direct commands that use this memory instead of the physical addresses list, for example upon mlx5dv_devx_obj_create to create a QP.

<h2>ARGUMENTS</h2>

<dl>
<dt>context
<dd>
<dt>
<dd> <pre>
RDMA device context to create the action on.
</pre>
<dt>addr
<dd> The memory start address to register.
<dt>size
<dd>
<dt>
<dd> <pre>
The size of *addr* buffer.
</pre>
<dt>access
<dd> The desired memory protection attributes; it is either 0 or the bitwise OR of one or more of enum ibv_access_flags.</dl>

<h2>RETURN VALUE</h2>

 

 Upon success mlx5dv_devx_umem_reg will return a new struct mlx5dv_devx_umem object, on error NULL will be returned and errno will be set. 

 mlx5dv_devx_umem_dereg returns 0 on success, or the value of errno on failure (which indicates the failure reason).

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-mlx5dv_open_device/">mlx5dv_open_device</a>(3), <a HREF="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a>(3), <a HREF="/docs/linux/man/3-mlx5dv_devx_obj_create/">mlx5dv_devx_obj_create</a>(3) 

 #AUTHOR 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


