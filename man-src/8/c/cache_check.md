---
title: "cache_check(8)"
name: "cache_check"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cache_check/"
description: "cache_check – validates cache metadata on a device or file."
---

<p><code>cache_check </code>&#8211; validates cache metadata on a device or file.</p>
<h2>Synopsis</h2>
<pre><code>cache_check</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>cache_check</code> checks cache metadata created by the device-mapper cache target on a device or file. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Output version information and exit.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress output messages, return only exit code.</p>
<dt><code>&#8211;super-block-only</code></p>
<dd>Only check the superblock.</p>
<dt><code>&#8211;skip-hints</code></p>
<dd>Skip checking of the policy hint values metadata.</p>
<dt><code>&#8211;skip-discards</code></p>
<dd>Skip checking of the discard bits in the metadata.</p>
<dt><code>&#8211;clear-needs-check-flag</code></p>
<dd>Clears the &#8216;needs_check&#8217; flag in the superblock.</dl>
<pre> The kernel may set a flag to force the pool to be checked before it's next
 activated. Set this switch to clear the flag if the check is successful.
 If the metadata check failed, the flag is not cleared and a cache_repair run
 is needed to fix any issues. After cache_repair succeeded, you may run
 cache_check again.</pre>
<h2>Example</h2>
<p>Analyses and repairs cache metadata on logical volume /dev/vg/metadata: </p>
<pre> $ cache_check /dev/vg/metadata</pre>
<p>The device may not be actively used by the target when running.</p>
<h2>Diagnostics</h2>
<p><code>cache_check</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cache_dump/">cache_dump</a></code>(8), <code><a href="/docs/linux/man/8-cache_repair/">cache_repair</a></code>(8), <code><a href="/docs/linux/man/8-cache_restore/">cache_restore</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;, Heinz Mauelshagen &lt;HeinzM [at] RedHat.com&gt;</p>
