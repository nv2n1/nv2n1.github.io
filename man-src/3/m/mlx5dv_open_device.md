---
title: "mlx5dv_open_device(3)"
name: "mlx5dv_open_device"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_open_device/"
---

mlx5dv_open_device - Open an RDMA device context for the mlx5 provider 

<h2>Synopsis</h2><dl COMPACT><dd><pre>#include &lt;infiniband/mlx5dv.h&gt;
struct ibv_context *
mlx5dv_open_device(struct ibv_device *device, struct mlx5dv_context_attr *attr);</pre></dl><h2>Description</h2>Open an RDMA device context with specific mlx5 provider attributes.
<h2>Arguments</h2><dl COMPACT><dt>device
<dd>RDMA device to open.</dl><h3>attr argument</h3><dl COMPACT><dd><pre>struct mlx5dv_context_attr {
 uint32_t flags;
 uint64_t comp_mask;
};</pre><dt>flags
<dd><dd><pre>A bitwise OR of the various values described below.
*MLX5DV_CONTEXT_FLAGS_DEVX*:
Allocate a DEVX context</pre><dt>comp_mask
<dd><dd><pre>Bitmask specifying what fields in the structure are valid</pre></dl><h2>Return Value</h2>Returns a pointer to the allocated device context, or NULL if the request fails.
<h2>See Also</h2><a HREF="/docs/linux/man/3-ibv_open_device/">ibv_open_device</a>(3)
<h2>Author</h2>Yishai Hadas &lt;yishaih [at] mellanox.com&gt;
