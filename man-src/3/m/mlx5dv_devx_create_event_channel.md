---
title: "mlx5dv_devx_create_event_channel(3)"
name: "mlx5dv_devx_create_event_channel"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_devx_create_event_channel/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_devx_create_event_channel - Create an event channel to be used for DEVX asynchronous events. 

 mlx5dv_devx_destroy_event_channel - Destroy a DEVX event channel. 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct mlx5dv_devx_event_channel {
    int fd;
};
struct mlx5dv_devx_event_channel *
mlx5dv_devx_create_event_channel(struct ibv_context *context,
                                 enum mlx5dv_devx_create_event_channel_flags flags) void mlx5dv_devx_destroy_event_channel(struct mlx5dv_devx_event_channel *event_channel)
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Create or destroy a channel to be used for DEVX asynchronous events. 

 The create verb exposes an mlx5dv_devx_event_channel object that can be used to read asynchronous DEVX events. This lets an application to subscribe to get device events and once an event occurred read it from this object.

<h2>ARGUMENTS</h2>

<dl>
<dt>context
<dd>
<dt>
<dd> <pre>
RDMA device context to create the channel on.
</pre>
<dt>flags
<dd> MLX5DV_DEVX_CREATE_EVENT_CHANNEL_FLAGS_OMIT_EV_DATA: omit the event data on this channel.</dl>

<h2>RETURN VALUE</h2>

 

 Upon success mlx5dv_devx_create_event_channel will return a new struct mlx5dv_devx_event_channel object, on error NULL will be returned and errno will be set.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-mlx5dv_open_device/">mlx5dv_open_device</a>(3), <a HREF="/docs/linux/man/3-mlx5dv_devx_obj_create/">mlx5dv_devx_obj_create</a>(3) 

 #AUTHOR 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


