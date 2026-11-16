---
title: "thin_restore(8)"
name: "thin_restore"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thin_restore/"
description: "thin_restore – restore thin provisioning metadata file to device or file."
---

<p><code>thin_restore </code>&#8211; restore thin provisioning metadata file to device or file.</p>
<h2>Synopsis</h2>
<pre><code>thin_restore</code> [<i>options</i>] <code>-i</code> {xml file} <code>-o</code> {device|file}</pre>
<h2>Description</h2>
<p><code>thin_restore</code> restores thin provisioning metadata created by the respective device-mapper target dumped into an XML formatted (see <code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8)) file, which optionally can be preprocessed before the restore to another device or file. If restored to a metadata device, the metadata can be processed by the device-mapper target. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>Print help and exit.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd>Print version information and exit.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd>Suppress output messages, return only exit code.</dd>
<dt><code>-i</code>, <code>&#8211;input</code> {xml file}</dt>
<dd>Input file containing XML metadata.</dd>
<dt><code>-o</code>, <code>&#8211;output</code> {device|file}</dt>
<dd>Output file or device for restored binary metadata.</dd></dl>
<pre> If a file is used for output, then it must be preallocated, and large
 enough to hold the metadata.</pre>
<dl>
<dt><code>&#8211;transaction-id</code> {natural}</dt>
<dd>Override the transaction id given in the input xml.</dd>
<dt><code>&#8211;data-block-size</code> {natural}</dt>
<dd>Override the data block size given in the input xml.</dd>
<dt><code>&#8211;nr-data-blocks</code> {natural}</dt>
<dd>Override the nr data blocks given in the input xml.</dd></dl>
<h2>Example</h2>
<p>Restores the XML formatted thin provisioning metadata on file metadata to logical volume /dev/vg/metadata for further processing by the respective device-mapper target: </p>
<pre> $ thin_restore -i metadata -o /dev/vg/metadata</pre>
<h2>Diagnostics</h2>
<p><code>thin_restore</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_check/">thin_check</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8), <code><a href="/docs/linux/man/8-thin_rmap/">thin_rmap</a></code>(8), <code><a href="/docs/linux/man/8-thin_metadata_size/">thin_metadata_size</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
