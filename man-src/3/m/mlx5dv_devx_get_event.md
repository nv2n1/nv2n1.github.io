---
title: "mlx5dv_devx_get_event(3)"
name: "mlx5dv_devx_get_event"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_devx_get_event/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_devx_get_event - Get an asynchronous event. 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct mlx5dv_devx_async_event_hdr {
    uint64_t cookie;
    uint8_t out_data[];
};
ssize_t mlx5dv_devx_get_event(struct mlx5dv_devx_event_channel *event_channel,
                              struct mlx5dv_devx_async_event_hdr *event_data,
                              size_t event_resp_len)
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Get a device event on the given event_channel. Post a successful subscription over the event channel by calling to mlx5dv_devx_subscribe_devx_event() the application should use this API to get the response once an event has occurred. 

 Upon response the cookie that was supplied upon the subscription is returned and the out_data includes the data itself. The out_data may be omitted in case the channel was created with the omit data flag. 

 The application must supply a large enough buffer to hold the event according to the device specification, the buffer size is given by the input event_resp_len parameter.

<h2>ARGUMENTS</h2>

<dl>
<dt>event_channel
<dd>
<dt>
<dd> <pre>
The channel to get the event over.
</pre>
<dt>event_data
<dd> The output data from the asynchronous event.
<dt>event_resp_len
<dd> The output buffer size to hold the response.</dl>

<h2>RETURN VALUE</h2>

 

 Upon success mlx5dv_devx_get_event will return the number of bytes read, otherwise -1 will be returned and errno was set.

<h2>NOTES</h2>

 

 In case the event_channel was created with the omit data flag, events having the same type may be combined per subscription and be reported once with the matching cookie. In that mode of work, ordering is not preserved between those events to other on this channel. 

 On the other hand, when each event should hold the device data ordering is preserved, however, events might be loose as of lack of kernel memory, in that case EOVERFLOW will be reported.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/3-mlx5dv_open_device/">mlx5dv_open_device</a>(3), <a HREF="/docs/linux/man/3-mlx5dv_devx_subscribe_devx_event/">mlx5dv_devx_subscribe_devx_event</a>(3) 

 #AUTHOR 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


