---
title: "cargo-clean(1)"
name: "cargo-clean"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-clean/"
description: "cargo-clean – Remove generated artifacts"
---

<h2 class="name">NAME</h2>
<p> cargo-clean &#8211; Remove generated artifacts </p>
<h2>SYNOPSIS</h2>
<p> cargo clean [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> Remove artifacts that cargo has generated in the past. </p>
<p> If the &#8211;package argument is given, then SPEC is a package id specification which indicates which package should be built. If it is not given, then the current package is built. For more information on SPEC and its format, see the &quot;cargo help pkgid&quot; command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC &#8230;</p>
<dd> Package to clean artifacts for.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;manifest-path PATH</code></p>
<dd> Path to the manifest to the package to clean.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;target TRIPLE</code></p>
<dd> Target triple to clean output for (default all).</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;release</code></p>
<dd> Whether or not to clean release artifacts.</p>
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
<h2>EXAMPLES</h2>
<p> Remove local package generated artifacts</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo clean
</pre>
</dl>
<p> Clean release artifacts</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo clean --release
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-build/">cargo-build</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
