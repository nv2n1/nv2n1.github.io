---
title: "cargo(1)"
name: "cargo"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo/"
description: "cargo – The Rust package manager"
---

<h2 class="name">NAME</h2>
<p> cargo &#8211; The Rust package manager </p>
<h2>SYNOPSIS</h2>
<p> cargo &lt;COMMAND&gt; [&lt;ARGS&gt;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This program is a package manager for the Rust language, available at &lt;<a rel="nofollow" href="http://rust-lang.org">http://rust-lang.org</a>&gt;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a help message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version information and exit.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;list</code></p>
<dd> List all available cargo commands.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;explain CODE</code></p>
<dd> Run rustc &#8211;explain CODE</p>
<dl>
<dt>
<dd></dl>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Use verbose output.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;color</code></p>
<dd> Configure coloring of output.</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>COMMANDS</h2>
<p> To get extended information about commands, run cargo help &lt;command&gt; or man cargo-command</p>
<dl>
<dt><code><a href="/docs/linux/man/1-cargo-build/">cargo-build</a>(1)</code></p>
<dd> Compile the current project.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-clean/">cargo-clean</a>(1)</code></p>
<dd> Remove the target directory with build output.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-doc/">cargo-doc</a>(1)</code></p>
<dd> Build this project&#8217;s and its dependencies&#8217; documentation.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-init/">cargo-init</a>(1)</code></p>
<dd> Create a new cargo project in the current directory.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-install/">cargo-install</a>(1)</code></p>
<dd> Install a Rust binary.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-new/">cargo-new</a>(1)</code></p>
<dd> Create a new cargo project.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-run/">cargo-run</a>(1)</code></p>
<dd> Build and execute src/main.rs.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-test/">cargo-test</a>(1)</code></p>
<dd> Run the tests for the package.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-bench/">cargo-bench</a>(1)</code></p>
<dd> Run the benchmarks for the package.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-update/">cargo-update</a>(1)</code></p>
<dd> Update dependencies in Cargo.lock.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-package/">cargo-package</a>(1)</code></p>
<dd> Generate a source tarball for the current package.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-publish/">cargo-publish</a>(1)</code></p>
<dd> Package and upload this project to the registry.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-owner/">cargo-owner</a>(1)</code></p>
<dd> Manage the owners of a crate on the registry.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-uninstall/">cargo-uninstall</a>(1)</code></p>
<dd> Remove a Rust binary.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-search/">cargo-search</a>(1)</code></p>
<dd> Search registry for crates.</p>
<dl>
<dt>
<dd></dl>
<dt><code><a href="/docs/linux/man/1-cargo-version/">cargo-version</a>(1)</code></p>
<dd> Print cargo&#8217;s version and exit.</p>
<dl>
<dt>
<dd></dl>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.cargo</code></p>
<dd> Directory in which Cargo stores repository data. Cargo can be instructed to use a .cargo subdirectory in a different location by setting the CARGO_HOME environment variable.</p>
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
<p> Run tests for a cross-compiled target</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo test --target i686-unknown-linux-gnu
</pre>
</dl>
<p> Create a new project that builds an executable</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo new --bin foobar
</pre>
</dl>
<p> Create a project in the current directory</p>
<dl>
<dt>
<dd>
<pre><code>
$ &amp;nbsp;
mkdir foo &amp;nbsp;
&amp;&amp;&amp;nbsp;
cd foo
    $ &amp;nbsp;
cargo init.
</code></pre>
</dl>
<p> Learn about a command&#8217;s options and usage</p>
<dl>
<dt>
<dd>
<pre>
$&nbsp;<wbr>cargo help clean
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rustc/">rustc</a>(1), <a href="/docs/linux/man/1-rustdoc/">rustdoc</a>(1)</p>
<h2>BUGS</h2>
<p> See &lt;<a rel="nofollow" href="https://github.com/rust-lang/cargo/issues">https://github.com/rust-lang/cargo/issues</a>&gt; for issues.</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
