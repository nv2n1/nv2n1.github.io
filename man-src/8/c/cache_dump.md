---
title: "cache_dump(8)"
name: "cache_dump"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cache_dump/"
description: "cache_dump – dump cache metadata from device or file to standard output."
---

<p><code>cache_dump </code>&#8211; dump cache metadata from device or file to standard output.</p>
<h2>Synopsis</h2>
<pre><code>cache_dump</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>cache_dump</code> dumps binary cache metadata created by the device-mapper cache target on a device or file to standard output for analysis or postprocessing in XML format. XML formatted metadata can be fed into cache_restore in order to put it back onto a metadata device (to process by the device-mapper target), or file. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-r</code>, <code>&#8211;repair</code></p>
<dd>Repair the metadata whilst dumping it.</p>
<dt><code>-o</code> {xml file}</p>
<dd>Specify an output file for the xml, rather than printing to stdout.</dl>
<h2>Examples</h2>
<p>Dumps the cache metadata on logical volume /dev/vg/metadata to standard output in XML format: </p>
<pre> $ cache_dump /dev/vg/metadata</pre>
<p>Dumps the cache metadata on logical volume /dev/vg/metadata whilst repairing it to standard output in XML format: </p>
<pre> $ cache_dump --repair /dev/vg/metadata</pre>
<h2>Diagnostics</h2>
<p><code>cache_dump</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cache_check/">cache_check</a></code>(8), <code><a href="/docs/linux/man/8-cache_repair/">cache_repair</a></code>(8), <code><a href="/docs/linux/man/8-cache_restore/">cache_restore</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
