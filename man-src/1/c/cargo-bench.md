---

title: "cargo-bench(1)"
name: "cargo-bench"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-bench/"
description: "cargo-bench – Execute benchmarks of a package"
---

<p> cargo bench [OPTIONS] [&#8211;] [&lt;ARGS&gt;&#8230;]</p>
<p> Execute all benchmarks of a local package. </p>
<p> All of the trailing arguments are passed to the benchmark binaries generated for filtering benchmarks and generally providing options configuring how they run. </p>
<p> If the &#8211;package argument is given, then SPEC is a package id specification which indicates which package should be built. If it is not given, then the current package is built. For more information on SPEC and its format, see the &quot;cargo help pkgid&quot; command. </p>
<p> The &#8211;jobs argument affects the building of the benchmark executable but does not affect how many jobs are used when running the benchmarks. </p>
<p> Compilation can be customized with the &#8216;bench&#8217; profile in the manifest.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>&#8211;lib</code></dt>
<dd> Benchmark only this package&#8217;s library.</dd>
<dl>
</dl>
<dt><code>&#8211;bin </code>NAME</dt>
<dd> Benchmark only the specified binary.</dd>
<dl>
</dl>
<dt><code>&#8211;example </code>NAME</dt>
<dd> Benchmark only the specified example.</dd>
<dl>
</dl>
<dt><code>&#8211;test </code>NAME</dt>
<dd> Benchmark only the specified test target.</dd>
<dl>
</dl>
<dt><code>&#8211;bench </code>NAME</dt>
<dd> Benchmark only the specified bench target.</dd>
<dl>
</dl>
<dt><code>&#8211;no-run</code></dt>
<dd> Compile, but don&#8217;t run benchmarks.</dd>
<dl>
</dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC &#8230;</dt>
<dd> Package to benchmarks for.</dd>
<dl>
</dl>
<dt><code>-j </code>IN, &#8211;jobs IN</dt>
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
<p> Execute all the benchmarks of the current package</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo bench
</pre>
</dd></dl>
<p> Execute the BENCH benchmark</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo bench --bench BENCH
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-build/">cargo-build</a>(1), <a href="/docs/linux/man/1-cargo-test/">cargo-test</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
