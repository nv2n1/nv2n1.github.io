---
title: "cargo-bench(1)"
name: "cargo-bench"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-bench/"
description: "cargo-bench – Execute benchmarks of a package"
---

<h2 class="name">NAME</h2>
<p> cargo-bench &#8211; Execute benchmarks of a package </p>
<h2>SYNOPSIS</h2>
<p> cargo bench [OPTIONS] [&#8211;] [&lt;ARGS&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Execute all benchmarks of a local package. </p>
<p> All of the trailing arguments are passed to the benchmark binaries generated for filtering benchmarks and generally providing options configuring how they run. </p>
<p> If the &#8211;package argument is given, then SPEC is a package id specification which indicates which package should be built. If it is not given, then the current package is built. For more information on SPEC and its format, see the &quot;cargo help pkgid&quot; command. </p>
<p> The &#8211;jobs argument affects the building of the benchmark executable but does not affect how many jobs are used when running the benchmarks. </p>
<p> Compilation can be customized with the &#8216;bench&#8217; profile in the manifest.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;lib</code></p>
<dd> Benchmark only this package&#8217;s library.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bin </code>NAME</p>
<dd> Benchmark only the specified binary.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;example </code>NAME</p>
<dd> Benchmark only the specified example.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;test </code>NAME</p>
<dd> Benchmark only the specified test target.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bench </code>NAME</p>
<dd> Benchmark only the specified bench target.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-run</code></p>
<dd> Compile, but don&#8217;t run benchmarks.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC &#8230;</p>
<dd> Package to benchmarks for.</p>
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
<p> Execute all the benchmarks of the current package</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo bench
</pre>
</dl>
<p> Execute the BENCH benchmark</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo bench --bench BENCH
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-build/">cargo-build</a>(1), <a href="/docs/linux/man/1-cargo-test/">cargo-test</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
