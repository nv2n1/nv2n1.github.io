---
title: "gfs_control(8)"
name: "gfs_control"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gfs_control/"
description: "gfs_control – a utility for the gfs_controld daemon"
---

<p>gfs_control &#8211; a utility for the gfs_controld daemon</p>
<h2>Synopsis</h2>
<p><code>gfs_control</code> [COMMAND] [OPTIONS] [ <i>name</i> ] </p>
<h2>Description</h2>
<dl>
<dt><code>ls</code></p>
<dd>Display internal gfs_controld state about mount groups.</p>
<dt><code>dump</code></p>
<dd>Dump gfs_controld debug buffer.</p>
<dt><code>plocks</code><i> name</i></p>
<dd>Dump posix locks from gfs_controld for the mount group. (For compat mode, otherwise see <code><a href="/docs/linux/man/8-dlm_tool/">dlm_tool</a></code>(8).) </p>
<h2>Options</h2>
<dl>
<dt><code>-n</code></p>
<dd>Show all node information in ls. </p>
<dt><code>-h</code></p>
<dd>Print a help message describing available options, then exit. </p>
<dt><code>-V</code></p>
<dd>Print program version information, then exit. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gfs_controld/">gfs_controld</a></code>(8), <code><a href="/docs/linux/man/8-dlm_tool/">dlm_tool</a></code>(8) </p>
