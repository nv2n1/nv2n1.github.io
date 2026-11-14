---
title: "thin_dump(8)"
name: "thin_dump"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thin_dump/"
description: "thin_dump – dump thin provisioning metadata from device or file to standard output."
---

<p><code>thin_dump </code>&#8211; dump thin provisioning metadata from device or file to standard output.</p>
<h2>Synopsis</h2>
<pre><code>thin_dump</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>thin_dump</code> dumps binary thin provisioning metadata (optionally from alternate block; see option <code>&#8211;metadata-snap</code>) created by the device-mapper thin provisioning target on a device or file to standard output for analysis or postprocessing in either XML or human readable format. XML formated metadata can be fed into thin_restore (see <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8)) in order to put it back onto a metadata device (to process by the device-mapper target) or file. </p>
<p> This tool cannot be run on live metadata unless the <code>&#8211;metadata-snap</code> option is used.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-f</code>, <code>&#8211;format</code> {xml|human_readable|custom}</p>
<dd>Choose output format.</dl>
<pre> Custom formats are supported via shared library plugins. They should be
 specified as in this example:
 $ thin_dump --format custom=mylib.so /dev/sda</pre>
<dl>
<dt><code>-r</code>, <code>&#8211;repair</code></p>
<dd>Repair the metadata whilst dumping it.</p>
<dt><code>-m</code>, <code>&#8211;metadata-snap</code>{=&lt;block nr&gt;}</p>
<dd>Dump metadata snapshot.</dl>
<pre> If block is not provided, access the default metadata snapshot created by
 the thin provisioning device-mapper target, else try the one at block nr.
 See the thin provisioning target documentation on how to create or release
 a metadata snapshot and retrieve the block number from the kernel.</pre>
<dl>
<dt><code>&#8211;dev-id</code> {natural}</p>
<dd>Dump the specified device.</dl>
<pre> This option may be specified multiple times to select more than one thin
 device.</pre>
<dl>
<dt><code>&#8211;transaction-id</code> {natural}</p>
<dd>Override the transaction id given in the input xml.</p>
<dt><code>&#8211;data-block-size</code> {natural}</p>
<dd>Override the data block size given in the input xml.</p>
<dt><code>&#8211;nr-data-blocks</code> {natural}</p>
<dd>Override the nr data blocks given in the input xml.</p>
<dt><code>&#8211;skip-mappings</code></p>
<dd>Do not dump the mappings.</p>
<dt><code>-o</code> {xml file}</p>
<dd>Specify a file for the output rather than writing to stdout.</dl>
<h2>Examples</h2>
<p>Dumps the thin provisioning metadata on logical volume /dev/vg/metadata to standard output in human readable format: </p>
<pre> $ thin_dump -f human_readable /dev/vg/metadata</pre>
<p>Dumps the thin provisioning metadata on logical volume /dev/vg/metadata to standard output in XML format: </p>
<pre> $ thin_dump /dev/vg/metadata</pre>
<p>Dumps the thin provisioning metadata snapshot on logical volume /dev/vg/metadata to standard output in human readable format (not processable by <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8)): </p>
<pre> $ thin_dump --format human_readable --metadata-snap /dev/vg/metadata</pre>
<h2>Diagnostics</h2>
<p><code>thin_dump</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-thin_check/">thin_check</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8), <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8), <code><a href="/docs/linux/man/8-thin_rmap/">thin_rmap</a></code>(8), <code><a href="/docs/linux/man/8-thin_metadata_size/">thin_metadata_size</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
