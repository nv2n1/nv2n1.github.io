---
title: "cargo-doc(1)"
name: "cargo-doc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-doc/"
description: "cargo-doc – Build a package’s documentation"
---

<h2 class="name">NAME</h2>
<p> cargo-doc &#8211; Build a package&#8217;s documentation </p>
<h2>SYNOPSIS</h2>
<p> cargo doc [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> Build a package&#8217;s documentation. </p>
<p> By default the documentation for the local package and all dependencies is built. The output is all placed in &#8216;target/doc&#8217; in rustdoc&#8217;s usual format. </p>
<p> If the &#8211;package argument is given, then SPEC is a package id specification which indicates which package should be built. If it is not given, then the current package is built. For more information on SPEC and its format, see the &quot;cargo help pkgid&quot; command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC &#8230;</dt>
<dd> Package to document.</dd>
<dl>
</dl>
<dt><code>&#8211;open</code></dt>
<dd> Opens the docs in a browser after the operation.</dd>
<dl>
</dl>
<dt><code>&#8211;no-deps</code></dt>
<dd> Don&#8217;t build documentation for dependencies.</dd>
<dl>
</dl>
<dt><code>-j </code>N, &#8211;jobs N</dt>
<dd> Number of parallel jobs, defaults to # of CPUs.</dd>
<dl>
</dl>
<dt><code>&#8211;release</code></dt>
<dd> Build artifacts in release mode, with optimizations.</dd>
<dl>
</dl>
<dt><code>&#8211;features </code>FEATURES</dt>
<dd> Space-separated list of features to also build.</dd>
<dl>
</dl>
<dt><code>&#8211;all-features</code></dt>
<dd> Build all available features.</dd>
<dl>
</dl>
<dt><code>&#8211;no-default-features</code></dt>
<dd> Do not build the default feature.</dd>
<dl>
</dl>
<dt><code>&#8211;target </code>TRIPLE</dt>
<dd> Build for the target triple.</dd>
<dl>
</dl>
<dt><code>&#8211;manifest-path </code>PATH</dt>
<dd> Path to the manifest to compile.</dd>
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
<p> Build a local package documentation in &#8216;target/doc&#8217;</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo doc
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-build/">cargo-build</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
