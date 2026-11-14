---
title: "era_check(8)"
name: "era_check"
section: "8"
letter: "e"
url: "/docs/linux/man/8-era_check/"
description: "era_check – validate era metadata on device or file."
---

<p><code>era_check </code>&#8211; validate era metadata on device or file.</p>
<h2>Synopsis</h2>
<pre><code>era_check</code> [<i>options</i>] {device|file}</pre>
<h2>Description</h2>
<p><code>era_check</code> checks era metadata created by the device-mapper era target on a device or file. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Suppress output messages, return only exit code.</p>
<dt><code>&#8211;super-block-only</code></p>
<dd>Only check the superblock is present.</dl>
<h2>Example</h2>
<p>Analyse thin provisioning metadata on logical volume /dev/vg/metadata: </p>
<pre> $ era_check /dev/vg/metadata</pre>
<p>The device may not be actively used by the target when running.</p>
<h2>Diagnostics</h2>
<p><code>era_check</code> returns an exit code of 0 for success or 1 for error.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-era_dump/">era_dump</a></code>(8), <code><a href="/docs/linux/man/8-era_restore/">era_restore</a></code>(8), <code><a href="/docs/linux/man/8-era_invalidate/">era_invalidate</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;</p>
