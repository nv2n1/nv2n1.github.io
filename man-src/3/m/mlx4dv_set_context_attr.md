---
title: "mlx4dv_set_context_attr(3)"
name: "mlx4dv_set_context_attr"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx4dv_set_context_attr/"
---

<h2 class="name">NAME</h2>
 

 

 mlx4dv_set_context_attr - Set context attributes 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx4dv.h&gt;
int mlx4dv_set_context_attr(struct ibv_context *context,
                            enum mlx4dv_set_ctx_attr_type attr_type,
                            void *attr);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 mlx4dv_set_context_attr gives the ability to set vendor specific attributes on the RDMA context.

<h2>ARGUMENTS</h2>

<dl>
<dt>context
<dd> RDMA device context to work on.
<dt>attr_type
<dd> The type of the provided attribute.
<dt>attr
<dd> Pointer to the attribute to be set. ## attr_type
<dt>
<dd> 
enum mlx4dv_set_ctx_attr_type {
    /* Attribute type uint8_t */
    MLX4DV_SET_CTX_ATTR_LOG_WQS_RANGE_SZ = 0,
    MLX4DV_SET_CTX_ATTR_BUF_ALLOCATORS = 1,
};

<dt>MLX4DV_SET_CTX_ATTR_LOG_WQS_RANGE_SZ
<dd> Change the LOG WQs Range size for RSS
<dt>MLX4DV_SET_CTX_ATTR_BUF_ALLOCATORS
<dd> Provide an external buffer allocator
<dt>
<dd> <pre><code>
struct mlx4dv_ctx_allocators {
    void *(*alloc)(size_t size, void *priv_data);
    void (*free)(void *ptr, void *priv_data);
    void *data;
};
</code></pre>
<dt>alloc
<dd> Function used for buffer allocation instead of libmlx4 internal method
<dt>free
<dd> Function used to free buffers allocated by alloc function
<dt>data
<dd> Metadata that can be used by alloc and free functions</dl>

<h2>RETURN VALUE</h2>

 

 Returns 0 on success, or the value of errno on failure (which indicates the failure reason). 

 #AUTHOR 

 Majd Dibbiny &lt;majd [at] mellanox.com&gt; 

<h2>Index</h2>


