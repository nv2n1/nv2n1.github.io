---

title: "cargo-pkgid(1)"
name: "cargo-pkgid"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-pkgid/"
description: "cargo-pkgid – Print a fully qualified package specification"
---

<p> cargo-pkgid &#8211; Print a fully qualified package specification </p>
<h2>SYNOPSIS</h2>
<p> cargo pkgid [OPTIONS] [&lt;SPEC&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Given a &lt;SPEC&gt; argument, print out the fully qualified package id specifier. This command will generate an error if &lt;SPEC&gt; is ambiguous as to which package it refers to in the dependency graph. If no &lt;SPEC&gt; is given, then the pkgid for the local package is printed. </p>
<p> This command requires that a lockfile is available and dependencies have been fetched.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>&#8211;manifest-path </code>PATH</dt>
<dd> Path to the manifest to the package to clean.</dd>
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
<p> Retrive package specification for foo package</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo pkgid foo
</pre>
</dd></dl>
<p> Retrieve package specification for version 1.0.0 of foo</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo pkgid foo:1.0.0
</pre>
</dd></dl>
<p> Retrive package specification for foo from crates.io</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo pkgid crates.io/foo
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-generate-lockfile/">cargo-generate-lockfile</a>(1), <a href="/docs/linux/man/1-cargo-search/">cargo-search</a>(1), <a href="/docs/linux/man/1-cargo-metadata/">cargo-metadata</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
