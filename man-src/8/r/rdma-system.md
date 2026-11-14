---
title: "rdma-system(8)"
name: "rdma-system"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdma-system/"
description: "rdma-system – RDMA subsystem configuration"
---

<p>rdma-system &#8211; RDMA subsystem configuration</p>
<h2>Synopsis</h2>
<pre><code>rdma

[ OPTIONS ]

sys

{ COMMAND |

    help }

OPTIONS := {

    -V[ersion] |
    -d[etails] }</code></pre>
<p> <code>rdma system show</code><br />
 <code>rdma system set</code> <code>netns</code> <code>NEWMODE</code><br />
 <code>rdma system help</code> </p>
<h2>Description</h2>
<h3>rdma system set &#8211; set RDMA subsystem network namespace mode</h3>
<h3>rdma system show &#8211; display RDMA subsystem network namespace mode</h3>
<p><i>NEWMODE</i> &#8211; specifies the RDMA subsystem mode. Either exclusive or shared. When user wants to assign dedicated RDMA device to a particular network namespace, exclusive mode should be set before creating any network namespace. If there are active network namespaces and if one or more RDMA devices exist, changing mode from shared to exclusive returns error code EBUSY. When RDMA subsystem is in shared mode, RDMA device is accessible in all network namespace. When RDMA device isolation among multiple network namespaces is not needed, shared mode can be used. It is preferred to not change the subsystem mode when there is active RDMA traffic running, even though it is supported. </p>
<h2>Examples</h2>
<p>rdma system show</p>
<dl>
<dd>Shows the state of RDMA subsystem network namespace mode on the system.</dl>
<p> rdma system set netns exclusive</p>
<dl>
<dd>Sets the RDMA subsystem in network namespace exclusive mode. In this mode RDMA devices are visible only in single network namespace.</dl>
<p> rdma system set netns shared</p>
<dl>
<dd>Sets the RDMA subsystem in network namespace shared mode. In this mode RDMA devices are shared among network namespaces.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-rdma/">rdma</a></code>(8), <code><a href="/docs/linux/man/8-rdma-link/">rdma-link</a></code>(8), <code><a href="/docs/linux/man/8-rdma-resource/">rdma-resource</a></code>(8), <code><a href="/docs/linux/man/7-network_namespaces/">network_namespaces</a></code>(7), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7), </p>
<h2>Author</h2>
<p>Parav Pandit &lt;parav [at] mellanox.com&gt;</p>
