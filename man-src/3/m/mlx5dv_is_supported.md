---
title: "mlx5dv_is_supported(3)"
name: "mlx5dv_is_supported"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_is_supported/"
---

mlx5dv_is_supported - Check whether an RDMA device implemented by the mlx5 provider 

<h2>Synopsis</h2><dl COMPACT><dd><pre>#include &lt;infiniband/mlx5dv.h&gt;
bool mlx5dv_is_supported(struct ibv_device *device);</pre></dl><h2>Description</h2>mlx5dv functions may be called only if this function returns true for the RDMA device.
<h2>Arguments</h2><dl COMPACT><dt>device
<dd>RDMA device to check.</dl><h2>Return Value</h2>Returns true if device is implemented by mlx5 provider.
<h2>See Also</h2><a HREF="/docs/linux/man/7-mlx5dv/">mlx5dv</a>(7)
<h2>Author</h2>Artemy Kovalyov &lt;artemyko [at] mellanox.com&gt;
