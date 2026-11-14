---
title: "thin_repair(8)"
name: "thin_repair"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thin_repair/"
description: "thin_repair – repair thin provisioning binary metadata."
---

<p><code>thin_repair </code>&#8211; repair thin provisioning binary metadata.</p>
<h2>Synopsis</h2>
<pre><code>thin_repair</code> [<i>options</i>] <code>-i</code> {device|file} <code>-o</code> {device|file}</pre>
<h2>Description</h2>
<p><code>thin_repair</code> reads binary thin provisioning metadata created by the respective device-mapper target from one device or file, repairs it and writes it to different device or file. If written to a metadata device, the metadata can be processed by the device-mapper target. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-i</code>, <code>&#8211;input</code> {device|file}</p>
<dd>Input file or device with binary data.</p>
<dt><code>-o</code>, <code>&#8211;output</code> {device|file}</p>
<dd>Output file or device for binary data.</dl>
<pre> If a file is used for output, then it must be preallocated, and large
 enough to hold the metadata.</pre>
<dl>
<dt><code>&#8211;transaction-id</code> {natural}</p>
<dd>Override the transaction id given in the input xml.</p>
<dt><code>&#8211;data-block-size</code> {natural}</p>
<dd>Override the data block size given in the input xml.</p>
<dt><code>&#8211;nr-data-blocks</code> {natural}</p>
<dd>Override the nr data blocks given in the input xml.</dl>
<h2>Example</h2>
<p>Reads the binary thin provisioning metadata from file metadata, repairs it and writes it to logical volume /dev/vg/metadata for further processing by the respective device-mapper target: </p>
<pre> $ thin_repair -i metadata -o /dev/vg/metadata</pre>
<h2>Diagnostics</h2>
<p><code>thin_repair</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_check/">thin_check</a></code>(8), <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8), <code><a href="/docs/linux/man/8-thin_rmap/">thin_rmap</a></code>(8), <code><a href="/docs/linux/man/8-thin_metadata_size/">thin_metadata_size</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
