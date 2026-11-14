---
title: "cargo-build(1)"
name: "cargo-build"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-build/"
description: "cargo-build – Compile the current project"
---

<h2 class="name">NAME</h2>
<p> cargo-build &#8211; Compile the current project </p>
<h2>SYNOPSIS</h2>
<p> cargo build [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> Compile a local package and all of its dependencies. </p>
<p> If the &#8211;package argument is given, then SPEC is a package id specification which indicates which package should be built. If it is not given, then the current package is built. For more information on SPEC and its format, see the &quot;cargo help pkgid&quot; command. </p>
<p> Compilation can be configured via the use of profiles which are configured in the manifest. The default profile for this command is dev, but passing the &#8211;release flag will use the release profile instead.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC &#8230;</p>
<dd> Package to build.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-j </code>IN, &#8211;jobs IN</p>
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
<dt><code>&#8211;all-features</code></p>
<dd> Build all available features.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;features </code>FEATURES</p>
<dd> Space-separated list of features to also build.</p>
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
<dd> Path to the manifest to compile.</p>
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
<p> Build a local package and all of its dependencies</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo build
</pre>
</dl>
<p> Build a package with optimizations</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo build --release
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
