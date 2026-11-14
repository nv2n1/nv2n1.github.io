---
title: "rdma-dev(8)"
name: "rdma-dev"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdma-dev/"
description: "rdma-dev – RDMA device configuration"
---

<p>rdma-dev &#8211; RDMA device configuration</p>
<h2>Synopsis</h2>
<pre><code>rdma

[ OPTIONS ]

dev

{ COMMAND |

    help }

OPTIONS := {

    -V[ersion] |
    -d[etails] }</code></pre>
<p> <code>rdma dev show</code> [ <i>DEV</i> ]<br />
 <code>rdma dev set</code> [ <i>DEV</i> ] <code>name</code> <code>NEWNAME</code><br />
 <code>rdma dev set</code> [ <i>DEV</i> ] <code>netns</code> <code>NSNAME</code><br />
 <code>rdma dev set</code> [ <i>DEV</i> ] <code>adaptive-moderation</code> <code>[on/off]</code><br />
 <code>rdma dev help</code> </p>
<h2>Description</h2>
<h3>rdma dev set &#8211; rename RDMA device or set network namespace or set RDMA device adaptive-moderation</h3>
<h3>rdma dev show &#8211; display RDMA device attributes</h3>
<p><i>DEV</i> &#8211; specifies the RDMA device to show. If this argument is omitted all devices are listed. </p>
<h2>Examples</h2>
<p>rdma dev</p>
<dl>
<dd>Shows the state of all RDMA devices on the system.</dl>
<p> rdma dev show mlx5_3</p>
<dl>
<dd>Shows the state of specified RDMA device.</dl>
<p> rdma dev set mlx5_3 name rdma_0</p>
<dl>
<dd>Renames the mlx5_3 device to rdma_0.</dl>
<p> rdma dev set mlx5_3 netns foo</p>
<dl>
<dd>Changes the network namespace of RDMA device to foo where foo is previously created using iproute2 ip command.</dl>
<p> rdma dev set mlx5_3 adaptive-moderation [on/off]</p>
<dl>
<dd>Sets the state of adaptive interrupt moderation for the RDMA device.</dl>
<dl>
<dd>This is a global setting for the RDMA device but the value is printed for each CQ individually because the state is constant from CQ allocation.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-rdma/">rdma</a></code>(8), <code><a href="/docs/linux/man/8-rdma-link/">rdma-link</a></code>(8), <code><a href="/docs/linux/man/8-rdma-resource/">rdma-resource</a></code>(8), <code><a href="/docs/linux/man/8-rdma-system/">rdma-system</a></code>(8), <code><a href="/docs/linux/man/8-rdma-statistic/">rdma-statistic</a></code>(8), </p>
<h2>Author</h2>
<p>Leon Romanovsky &lt;leonro [at] mellanox.com&gt;</p>
