---
title: "cargo-rustc(1)"
name: "cargo-rustc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-rustc/"
description: "cargo-rustc – Compile a package and all of its dependencies"
---

<h2 class="name">NAME</h2>
<p> cargo-rustc &#8211; Compile a package and all of its dependencies </p>
<h2>SYNOPSIS</h2>
<p> cargo rustc [OPTIONS] [&#8211;] [&lt;OPTS&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The specified target for the current package (or package specified by SPEC if provided) will be compiled along with all of its dependencies. The specified &#8230; will all be passed to the final compiler invocation, not any of the dependencies. Note that the compiler will still unconditionally receive arguments such as -L, &#8211;extern, and &#8211;crate-type, and the specified &#8230; will simply be added to the compiler invocation. </p>
<p> This command requires that only one target is being compiled. If more than one target is available for the current package the filters of &#8211;lib, &#8211;bin, etc, must be used to select which target is compiled. To pass flags to all compiler processes spawned by Cargo, use the $RUSTFLAGS environment variable or the build.rustflags configuration option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC</p>
<dd> The profile to compiler for.</p>
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
<dt><code>&#8211;profile </code>PROFILE</p>
<dd> Profile to build the selected target for.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;features </code>FEATURES</p>
<dd> The version to yank or un-yank.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;all-features</code></p>
<dd> Build all available features.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-default-features</code></p>
<dd> Do not compile default features for the package.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;target </code>TRIPLE</p>
<dd> Target triple which compiles will be for.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;manifest-path </code>PATH</p>
<dd> Path to the manifest to fetch dependencies for.</p>
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
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-run/">cargo-run</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
