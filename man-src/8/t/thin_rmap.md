---
title: "thin_rmap(8)"
name: "thin_rmap"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thin_rmap/"
description: "thin_rmap – output reverse map of a thin provisioned region of blocks from metadata device or file."
---

<p><code>thin_rmap </code>&#8211; output reverse map of a thin provisioned region of blocks from <code>metadata device or file. </code></p>
<h2>Synopsis</h2>
<pre><code>thin_rmap</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>thin_rmap</code> outputs the reverse mapping stored in the metadata on a device or file between a region of thin provisioned pool blocks and the associated thin provisioned devices. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>&#8211;region</code> {block range}</p>
<dd>Specify range of blocks on the data device.</dl>
<pre> At least one region must be specified. Multiple regions may be specified.
 The range takes the format &lt;begin&gt;..&lt;one past the end&gt;. For example,
 &quot;5..45&quot; specifies data blocks 5 to 44 inclusive, but not 45.</pre>
<h2>Examples</h2>
<p>$ <code>thin_rmap</code> <code>&#8211;region</code> 5..45 /dev/pool-metadata</p>
<h2>Diagnostics</h2>
<p><code>thin_rmap</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-thin_check/">thin_check</a></code>(8), <code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8), <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8), <code><a href="/docs/linux/man/8-thin_metadata_size/">thin_metadata_size</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
