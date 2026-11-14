---
title: "relay_late_setup_files(9)"
name: "relay_late_setup_files"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_late_setup_files/"
description: "relay_late_setup_files – triggers file creation"
---

<p>relay_late_setup_files &#8211; triggers file creation</p>
<h2>Synopsis</h2>
<pre><code>int relay_late_setup_files(struct rchan *chan, const char *base_filename, struct dentry *parent);</code></pre>
<h2>Arguments</h2>
<p><i>chan</i></p>
<dl>
<dd>
<dd>channel to operate on</dl>
<p> <i>base_filename</i></p>
<dl>
<dd>base name of files to create</dl>
<p> <i>parent</i></p>
<dl>
<dd>dentry of parent directory, <code>NULL</code> for root directory</dl>
<h2>Description</h2>
<p>Returns 0 if successful, non-zero otherwise. </p>
<p> Use to setup files for a previously buffer-only channel created by <code>relay_open</code> with a NULL parent dentry. </p>
<p> For example, this is useful for perfomring early tracing in kernel, before VFS is up and then exposing the early results once the dentry is available.</p>
<h2>Copyright</h2>
