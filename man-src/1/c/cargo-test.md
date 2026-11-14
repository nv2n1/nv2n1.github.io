---
title: "cargo-test(1)"
name: "cargo-test"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-test/"
description: "cargo-test – Execute unit and integration tests of a package"
---

<h2 class="name">NAME</h2>
<p> cargo-test &#8211; Execute unit and integration tests of a package </p>
<h2>SYNOPSIS</h2>
<p> cargo test [OPTIONS] [&#8211;] [&lt;ARGS&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Execute all unit and integration tests of a local package. </p>
<p> All of the trailing arguments are passed to the test binaries generated for filtering tests and generally providing options configuring how they run. For example, this will run all tests with the name &#8216;foo&#8217; in their name:</p>
<dl>
<dt>
<dd>
<pre>
cargo test foo
</pre>
</dl>
<p> If the &#8211;package argument is given, then &#8216;SPEC&#8217; is a package id specification which indicates which package should be tested. If it is not given, then the current package is tested. For more information on &#8216;SPEC&#8217; and its format, see the &quot;cargo help pkgid&quot; command. </p>
<p> The &#8211;jobs argument affects the building of the test executable but does not affect how many jobs are used when running the tests. </p>
<p> Compilation can be configured via the &#8216;test&#8217; profile in the manifest. </p>
<p> By default the rust test harness hides output from test execution to keep results readable. Test output can be recovered (e.g. for debugging) by passing &#8211;nocapture to the test binaries:</p>
<dl>
<dt>
<dd>
<pre>
cargo test -- --nocapture
</pre>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;lib</code></p>
<dd> Test only this package&#8217;s library.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;doc</code></p>
<dd> Test only this library&#8217;s documentation</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bin </code>NAME</p>
<dd> Test only the specified binary.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;example </code>NAME</p>
<dd> Test only the specified example.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;test </code>NAME</p>
<dd> Test only the specified integration test target.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bench </code>NAME</p>
<dd> Test only the specified benchmark target.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-run</code></p>
<dd> Compile, but don&#8217;t run tests.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC &#8230;</p>
<dd> Package to run tests for.</p>
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
<dt><code>&#8211;no-fail-fast</code></p>
<dd> Run all tests regardless of failure.</p>
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
<p> Execute all the unit and integration tests of the current package</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo test
</pre>
</dl>
<p> Execute the BENCH benchmark</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo test --bench BENCH
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-build/">cargo-build</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
