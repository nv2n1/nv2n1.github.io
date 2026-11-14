---
title: "mlx5dv(7)"
name: "mlx5dv"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mlx5dv/"
description: "mlx5dv – Direct verbs for mlx5 devices This is low level access to mlx5 devices to perform data path operations, without general branching performed by"
---

<p>mlx5dv &#8211; Direct verbs for mlx5 devices<br />
 This is low level access to mlx5 devices to perform data path operations, without general branching performed by <code></p>
<p> <a href="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a></code>(3). </p>
<h2>Description</h2>
<p>The libibverbs API is an abstract one. It is agnostic to any underlying provider specific implementation. While this abstraction has the advantage of user applications portability it has a performance penalty. For some applications optimizing performance is more important than portability. The mlx5 direct verbs API is intended for such applications. It exposes mlx5 specific low level data path (send/receive/completion) operations, allowing the application to bypass the libibverbs data path API. This interface consists from one hardware specific header file with relevant inline functions and conversion logic from ibverbs structures to mlx5 specific structures. The direct include of mlx5dv.h together with linkage to mlx5 library will allow usage of this new interface. Once an application uses the direct flow the locking scheme is fully managed by itself. There is an expectation that no mixed flows in the data path for both direct/non-direct access will be by same application. </p>
<h2>Notes</h2>
<p>All Mellanox NIC devices starting from Connect-IB (Connect-IB, ConnectX-4, ConnectX-4Lx, ConnectX-5, &#8230;) implement the mlx5 API, thus using the mlx5 direct verbs does not limit the applications to a single NIC HW device thus keeping some level of portability. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a></code>(3), <code><a href="/docs/linux/man/7-verbs/">verbs</a></code>(7), <code><a href="/docs/linux/man/3-mlx5dv_is_supported/">mlx5dv_is_supported</a>(3)</code> </p>
<h2>Authors</h2>
<dl>
<dt>Leon Romanovsky &lt;leonro [at] mellanox.com&gt;</p>
<dd></dl>
