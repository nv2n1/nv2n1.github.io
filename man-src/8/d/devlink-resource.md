---
title: "devlink-resource(8)"
name: "devlink-resource"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-resource/"
description: "devlink-resource – devlink device resource configuration"
---

<p>devlink-resource &#8211; devlink device resource configuration</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

resource

{ COMMAND |

    help }

OPTIONS := {

    -v[erbose] }</code></pre>
<p> <code>devlink resource show</code> <i>DEV</i><br />
 <code>devlink resource help</code><br />
 <code>devlink resource set</code> <i>DEV</i> <code>path</code><i> RESOURCE_PATH</i> <code>size</code><i> RESOURCE_SIZE</i> </p>
<h2>Description</h2>
<h3>devlink resource show &#8211; display devlink device&#8217;s resosources</h3>
<p><i>DEV</i> &#8211; specifies the devlink device to show. Format is: BUS_NAME/BUS_ADDRESS</p>
<h3>devlink resource set &#8211; sets resource size of specific resource</h3>
<p><i>DEV</i> &#8211; specifies the devlink device.</p>
<dl>
<dt><code>path</code><i> RESOURCE_PATH</i></p>
<dd>Resource&#8217;s path.</p>
<dt><code>size</code><i> RESOURCE_SIZE</i></p>
<dd>The new resource&#8217;s size. </p>
<h2>Examples</h2>
<p>devlink resource show pci/0000:01:00.0</p>
<dl>
<dd>Shows the resources of the specified devlink device.</dl>
<p> devlink resource set pci/0000:01:00.0 /kvd/linear 98304</p>
<dl>
<dd>Sets the size of the specified resource for the specified devlink device.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-port/">devlink-port</a></code>(8), <code><a href="/docs/linux/man/8-devlink-sb/">devlink-sb</a></code>(8), <code><a href="/docs/linux/man/8-devlink-monitor/">devlink-monitor</a></code>(8), </p>
<h2>Author</h2>
<p>Arkadi Sharshevsky &lt;arkadis [at] mellanox.com&gt;</p>
