---
title: "cargo-pkgid(1)"
name: "cargo-pkgid"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-pkgid/"
description: "cargo-pkgid – Print a fully qualified package specification"
---

<h2 class="name">NAME</h2>
<p> cargo-pkgid &#8211; Print a fully qualified package specification </p>
<h2>SYNOPSIS</h2>
<p> cargo pkgid [OPTIONS] [&lt;SPEC&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Given a &lt;SPEC&gt; argument, print out the fully qualified package id specifier. This command will generate an error if &lt;SPEC&gt; is ambiguous as to which package it refers to in the dependency graph. If no &lt;SPEC&gt; is given, then the pkgid for the local package is printed. </p>
<p> This command requires that a lockfile is available and dependencies have been fetched.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;manifest-path </code>PATH</p>
<dd> Path to the manifest to the package to clean.</p>
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
<p> Retrive package specification for foo package</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo pkgid foo
</pre>
</dl>
<p> Retrieve package specification for version 1.0.0 of foo</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo pkgid foo:1.0.0
</pre>
</dl>
<p> Retrive package specification for foo from crates.io</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo pkgid crates.io/foo
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-generate-lockfile/">cargo-generate-lockfile</a>(1), <a href="/docs/linux/man/1-cargo-search/">cargo-search</a>(1), <a href="/docs/linux/man/1-cargo-metadata/">cargo-metadata</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
