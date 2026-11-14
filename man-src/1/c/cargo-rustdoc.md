---
title: "cargo-rustdoc(1)"
name: "cargo-rustdoc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-rustdoc/"
description: "cargo-rustdoc – Build a package’s documentation, using specified custom flags."
---

<h2 class="name">NAME</h2>
<p> cargo-rustdoc &#8211; Build a package&#8217;s documentation, using specified custom flags.</p>
<h2>SYNOPSIS</h2>
<p> cargo rustdoc [OPTIONS] [&#8211;] [&lt;OPTS&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The specified target for the current package (or package specified by SPEC if provided) will be documented with the specified &lt;OPTS&gt;&#8230; being passed to the final rustdoc invocation. Dependencies will not be documented as part of this command. Note that rustdoc will still unconditionally receive arguments such as -L, &#8211;extern, and &#8211;crate-type, and the specified &lt;OPTS&gt;&#8230; will simply be added to the rustdoc invocation. </p>
<p> If the &#8211;package argument is given, then SPEC is a package id specification which indicates which package should be documented. If it is not given, then the current package is documented. For more information on SPEC and its format, see the cargo help pkgid command. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;open</code></p>
<dd> Open the docs in a browser after the operation.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC</p>
<dd> Package to document.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-j </code>N, &#8211;jobs N</p>
<dd> Number of parallel jobs, defaults to # of CPUs.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;lib</code></p>
<dd> Build only this package&#8217;s library.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bin </code>NAME</p>
<dd> Build only the specified binary.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;example </code>NAME</p>
<dd> Build only the specified example.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;test </code>NAME</p>
<dd> Build only the specified test target.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bench </code>NAME</p>
<dd> Build only the specified benchmark target.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;release</code></p>
<dd> Build artifacts in release mode, with optimizations.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;features </code>FEATURES</p>
<dd> Space-separated list of features to also build.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;all-features</code></p>
<dd> Build all available features.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-default-features</code></p>
<dd> Do not build the default feature.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;target </code>TRIPLE</p>
<dd> Build for the target triple.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;manifest-path </code>PATH</p>
<dd> Path to the manifest to document.</p>
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
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-doc/">cargo-doc</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
