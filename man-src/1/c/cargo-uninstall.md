---
title: "cargo-uninstall(1)"
name: "cargo-uninstall"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-uninstall/"
description: "cargo-uninstall – Remove a Rust binary"
---

<h2 class="name">NAME</h2>
<p> cargo-uninstall &#8211; Remove a Rust binary </p>
<h2>SYNOPSIS</h2>
<p> cargo uninstall [OPTIONS] &lt;SPEC&gt; </p>
<p> cargo uninstall (-h | &#8211;help)</p>
<h2>DESCRIPTION</h2>
<p> The argument SPEC is a package id specification (see cargo help pkgid) to specify which crate should be uninstalled. By default all binaries are uninstalled for a crate but the &#8211;bin and &#8211;example flags can be used to only uninstall particular binaries.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;root </code>DIR</p>
<dd> Directory to uninstall packages from.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bin </code>NAME</p>
<dd> Only uninstall the binary NAME.</p>
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
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-install/">cargo-install</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
