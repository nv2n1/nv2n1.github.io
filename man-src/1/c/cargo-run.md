---

title: "cargo-run(1)"
name: "cargo-run"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-run/"
description: "cargo-run – Run the current project"
---

<p> cargo run [OPTIONS] [&#8211;] [&lt;ARGS&gt;&#8230;]</p>
<p> Run the main binary of the local package (src/main.rs). </p>
<p> If neither &#8211;bin nor &#8211;example are given, then if the project only has one bin target it will be run. Otherwise &#8211;bin specifies the bin target to run, and &#8211;example specifies the example target to run. At most one of &#8211;bin or &#8211;example can be provided. </p>
<p> All of the trailing arguments are passed to the binary to run. If you&#8217;re passing arguments to both Cargo and the binary, the ones after &#8212; go to the binary, the ones before go to Cargo.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>&#8211;bin </code>NAME</dt>
<dd> Name of the bin target to run.</dd>
<dl>
</dl>
<dt><code>&#8211;example </code>NAME</dt>
<dd> Name of the example target to run.</dd>
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
<p> Run the main binary of the current package</p>
<dl>
<dt>
</dt><dd>
<pre>
$&nbsp;<wbr>cargo run
</pre>
</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-new/">cargo-new</a>(1), <a href="/docs/linux/man/1-cargo-init/">cargo-init</a>(1), <a href="/docs/linux/man/1-cargo-build/">cargo-build</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
