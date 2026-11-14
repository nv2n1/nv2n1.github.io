---
title: "vdpa-mgmtdev(8)"
name: "vdpa-mgmtdev"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vdpa-mgmtdev/"
description: "vdpa-dev – vdpa management device view"
---

<p>vdpa-dev &#8211; vdpa management device view</p>
<h2>Synopsis</h2>
<pre><code>vdpa

mgmtdev

{ COMMAND|

    help }

OPTIONS := {

    -V[ersion]
}</code></pre>
<p> <code>vdpa mgmtdev show</code> [ <i>MGMTDEV</i> ]<br />
 <code>vdpa mgmtdev help</code> </p>
<h2>Description</h2>
<h3>vdpa mgmtdev show &#8211; display vdpa management device attributes</h3>
<p><i>MGMTDEV</i> &#8211; specifies the vdpa management device to show. If this argument is omitted all management devices are listed. </p>
<h2>Examples</h2>
<p>vdpa mgmtdev show</p>
<dl>
<dd>Shows all the vdpa management devices on the system.</dl>
<p> vdpa mgmtdev show bar</p>
<dl>
<dd>Shows the specified vdpa management device.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-vdpa/">vdpa</a></code>(8), <code><a href="/docs/linux/man/8-vdpa-dev/">vdpa-dev</a></code>(8), </p>
<h2>Author</h2>
<p>Parav Pandit &lt;parav [at] nvidia.com&gt;</p>
