---
title: "cargo-yank(1)"
name: "cargo-yank"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-yank/"
description: "cargo-yank – Remove a pushed crate from the index"
---

<h2 class="name">NAME</h2>
<p> cargo-yank &#8211; Remove a pushed crate from the index </p>
<h2>SYNOPSIS</h2>
<p> cargo yank [OPTIONS] [&lt;CRATE&gt;]</p>
<h2>DESCRIPTION</h2>
<p> The yank command removes a previously pushed crate&#8217;s version from the server&#8217;s index. This command does not delete any data, and the crate will still be available for download via the registry&#8217;s download link. </p>
<p> Note that existing crates locked to a yanked version will still be able to download the yanked version to use it. Cargo will, however, not allow any new crates to be locked to any yanked version. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;vers </code>VERSION</p>
<dd> The version to yank or un-yank.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;undo</code></p>
<dd> Undo a yank, putting a version back into the index.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;index </code>INDEX</p>
<dd> Registry index to yank from.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;token </code>TOKEN</p>
<dd> API token to use when authenticating.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Use verbose output.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd> No output printed to stdout.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;color </code>WHEN</p>
<dd> Coloring: auto, always, never.</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-owner/">cargo-owner</a>(1), <a href="/docs/linux/man/1-cargo-version/">cargo-version</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
