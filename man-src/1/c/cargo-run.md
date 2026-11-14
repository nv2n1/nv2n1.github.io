---
title: "cargo-run(1)"
name: "cargo-run"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-run/"
description: "cargo-run – Run the current project"
---

<h2 class="name">NAME</h2>
<p> cargo-run &#8211; Run the current project </p>
<h2>SYNOPSIS</h2>
<p> cargo run [OPTIONS] [&#8211;] [&lt;ARGS&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Run the main binary of the local package (src/main.rs). </p>
<p> If neither &#8211;bin nor &#8211;example are given, then if the project only has one bin target it will be run. Otherwise &#8211;bin specifies the bin target to run, and &#8211;example specifies the example target to run. At most one of &#8211;bin or &#8211;example can be provided. </p>
<p> All of the trailing arguments are passed to the binary to run. If you&#8217;re passing arguments to both Cargo and the binary, the ones after &#8212; go to the binary, the ones before go to Cargo.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bin </code>NAME</p>
<dd> Name of the bin target to run.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;example </code>NAME</p>
<dd> Name of the example target to run.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-j </code>IN, &#8211;jobs IN</p>
<dd> Number of parallel jobs, defaults to # of CPUs.</p>
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
<p> Run the main binary of the current package</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo run
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-new/">cargo-new</a>(1), <a href="/docs/linux/man/1-cargo-init/">cargo-init</a>(1), <a href="/docs/linux/man/1-cargo-build/">cargo-build</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
