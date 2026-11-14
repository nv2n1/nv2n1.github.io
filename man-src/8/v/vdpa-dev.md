---
title: "vdpa-dev(8)"
name: "vdpa-dev"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vdpa-dev/"
description: "vdpa-dev – vdpa device configuration"
---

<p>vdpa-dev &#8211; vdpa device configuration</p>
<h2>Synopsis</h2>
<pre><code>vdpa

dev

[ OPTIONS ]

{ COMMAND|

    help }

OPTIONS := {

    -V[ersion]
}</code></pre>
<p> <code>vdpa dev show</code> [ <i>DEV</i> ]<br />
 <code>vdpa dev help</code><br />
 <code>vdpa dev add</code> <code>name</code> <i>NAME</i> <code>mgmtdev</code> <i>MGMTDEV</i><br />
 <code>vdpa dev del</code> <i>DEV</i> </p>
<h2>Description</h2>
<h3>vdpa dev show &#8211; display vdpa device attributes</h3>
<p><i>DEV</i> &#8211; specifies the vdpa device to show. If this argument is omitted all devices are listed. Format is: VDPA_DEVICE_NAME</p>
<h3>vdpa dev add &#8211; add a new vdpa device.</h3>
<dl>
<dt><code>name</code><i> NAME</i></p>
<dd>Name of the new vdpa device to add.</p>
<dt><code>mgmtdev</code><i> MGMTDEV</i></p>
<dd>Name of the management device to use for device addition.</dl>
<h3>vdpa dev del &#8211; Delete the vdpa device.</h3>
<p><i>DEV</i> &#8211; specifies the vdpa device to delete. </p>
<h2>Examples</h2>
<p>vdpa dev show</p>
<dl>
<dd>Shows the all vdpa devices on the system.</dl>
<p> vdpa dev show foo</p>
<dl>
<dd>Shows the specified vdpa device.</dl>
<p> vdpa dev add name foo mgmtdev vdpa_sim_net</p>
<dl>
<dd>Add the vdpa device named foo on the management device vdpa_sim_net.</dl>
<p> vdpa dev del foo</p>
<dl>
<dd>Delete the vdpa device named foo which was previously created.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-vdpa/">vdpa</a></code>(8), <code><a href="/docs/linux/man/8-vdpa-mgmtdev/">vdpa-mgmtdev</a></code>(8), </p>
<h2>Author</h2>
<p>Parav Pandit &lt;parav [at] nvidia.com&gt;</p>
