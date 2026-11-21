---

title: "mlx4dv_set_context_attr(3)"
name: "mlx4dv_set_context_attr"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx4dv_set_context_attr/"
---

mlx4dv_set_context_attr - Set context attributes 

<dl>
<dt>
</dt><dd> <pre><code>
#include &lt;infiniband/mlx4dv.h&gt;
int mlx4dv_set_context_attr(struct ibv_context *context,
                            enum mlx4dv_set_ctx_attr_type attr_type,
                            void *attr);
</code></pre></dd></dl>

mlx4dv_set_context_attr gives the ability to set vendor specific attributes on the RDMA context.

<h2>ARGUMENTS</h2>

<dl>
<dt>context
</dt><dd> RDMA device context to work on.
</dd><dt>attr_type
</dt><dd> The type of the provided attribute.
</dd><dt>attr
</dt><dd> Pointer to the attribute to be set. ## attr_type
</dd><dt>
</dt><dd> 
enum mlx4dv_set_ctx_attr_type {
    /* Attribute type uint8_t */
    MLX4DV_SET_CTX_ATTR_LOG_WQS_RANGE_SZ = 0,
    MLX4DV_SET_CTX_ATTR_BUF_ALLOCATORS = 1,
};
</dd><dt>MLX4DV_SET_CTX_ATTR_LOG_WQS_RANGE_SZ
</dt><dd> Change the LOG WQs Range size for RSS
</dd><dt>MLX4DV_SET_CTX_ATTR_BUF_ALLOCATORS
</dt><dd> Provide an external buffer allocator
</dd><dt>
</dt><dd> <pre><code>
struct mlx4dv_ctx_allocators {
    void *(*alloc)(size_t size, void *priv_data);
    void (*free)(void *ptr, void *priv_data);
    void *data;
};
</code></pre>
</dd><dt>alloc
</dt><dd> Function used for buffer allocation instead of libmlx4 internal method
</dd><dt>free
</dt><dd> Function used to free buffers allocated by alloc function
</dd><dt>data
</dt><dd> Metadata that can be used by alloc and free functions</dd></dl>

<h2>RETURN VALUE</h2>

 

 Returns 0 on success, or the value of errno on failure (which indicates the failure reason). 

 #AUTHOR 

 Majd Dibbiny &lt;majd [at] mellanox.com&gt;
