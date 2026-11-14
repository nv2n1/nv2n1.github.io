---
title: "era_invalidate(8)"
name: "era_invalidate"
section: "8"
letter: "e"
url: "/docs/linux/man/8-era_invalidate/"
description: "era_invalidate – Provide a list of blocks that have changed since a particular era."
---

<p><code>era_invalidate </code>&#8211; Provide a list of blocks that have changed since a particular era.</p>
<h2>Synopsis</h2>
<pre><code>era_invalidate</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>era_invalidate</code> examines era metadata and lists blocks that may have changed since a given era. </p>
<p> This tool cannot be run on live metadata unless the <code>&#8211;metadata-snap</code> option is used.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-o</code> {output file}</p>
<dd>Write output to a file rather than stdout.</p>
<dt><code>&#8211;metadata-snapshot</code></p>
<dd>Use the metadata snapshot rather than the current superblock.</p>
<dt><code>&#8211;written-since</code> {era nr}</p>
<dd>Blocks written since the given era will be listed.</dl>
<h2>Example</h2>
<p>List the blocks that may have been written since the beginning of era 13 on the metadata device /dev/vg/metadata: </p>
<pre> $ era_invalidate --written-since 13 /dev/vg/metadata</pre>
<p>The device may not be actively used by the target when running.</p>
<h2>Diagnostics</h2>
<p><code>era_invalidate</code> returns an exit code of 0 for success or 1 for error (eg, metadata corruption).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-era_check/">era_check</a></code>(8), <code><a href="/docs/linux/man/8-era_dump/">era_dump</a></code>(8), <code><a href="/docs/linux/man/8-era_restore/">era_restore</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;</p>
