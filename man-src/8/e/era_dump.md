---
title: "era_dump(8)"
name: "era_dump"
section: "8"
letter: "e"
url: "/docs/linux/man/8-era_dump/"
description: "era_dump – dump era metadata from device or file to standard output."
---

<p><code>era_dump </code>&#8211; dump era metadata from device or file to standard output.</p>
<h2>Synopsis</h2>
<pre><code>era_dump</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>era_dump</code> dumps binary era metadata created by the device-mapper era target on a device or file to standard output for analysis or postprocessing in XML format. XML formated metadata can be fed into era_restore (see <code><a href="/docs/linux/man/8-era_restore/">era_restore</a></code>(8)) in order to put it back onto a metadata device (to process by the device-mapper target) or file. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>&#8211;repair</code></p>
<dd>Repair the metadata whilst dumping it.</p>
<dt><code>&#8211;logical</code></p>
<dd>Fold any unprocessed write sets into the final era array.</dl>
<pre> You probably want to do this if you're intending to process the results as
 it simplifies the XML.</pre>
<p><code>-o</code> {xml file} Specify a file for the output rather than writeing to stdout.</p>
<h2>Examples</h2>
<p>Dumps era metadata on logical volume /dev/vg/metadata to standard output in XML format: </p>
<pre> $ era_dump /dev/vg/metadata</pre>
<h2>Diagnostics</h2>
<p><code>era_dump</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-era_check/">era_check</a></code>(8), <code><a href="/docs/linux/man/8-era_restore/">era_restore</a></code>(8), <code><a href="/docs/linux/man/8-era_invalidate/">era_invalidate</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;</p>
