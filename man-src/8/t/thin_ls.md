---
title: "thin_ls(8)"
name: "thin_ls"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thin_ls/"
description: "thin_ls – List thin volumes within a pool."
---

<p><code>thin_ls </code>&#8211; List thin volumes within a pool.</p>
<h2>Synopsis</h2>
<pre><code>thin_ls</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>thin_ls</code> displays infomation about thin volumes in a pool. Pass the metadata device on the command line, not the pool device. </p>
<p> This tool cannot be run on live metadata unless the <code>&#8211;metadata-snap</code> option is used.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-o</code>, <code>&#8211;format</code></p>
<dd>Give a comma separated list of fields to be output.</dl>
<pre> Valid fields are:
 DEV, MAPPED_BLOCKS, EXCLUSIVE_BLOCKS, SHARED_BLOCKS, MAPPED_SECTORS,
 EXCLUSIVE_SECTORS, SHARED_SECTORS, MAPPED_BYTES, EXCLUSIVE_BYTES,
 SHARED_BYTES, MAPPED, EXCLUSIVE, SHARED, TRANSACTION, CREATE_TIME,
 SNAP_TIME</pre>
<dl>
<dt><code>&#8211;no-headers</code></p>
<dd>Don&#8217;t output headers.</p>
<dt><code>-m</code>, <code>&#8211;metadata-snap</code></p>
<dd>Use metadata snapshot.</dl>
<pre> If you want to get information out of a live pool then you will need to
 take a metadata snapshot and use this switch.</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8), <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8), <code><a href="/docs/linux/man/8-thin_rmap/">thin_rmap</a></code>(8), <code><a href="/docs/linux/man/8-thin_trim/">thin_trim</a></code>(8), <code><a href="/docs/linux/man/8-thin_metadata_size/">thin_metadata_size</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;</p>
