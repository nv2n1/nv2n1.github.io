---
title: "era_restore(8)"
name: "era_restore"
section: "8"
letter: "e"
url: "/docs/linux/man/8-era_restore/"
description: "era_restore – restore era metadata file to device or file."
---

<p><code>era_restore </code>&#8211; restore era metadata file to device or file.</p>
<h2>Synopsis</h2>
<pre><code>era_restore</code> [<i>options</i>] <code>-i</code> {xml file} <code>-o</code> {device|file}</pre>
<h2>Description</h2>
<p><code>era_restore</code> restores era metadata created by the respective device-mapper target dumped into an XML formatted (see <code><a href="/docs/linux/man/8-era_dump/">era_dump</a></code>(8)) file, which optionally can be preprocessed before the restore to another device or file. If restored to a metadata device, the metadata can be processed by the device-mapper target. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Don&#8217;t print any output. Check the exit code to test for success.</p>
<dt><code>-i</code>, <code>&#8211;input</code> {xml file}</p>
<dd>Specify input file containing xml metadata.</p>
<dt><code>-o</code>, <code>&#8211;output</code> {device|file}</p>
<dd>Output device or file for restored binary metadata.</dl>
<pre> If a file is used, then it must be preallocated, and large enough to hold
 the metadata.</pre>
<h2>Example</h2>
<p>Restores the XML formatted era metadata on file metadata to logical volume /dev/vg/metadata for further processing by the respective device-mapper target: </p>
<pre> $ era_restore -i metadata -o /dev/vg/metadata</pre>
<h2>Diagnostics</h2>
<p><code>era_restore</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-era_dump/">era_dump</a></code>(8), <code><a href="/docs/linux/man/8-era_check/">era_check</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
