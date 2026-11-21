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
<dt><code>-h, &#8211;help</code></dt>
<dd> Print this message.</dd>
<dl>
</dl>
<dt><code>-p </code>SPEC, &#8211;package SPEC</dt>
<dd> The profile to compiler for.</dd>
<dl>
</dl>
<dt><code>-j </code>N, &#8211;jobs N</dt>
<dd> Number of parallel jobs, defaults to # of CPUs.</dd>
<dl>
</dl>
<dt><code>&#8211;lib</code></dt>
<dd> Build only this package&#8217;s library.</dd>
<dl>
</dl>
<dt><code>&#8211;bin </code>NAME</dt>
<dd> Build only the specified binary.</dd>
<dl>
</dl>
<dt><code>&#8211;example </code>NAME</dt>
<dd> Build only the specified example.</dd>
<dl>
</dl>
<dt><code>&#8211;test </code>NAME</dt>
<dd> Build only the specified test target.</dd>
<dl>
</dl>
<dt><code>&#8211;bench </code>NAME</dt>
<dd> Build only the specified benchmark target.</dd>
<dl>
</dl>
<dt><code>&#8211;release</code></dt>
<dd> Build artifacts in release mode, with optimizations.</dd>
<dl>
</dl>
<dt><code>&#8211;profile </code>PROFILE</dt>
<dd> Profile to build the selected target for.</dd>
<dl>
</dl>
<dt><code>&#8211;features </code>FEATURES</dt>
<dd> The version to yank or un-yank.</dd>
<dl>
</dl>
<dt><code>&#8211;all-features</code></dt>
<dd> Build all available features.</dd>
<dl>
</dl>
<dt><code>&#8211;no-default-features</code></dt>
<dd> Do not compile default features for the package.</dd>
<dl>
</dl>
<dt><code>&#8211;target </code>TRIPLE</dt>
<dd> Target triple which compiles will be for.</dd>
<dl>
</dl>
<dt><code>&#8211;manifest-path </code>PATH</dt>
<dd> Path to the manifest to fetch dependencies for.</dd>
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
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-run/">cargo-run</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
