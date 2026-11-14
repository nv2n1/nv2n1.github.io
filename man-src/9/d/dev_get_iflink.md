---
title: "dev_get_iflink(9)"
name: "dev_get_iflink"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_get_iflink/"
---

dev_get_iflink - get 'iflink' value of a interface

<h2>Synopsis</h2>

<pre><code>int dev_get_iflink(const struct net_device *dev);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>targeted interface</dl>

<h2>Description</h2>

Indicates the ifindex the interface is linked to. Physical interfaces have the same 'ifindex' and 'iflink' values.

<h2>Copyright</h2>


