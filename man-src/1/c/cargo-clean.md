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
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC &#8230;</dt>
<dd> Package to clean artifacts for.</dd>
<dl>
</dl>
<dt><code>&#8211;manifest-path PATH</code></dt>
<dd> Path to the manifest to the package to clean.</dd>
<dl>
</dl>
<dt><code>&#8211;target TRIPLE</code></dt>
<dd> Target triple to clean output for (default all).</dd>
<dl>
</dl>
<dt><code>&#8211;release</code></dt>
<dd> Whether or not to clean release artifacts.</dd>
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
<h2>EXAMPLES</h2>
<p> Remove local package generated artifacts</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo clean
</pre>
</dd></dl>
<p> Clean release artifacts</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo clean --release
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-build/">cargo-build</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
