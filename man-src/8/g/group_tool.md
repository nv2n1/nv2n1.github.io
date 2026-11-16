---
title: "group_tool(8)"
name: "group_tool"
section: "8"
letter: "g"
url: "/docs/linux/man/8-group_tool/"
description: "group_tool – run common fence_tool, dlm_tool, gfs_control commands"
---

<p>group_tool &#8211; run common fence_tool, dlm_tool, gfs_control commands</p>
<h2>Synopsis</h2>
<p><code>group_tool</code> [COMMAND] [OPTIONS] </p>
<h2>Description</h2>
<p>This utility is deprecated and the new replacements are shown. See <code><a href="/docs/linux/man/8-fence_tool/">fence_tool</a></code>(8), <code><a href="/docs/linux/man/8-dlm_tool/">dlm_tool</a></code>(8), <code><a href="/docs/linux/man/8-gfs_control/">gfs_control</a></code>(8) man pages for more information about the new commands.</p>
<dl>
<dt><code>ls</code></dt>
<dd>runs <code>fence_tool ls </code>; <code>dlm_tool ls </code>; <code>gfs_control ls</code></dd>
<dt><code>dump fence</code></dt>
<dd>equivalent to new <code>fence_tool dump</code></dd>
<dt><code>dump dlm</code></dt>
<dd>equivalent to new <code>dlm_tool dump</code></dd>
<dt><code>dump gfs</code></dt>
<dd>equivalent to new <code>gfs_control dump</code></dd>
<dt><code>dump plocks</code><i> name</i></dt>
<dd>equivalent to new <code>dlm_tool plocks</code><i> name</i></dd></dl>
<h3>Cluster Uprading</h3>
<p>When performing a rolling upgrade from cluster2 to cluster3, the <code><a href="/docs/linux/man/8-groupd/">groupd</a></code>(8) daemon will be running and group_tool can be used with groupd like it was in cluster2.</p>
<dl>
<dt><code>ls -g1</code></dt>
<dd>queries and displays the internal groupd state.</dd>
<dt><code>dump</code></dt>
<dd>queries and dumps the groupd debug buffer.</dd>
<dt><code>compat</code></dt>
<dd>queries and displays the internal groupd compatibility mode. </dd>
<h2>Options</h2>
<dl>
<dt><code>-g</code><i> num</i></dt>
<dd>Force old groupd queries with 1.</dd>
<dt><code>-n</code></dt>
<dd>Show all node information in ls.</dd>
<dt><code>-v</code></dt>
<dd>Show verbose information from groupd with ls -g1.</dd>
<dt><code>-h</code></dt>
<dd>Print a help message describing available options, then exit.</dd>
<dt><code>-V</code></dt>
<dd>Print program version information, then exit. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-cman/">cman</a></code>(5), <code><a href="/docs/linux/man/8-groupd/">groupd</a></code>(8), <code><a href="/docs/linux/man/8-fence_tool/">fence_tool</a></code>(8), <code><a href="/docs/linux/man/8-dlm_tool/">dlm_tool</a></code>(8), <code><a href="/docs/linux/man/8-gfs_control/">gfs_control</a>(8)</code> </p>
</dl>