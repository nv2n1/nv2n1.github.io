---
title: "cache_writeback(8)"
name: "cache_writeback"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cache_writeback/"
description: "cache_writeback – writeback dirty blocks to the origin device."
---

<p><code>cache_writeback </code>&#8211; writeback dirty blocks to the origin device.</p>
<h2>Synopsis</h2>
<pre><code>cache_writeback</code> [<i>options</i>] <code>--metadata-device</code> {device|file} <code>--origin-device</code> {device|file} <code>--fast-device</code> {device|file}</pre>
<h2>Description</h2>
<p><code>cache_writeback</code> is an offline tool that writes back dirty data to the data device (origin). Intended for use in recovery scenarios when the SSD is giving IO errors. </p>
<p> This tool cannot be run on a live cache.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Print help and exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Print version information and exit.</dd>
<dt><code>&#8211;metadata-device</code> {device|file}</dt>
<dd>Location of cache metadata.</dd>
<dt><code>&#8211;origin-device</code> {device|file}</dt>
<dd>Slow device being cached.</dd>
<dt><code>&#8211;fast-device</code> {device|file}</dt>
<dd>Fast device containing the data that needs to be written back.</dd>
<dt><code>&#8211;no-metadata-update</code></dt>
<dd>Do not update the metadata to clear the dirty flags.</dd></dl>
<pre> You may want to use this flag if you're decommissioning the cache.</pre>
<dl>
<dt><code>&#8211;buffer-size-meg</code> {size}</dt>
<dd>Specify the size for the metadata cache.</dd></dl>
<pre> Defaults to 16 Gig, a larger size may improve performance.</pre>
<dl>
<dt><code>&#8211;list-failed-blocks</code></dt>
<dd>List any blocks that failed the writeback process.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cache_dump/">cache_dump</a></code>(8), <code><a href="/docs/linux/man/8-cache_check/">cache_check</a></code>(8), <code><a href="/docs/linux/man/8-cache_repair/">cache_repair</a></code>(8), <code><a href="/docs/linux/man/8-cache_restore/">cache_restore</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;</p>
