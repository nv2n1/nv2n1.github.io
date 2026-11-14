---
title: "thin_check(8)"
name: "thin_check"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thin_check/"
description: "thin_check – validates thin provisioning metadata on a device or file"
---

<p><code>thin_check </code>&#8211; validates thin provisioning metadata on a device or file</p>
<h2>Synopsis</h2>
<pre><code>thin_check</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>thin_check</code> checks thin provisioning metadata created by the device-mapper thin provisioning target on a device or file. </p>
<p> The tool cannot be run on live metadata unless the <code>&#8211;metadata-snapshot</code> option is used.</p>
<h2>Options</h2>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress output messages, return only exit code.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Output version information and exit.</p>
<dt><code>&#8211;super-block-only</code></p>
<dd>Only check the superblock.</p>
<dt><code>&#8211;skip-mappings</code></p>
<dd>Skip checking of the block mappings which make up the bulk of the metadata.</p>
<dt><code>&#8211;ignore-non-fatal-errors</code></p>
<dd>Will only return a non-zero exit code if it finds a fatal error.</dl>
<pre> An example of a nonfatal error is an incorrect data block reference count
 causing a block to be considered allocated when it in fact isn't. Ignoring
 errors for a long time is not advised, you really should be using
 thin_repair to fix them.</pre>
<dl>
<dt><code>&#8211;clear-needs-check-flag</code></p>
<dd>Clears the &#8216;needs_check&#8217; flag in the superblock.</dl>
<pre> The kernel may set a flag to force the pool to be checked before it's next
 activated. Set this switch to clear the flag if the check is successful.
 If the metadata check failed, the flag is not cleared and a thin_repair run
 is needed to fix any issues. After thin_repair succeeded, you may run
 thin_check again.</pre>
<dl>
<dt><code>&#8211;metadata-snapshot</code>, <code>-m</code></p>
<dd>Check the metadata snapshot.</dl>
<pre> This will check the devices tree and mappings in a metadata snapshot.
 The snap does not contain space maps, so these will not be checked. This
 may be used on live metadata.</pre>
<dl>
<dt><code>&#8211;auto-repair</code></p>
<dd>Automatically repair any trivial issues found with the metadata.</dl>
<pre> Currently only fixes metadata leaks.</pre>
<dl>
<dt><code>&#8211;override-mapping-root</code> &lt;block&gt;</p>
<dd>Specify a mapping root to use.</dl>
<pre> Don't use this. This overrides what's specified in the superblock. Only
 use this if you really understand the metadata format and are trying to
 recover damaged metadata.</pre>
<h2>Example</h2>
<p>Analyses thin provisioning metadata on logical volume /dev/vg/metadata: </p>
<pre> $ thin_check /dev/vg/metadata</pre>
<p>The device must not be actively used by the target when running.</p>
<h2>Diagnostics</h2>
<p><code>thin_check</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8), <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8), <code><a href="/docs/linux/man/8-thin_rmap/">thin_rmap</a></code>(8), <code><a href="/docs/linux/man/8-thin_metadata_size/">thin_metadata_size</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;heinzm [at] redhat.com&gt;</p>
