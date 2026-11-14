---
title: "thin_trim(8)"
name: "thin_trim"
section: "8"
letter: "t"
url: "/docs/linux/man/8-thin_trim/"
description: "thin_trim – Issue discard requests for free pool space (offline tool)."
---

<p><code>thin_trim </code>&#8211; Issue discard requests for free pool space (offline tool).</p>
<h2>Synopsis</h2>
<pre><code>thin_trim</code> [<i>options</i>] <code>--metadata-dev</code> {device|file} <code>--data-dev</code> {device|file}</pre>
<h2>Description</h2>
<p><code>thin_trim</code> sends discard requests to the pool device for unprovisioned areas. </p>
<p> This tool cannot be run on live metadata.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Print help and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Print version information and exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-thin_dump/">thin_dump</a></code>(8), <code><a href="/docs/linux/man/8-thin_repair/">thin_repair</a></code>(8), <code><a href="/docs/linux/man/8-thin_restore/">thin_restore</a></code>(8), <code><a href="/docs/linux/man/8-thin_rmap/">thin_rmap</a></code>(8), <code><a href="/docs/linux/man/8-thin_metadata_size/">thin_metadata_size</a></code>(8)</p>
<h2>Author</h2>
<p>Joe Thornber &lt;ejt [at] redhat.com&gt;</p>
