---
title: "mlx5dv_get_clock_info(3)"
name: "mlx5dv_get_clock_info"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_get_clock_info/"
description: "mlx5dv_get_clock_info – Get device clock information"
---

<p>mlx5dv_get_clock_info &#8211; Get device clock information </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/mlx5dv.h&gt;</code>
<code>int mlx5dv_get_clock_info(struct ibv_context *ctx_in,</code>
<code> struct mlx5dv_clock_info *clock_info);</code></pre>
<h2>Description</h2>
<p>Get the updated core <i>clock_info</i> from the device driver. This information will be used later to translate the completion timestamp from HCA core clock to nanoseconds. The values of the clock are updated from the driver&#8217;s PTP clock, therefore, without a running PTP client on the machine, the wall clock conversion will not be accurate. </p>
<p> Pass the latest <code>struct mlx5dv_clock_info</code> to <code><a href="/docs/linux/man/3-mlx5dv_ts_to_ns/">mlx5dv_ts_to_ns</a>(3)</code> in order to translate the completion timestamp from HCA core clock to nanoseconds. </p>
<p> If the clock_info becomes too old then time conversion will return wrong conversion results. The user must ensure that <code><a href="/docs/linux/man/3-mlx5dv_get_clock_info/">mlx5dv_get_clock_info</a>(3)</code> is called at least once every <code>max_clock_info_update_nsec</code> as returned by the <code><a href="/docs/linux/man/3-mlx5dv_query_device/">mlx5dv_query_device</a>(3)</code> function. </p>
<h2>Return Value</h2>
<p>0 on success or the value of errno on failure (which indicates the failure reason).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-mlx5dv/">mlx5dv</a></code>(7), <code><a href="/docs/linux/man/3-mlx5dv_ts_to_ns/">mlx5dv_ts_to_ns</a></code>(3)</p>
<h2>Authors</h2>
<dl COMPACT>
<dt>Feras Daoud &lt;ferasda [at] mellanox.com&gt;</p>
<dd></dl>
