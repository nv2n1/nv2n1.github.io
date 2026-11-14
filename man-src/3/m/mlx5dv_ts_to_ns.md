---
title: "mlx5dv_ts_to_ns(3)"
name: "mlx5dv_ts_to_ns"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_ts_to_ns/"
description: "mlx5dv_ts_to_ns – Convert device timestamp from HCA core clock units to the corresponding nanosecond counts"
---

<p>mlx5dv_ts_to_ns &#8211; Convert device timestamp from HCA core clock units to the corresponding nanosecond counts </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/mlx5dv.h&gt;</code>
<code>uint64_t mlx5dv_ts_to_ns(struct mlx5dv_clock_info *clock_info,</code>
<code> uint64_t device_timestamp);</code></pre>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-mlx5dv_ts_to_ns/">mlx5dv_ts_to_ns</a>(3)</code> Converts a host byte order<br />
 <i>device_timestamp</i> from HCA core clock units into the corresponding nanosecond wallclock time. </p>
<p> <code>struct mlx5dv_clock_info</code> can be retrieved using <code><a href="/docs/linux/man/3-mlx5dv_get_clock_info/">mlx5dv_get_clock_info</a>(3)</code>. </p>
<p> The greater the difference between the device reporting a timestamp and the last mlx5dv_clock_info update, the greater the inaccuracy of the clock time conversion. </p>
<h2>Return Value</h2>
<p>Timestamp in nanoseconds</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-mlx5dv/">mlx5dv</a></code>(7), <code><a href="/docs/linux/man/3-mlx5dv_get_clock_info/">mlx5dv_get_clock_info</a></code>(3), <code><a href="/docs/linux/man/3-mlx5dv_query_device/">mlx5dv_query_device</a></code>(3)</p>
<h2>Authors</h2>
<dl COMPACT>
<dt>Feras Daoud &lt;ferasda [at] mellanox.com&gt;</p>
<dd></dl>
