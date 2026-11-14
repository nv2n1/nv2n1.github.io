---
title: "cache_restore(8)"
name: "cache_restore"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cache_restore/"
description: "cache_restore – restore cache metadata file to device or file."
---

<p><code>cache_restore </code>&#8211; restore cache metadata file to device or file.</p>
<h2>Synopsis</h2>
<pre><code>cache_restore</code> [<i>options</i>] <code>-i</code> {xml file} <code>-o</code> {device|file}</pre>
<h2>Description</h2>
<p><code>cache_restore</code> restores cache metadata created by the respective device-mapper target dumped into an XML formatted (see <code><a href="/docs/linux/man/8-cache_dump/">cache_dump</a></code>(8)) file, which optionally can be preprocessed before the restore to another device or file. If restored to a metadata device, the metadata can be processed by the device-mapper target. </p>
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
<dd>Input xml.</p>
<dt><code>-o</code>, <code>&#8211;output</code> {device|file}</p>
<dd>Output file or device for restored binary metadata.</dl>
<pre> If a file is used thin it must be preallocated, and large enough to hold
 the metadata.</pre>
<dl>
<dt><code>&#8211;metadata-version</code> {1|2}</p>
<dd>Choose a metadata version.</dl>
<h2>Debugging Options</h2>
<dl>
<dt><code>&#8211;debug-override-metadata-version</code> {integer}</p>
<dd>Override the version stored in the metadata.</p>
<dt><code>&#8211;omit-clean-shutdown</code></p>
<dd>Don&#8217;t set the clean shutdown flag.</dl>
<h2>Example</h2>
<p>Restores the XML formatted cache metadata on file metadata to logical volume /dev/vg/metadata for further processing by the respective device-mapper target: </p>
<pre> $ cache_restore -i metadata -o /dev/vg/metadata</pre>
<h2>Diagnostics</h2>
<p><code>cache_restore</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cache_dump/">cache_dump</a></code>(8), <code><a href="/docs/linux/man/8-cache_check/">cache_check</a></code>(8), <code><a href="/docs/linux/man/8-cache_repair/">cache_repair</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
