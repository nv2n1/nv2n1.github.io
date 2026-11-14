---
title: "dev_change_xdp_fd(9)"
name: "dev_change_xdp_fd"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_change_xdp_fd/"
---

dev_change_xdp_fd - set or clear a bpf program for a device rx path

<h2>Synopsis</h2>

<pre><code>int dev_change_xdp_fd(struct net_device *dev, int fd);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>device</dl>
 

 <i>fd</i>
<dl><dd>new program fd or negative value to clear</dl>

<h2>Description</h2>

Set or clear a bpf program for a device

<h2>Copyright</h2>


