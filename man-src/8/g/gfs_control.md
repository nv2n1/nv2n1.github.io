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
<dt><code>ls</code></dt>
<dd>Display internal gfs_controld state about mount groups.</dd>
<dt><code>dump</code></dt>
<dd>Dump gfs_controld debug buffer.</dd>
<dt><code>plocks</code><i> name</i></dt>
<dd>Dump posix locks from gfs_controld for the mount group. (For compat mode, otherwise see <code><a href="/docs/linux/man/8-dlm_tool/">dlm_tool</a></code>(8).) </dd>
<h2>Options</h2>
<dl>
<dt><code>-n</code></dt>
<dd>Show all node information in ls. </dd>
<dt><code>-h</code></dt>
<dd>Print a help message describing available options, then exit. </dd>
<dt><code>-V</code></dt>
<dd>Print program version information, then exit. </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gfs_controld/">gfs_controld</a></code>(8), <code><a href="/docs/linux/man/8-dlm_tool/">dlm_tool</a></code>(8) </p>
</dl>