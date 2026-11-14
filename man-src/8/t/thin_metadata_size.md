---
title: "thin_metadata_size(8)"
name: "thin_metadata_size"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thin_metadata_size/"
description: "thin_metadata_size – thin provisioning metadata device/file size calculator."
---

<p><code>thin_metadata_size </code>&#8211; thin provisioning metadata device/file size calculator.</p>
<h2>Synopsis</h2>
<pre><code>thin_metadata_size</code> [<i>options</i>]</pre>
<h2>Description</h2>
<p><code>thin_metadata_size</code> calculates the size of the thin provisioning metadata based on the block size of the thin provisioned devices, the size of the thin provisioning pool and the maximum number of all thin provisioned devices and snapshots. Because thin provisioning pools are holding widely variable contents, this tool is needed to provide sensible initial default size.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-b</code>, <code>&#8211;block-size</code> {BLOCKSIZE[bskKmMgGtTpPeEzZyY]}</p>
<dd>Set block size.</dl>
<pre> Block size of thin provisioned devices in units of bytes, sectors,
 kibibytes, kilobytes, ... respectively. Default is in sectors without a
 block size unit specifier. Size/number option arguments can be followed by
 unit specifiers in short one character and long form (eg. -b1m or
 -b1mebibytes).</pre>
<dl>
<dt><code>-s</code>, <code>&#8211;pool-size</code> {POOLSIZE[bskKmMgGtTpPeEzZyY]}</p>
<dd>Set pool size.</dl>
<pre> Thin provisioning pool size in units of bytes, sectors, kibibytes,
 kilobytes, ... respectively. Default is in sectors without a pool size
 unit specifier.</pre>
<dl>
<dt><code>-m</code>, <code>&#8211;max-thins</code> {count[bskKmMgGtTpPeEzZyY]}</p>
<dd>Set max thins.</dl>
<pre> Maximum sum of all thin provisioned devices and snapshots. Unit identifier
 supported to allow for convenient entry of large quantities, eg. 1000000 =
 1M. Default is absolute quantity without a number unit specifier.</pre>
<p><code>-u</code>, <code>&#8211;unit</code> {bskKmMgGtTpPeEzZyY} </p>
<pre> Output unit specifier in units of bytes, sectors, kibibytes, kilobytes, ...
 respectively. Default is in sectors without an output unit specifier.</pre>
<dl>
<dt><code>-n</code>, <code>&#8211;numeric-only</code> {short|long}</p>
<dd>Limit output to just the size number.</dl>
<h2>Examples</h2>
<p>Calculates the thin provisioning metadata device size for block size 64 kibibytes, pool size 1 tebibytes and maximum number of thin provisioned devices and snapshots of 1000 in units of sectors with long output: </p>
<pre> $ thin_metadata_size -b64k -s1t -m1000</pre>
<p>Or (using the long <i>options</i> instead) for block size 1 gibibyte, pool size 1 petabyte and maximum number of thin provisioned devices and snapshots of 1 million with numeric-only output in units of gigabytes: </p>
<pre> $ thin_metadata_size --block-size=1g --pool-size=1P --max-thins=1M --unit=G --numeric-only</pre>
<p>Same as before (1g, 1P, 1M, numeric-only) but with unit specifier character appended: </p>
<pre> $ thin_metadata_size --block-size=1gibi --pool-size=1petabytes --max-thins=1mega --unit=G --numeric-only=short</pre>
<p>Or with unit specifier string appended: </p>
<pre> $ thin_metadata_size --block-size=1gibi --pool-size=1petabytes --max-thins=1mega --unit=G -nlong</pre>
<h2>Diagnostics</h2>
<p><code>thin_metadata_size</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_check/">thin_check</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8), <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8), <code><a href="/docs/linux/man/8-thin_rmap/">thin_rmap</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
