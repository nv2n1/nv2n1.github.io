---
title: "rdma-link(8)"
name: "rdma-link"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdma-link/"
description: "rdma-link – rdma link configuration"
---

<p>rdma-link &#8211; rdma link configuration</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

link

{ COMMAND |

    help }

OPTIONS := {

    -V[ersion] |
    -d[etails] }</code></pre>
<p> <code>rdma link show</code> [ <i>DEV/PORT_INDEX</i> ]<br />
 <code>rdma link add</code> <code>NAME</code> <code>type</code> <code>TYPE</code> <code>netdev</code> <code>NETDEV</code><br />
 <code>rdma link delete</code> NAME<br />
 <code>rdma link help</code> </p>
<h2>Description</h2>
<h3>rdma link show &#8211; display rdma link attributes</h3>
<p><i>DEV/PORT_INDEX</i> &#8211; specifies the RDMA link to show. If this argument is omitted all links are listed.</p>
<h3>rdma link add NAME type TYPE netdev NETDEV &#8211; add an rdma link for the specified type to the network device</h3>
<p><code>NAME</code> &#8211; specifies the new name of the rdma link to add <code>TYPE</code> &#8211; specifies which rdma type to use. Link types: <code>rxe</code> &#8211; Soft RoCE driver <code>siw</code> &#8211; Soft iWARP driver <code>NETDEV</code> &#8211; specifies the network device to which the link is bound</p>
<h3>rdma link delete NAME &#8211; delete an rdma link</h3>
<p><code>NAME</code> &#8211; specifies the name of the rdma link to delete </p>
<h2>Examples</h2>
<p>rdma link show</p>
<dl>
<dd>Shows the state of all rdma links on the system.</dl>
<p> rdma link show mlx5_2/1</p>
<dl>
<dd>Shows the state of specified rdma link.</dl>
<p> rdma link add rxe_eth0 type rxe netdev eth0</p>
<dl>
<dd>Adds a RXE link named rxe_eth0 to network device eth0</dl>
<p> rdma link del rxe_eth0</p>
<dl>
<dd>Removes RXE link rxe_eth0</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rdma/">rdma</a></code>(8), <code><a href="/docs/linux/man/8-rdma-dev/">rdma-dev</a></code>(8), <code><a href="/docs/linux/man/8-rdma-resource/">rdma-resource</a></code>(8), <code><a href="/docs/linux/man/8-rdma-statistic/">rdma-statistic</a></code>(8), </p>
<h2>Author</h2>
<p>Leon Romanovsky &lt;leonro [at] mellanox.com&gt;</p>
