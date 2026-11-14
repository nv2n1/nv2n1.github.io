---
title: "relay_open(9)"
name: "relay_open"
section: "9"
letter: "r"
url: "/docs/linux/man/9-relay_open/"
description: "relay_open – create a new relay channel"
---

<p>relay_open &#8211; create a new relay channel</p>
<h2>Synopsis</h2>
<pre><code>struct rchan *relay_open(const char *base_filename, struct dentry *parent, size_t subbuf_size, size_t n_subbufs, struct rchan_callbacks *cb, void *private_data);</code></pre>
<h2>Arguments</h2>
<p><i>base_filename</i></p>
<dl>
<dd>
<dd>base name of files to create, <code>NULL</code> for buffering only</dl>
<p> <i>parent</i></p>
<dl>
<dd>dentry of parent directory, <code>NULL</code> for root directory or buffer</dl>
<p> <i>subbuf_size</i></p>
<dl>
<dd>size of sub-buffers</dl>
<p> <i>n_subbufs</i></p>
<dl>
<dd>number of sub-buffers</dl>
<p> <i>cb</i></p>
<dl>
<dd>client callback functions</dl>
<p> <i>private_data</i></p>
<dl>
<dd>user-defined data</dl>
<h2>Description</h2>
<p>Returns channel pointer if successful, <code>NULL</code> otherwise. </p>
<p> Creates a channel buffer for each cpu using the sizes and attributes specified. The created channel buffer files will be named base_filename0&#8230;base_filenameN-1. File permissions will be <code>S_IRUSR</code>. </p>
<p> If opening a buffer (<i>parent</i> = NULL) that you later wish to register in a filesystem, call <code>relay_late_setup_files</code> once the <i>parent</i> dentry is available.</p>
<h2>Copyright</h2>
