---
title: "devlink-dpipe(8)"
name: "devlink-dpipe"
section: "8"
letter: "d"
url: "/docs/linux/man/8-devlink-dpipe/"
description: "devlink-dpipe – devlink dataplane pipeline visualization"
---

<p>devlink-dpipe &#8211; devlink dataplane pipeline visualization</p>
<h2>Synopsis</h2>
<pre><code>devlink

[ OPTIONS ]

dpipe

{ table | header }

{ COMMAND |

    help }

OPTIONS := {

    -V[ersion] }</code></pre>
<p> <code>devlink dpipe table show </code><i>DEV</i> [ <code>name</code> <i>TABLE_NAME</i> ]<br />
 <code>devlink dpipe table set </code><i>DEV</i> <code>name</code><i> TABLE_NAME </i><br />
 <code>devlink dpipe table dump </code><i>DEV</i> <code>name</code><i> TABLE_NAME </i><br />
 <code>devlink dpipe header show </code><i>DEV</i><br />
 <code>devlink dpipe help</code> </p>
<h2>Description</h2>
<h3>devlink dpipe table show &#8211; display devlink dpipe table attributes</h3>
<dl>
<dt><code>name</code><i> TABLE_NAME</i></p>
<dd>Specifies the table to operate on.</dl>
<h3>devlink dpipe table set &#8211; set devlink dpipe table attributes</h3>
<dl>
<dt><code>name</code><i> TABLE_NAME</i></p>
<dd>Specifies the table to operate on.</dl>
<h3>devlink dpipe table dump &#8211; dump devlink dpipe table entries</h3>
<dl>
<dt><code>name</code><i> TABLE_NAME</i></p>
<dd>Specifies the table to operate on.</dl>
<h3>devlink dpipe header show &#8211; display devlink dpipe header attributes</h3>
<dl>
<dt><code>name</code><i> TABLE_NAME</i></p>
<dd>Specifies the table to operate on. </p>
<h2>Examples</h2>
<p>devlink dpipe table show pci/0000:01:00.0</p>
<dl>
<dd>Shows all dpipe tables on specified devlink device.</dl>
<p> devlink dpipe table show pci/0000:01:00.0 name mlxsw_erif</p>
<dl>
<dd>Shows mlxsw_erif dpipe table on specified devlink device.</dl>
<p> devlink dpipe table set pci/0000:01:00.0 name mlxsw_erif counters_enabled true</p>
<dl>
<dd>Turns on the counters on mlxsw_erif table.</dl>
<p> devlink dpipe table dump pci/0000:01:00.0 name mlxsw_erif</p>
<dl>
<dd>Dumps content of mlxsw_erif table.</dl>
<p> devlink dpipe header show pci/0000:01:00.0</p>
<dl>
<dd>Shows all dpipe headers on specified devlink device.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-devlink/">devlink</a></code>(8), <code><a href="/docs/linux/man/8-devlink-dev/">devlink-dev</a></code>(8), <code><a href="/docs/linux/man/8-devlink-monitor/">devlink-monitor</a></code>(8), </p>
<h2>Author</h2>
<p>Jiri Pirko &lt;jiri [at] mellanox.com&gt;</p>
