---
title: "mlx5dv_devx_query_eqn(3)"
name: "mlx5dv_devx_query_eqn"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_devx_query_eqn/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_devx_query_eqn - Query EQN for a given vector id. 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
int mlx5dv_devx_query_eqn(struct ibv_context *context, uint32_t vector,
                          uint32_t *eqn);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Query EQN for a given input vector, the EQN is needed for other device commands over the DEVX interface. 

 The DEVX API enables direct access from the user space area to the mlx5 device driver, the EQN information is needed for few commands such as CQ creation.

<h2>ARGUMENTS</h2>

<dl>
<dt>context
<dd> RDMA device context to work on.
<dt>vector
<dd> Completion vector number.
<dt>eqn
<dd> The device EQ number which relates to the given input vector.</dl>

<h2>RETURN VALUE</h2>

 

 returns 0 on success, or the value of errno on failure (which indicates the failure reason).

<h2>SEE ALSO</h2>

 

 mlx5dv_open_device, mlx5dv_devx_obj_create 

 #AUTHOR 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


