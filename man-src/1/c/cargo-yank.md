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
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>&#8211;vers </code>VERSION</dt>
<dd> The version to yank or un-yank.</dd>
<dl>
</dl>
<dt><code>&#8211;undo</code></dt>
<dd> Undo a yank, putting a version back into the index.</dd>
<dl>
</dl>
<dt><code>&#8211;index </code>INDEX</dt>
<dd> Registry index to yank from.</dd>
<dl>
</dl>
<dt><code>&#8211;token </code>TOKEN</dt>
<dd> API token to use when authenticating.</dd>
<dl>
</dl>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Use verbose output.</dd>
<dl>
</dl>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> No output printed to stdout.</dd>
<dl>
</dl>
<dt><code>&#8211;color </code>WHEN</dt>
<dd> Coloring: auto, always, never.</dd>
<dl>
</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-owner/">cargo-owner</a>(1), <a href="/docs/linux/man/1-cargo-version/">cargo-version</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
