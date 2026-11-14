---
title: "cache_repair(8)"
name: "cache_repair"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cache_repair/"
description: "cache_repair – repair cache binary metadata from device/file to device/file."
---

<p><code>cache_repair </code>&#8211; repair cache binary metadata from device/file to device/file.</p>
<h2>Synopsis</h2>
<pre><code>cache_repair</code> [<i>options</i>] <code>-i</code> {device|file} <code>-o</code> {device|file}</pre>
<h2>Description</h2>
<p><code>cache_repair</code> reads binary cache metadata created by the respective device-mapper target from one device or file, repairs it and writes it to another device or file. If written to a metadata device, the metadata can be processed by the device-mapper target. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-i</code>, <code>&#8211;input</code> {device|file}</p>
<dd>Input file or device containing binary metadata.</p>
<dt><code>-o</code>, <code>&#8211;output</code> {device|file}</p>
<dd>Output file or device for repaired binary metadata.</dl>
<pre> If a file is then it must be preallocated, and large enough to hold the
 metadata.</pre>
<h2>Example</h2>
<p>Reads the binary cache metadata from file metadata, repairs it and writes it to logical volume /dev/vg/metadata for further processing by the respective device-mapper target: </p>
<pre> $ cache_repair -i metadata -o /dev/vg/metadata</pre>
<h2>Diagnostics</h2>
<p><code>cache_repair</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cache_dump/">cache_dump</a></code>(8), <code><a href="/docs/linux/man/8-cache_check/">cache_check</a></code>(8), <code><a href="/docs/linux/man/8-cache_restore/">cache_restore</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
