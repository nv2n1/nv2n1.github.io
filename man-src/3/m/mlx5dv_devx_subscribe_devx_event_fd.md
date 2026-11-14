---
title: "mlx5dv_devx_subscribe_devx_event_fd(3)"
name: "mlx5dv_devx_subscribe_devx_event_fd"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_devx_subscribe_devx_event_fd/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_devx_subscribe_devx_event - Subscribe over an event channel for device events. 

 mlx5dv_devx_subscribe_devx_event_fd - Subscribe over an event channel for device events to signal eventfd. 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
int mlx5dv_devx_subscribe_devx_event(struct mlx5dv_devx_event_channel *dv_event_channel,
                                     struct mlx5dv_devx_obj *obj,
                                     uint16_t events_sz,
                                     uint16_t events_num[],
                                     uint64_t cookie) int mlx5dv_devx_subscribe_devx_event_fd(struct mlx5dv_devx_event_channel *dv_event_channel,
                                                                                              int fd,
                                                                                              struct mlx5dv_devx_obj *obj,
                                                                                              uint16_t event_num)
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Subscribe over a DEVX event channel for device events.

<h2>ARGUMENTS</h2>

<dl>
<dt>dv_event_channel
<dd> Event channel to subscribe over.
<dt>fd
<dd> A file descriptor that previously was opened by the eventfd() system call.
<dt>obj
<dd> DEVX object that events_num relates to, can be NULL for unaffiliated events.
<dt>events_sz
<dd> Size of the events_num buffer that holds the events to subscribe for.
<dt>events_num
<dd> Holds the required event numbers to subscribe for, numbers are according to the device specification.
<dt>cookie
<dd> The value to be returned back when reading the event, can be used as an ID for application use.</dl>

<h2>NOTES</h2>

 

 When mlx5dv_devx_subscribe_devx_event_fd will be used the fd will be signaled once an event has occurred.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-mlx5dv_open_device/">mlx5dv_open_device</a>(3), <a HREF="/docs/linux/man/3-mlx5dv_devx_create_event_channel/">mlx5dv_devx_create_event_channel</a>(3), <a HREF="/docs/linux/man/3-mlx5dv_devx_get_event/">mlx5dv_devx_get_event</a>(3) 

 #AUTHOR 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


