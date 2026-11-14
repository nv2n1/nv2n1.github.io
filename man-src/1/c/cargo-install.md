---
title: "cargo-install(1)"
name: "cargo-install"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cargo-install/"
description: "cargo-install – Install a Rust binary"
---

<h2 class="name">NAME</h2>
<p> cargo-install &#8211; Install a Rust binary </p>
<h2>SYNOPSIS</h2>
<p> cargo install [OPTIONS] &lt;CRATE&gt; </p>
<p> cargo install [OPTIONS] &#8211;list</p>
<h2>DESCRIPTION</h2>
<p> Install a Rust binary </p>
<p> This command manages Cargo&#8217;s local set of install binary crates. Only packages which have [[bin]] targets can be installed, and all binaries are installed into the installation root&#8217;s bin folder. The installation root is determined, in order of precedence, by &#8211;root, $CARGO_INSTALL_ROOT, the install.root configuration key, and finally the home directory (which is either $CARGO_HOME if set or $HOME/.cargo by default). </p>
<p> There are multiple sources from which a crate can be installed. The default location is crates.io but the &#8211;git and &#8211;path flags can change this source. If the source contains more than one package (such as crates.io or a git repository with multiple crates) the argument is required to indicate which crate should be installed. </p>
<p> Crates from crates.io can optionally specify the version they wish to install via the &#8211;vers flags, and similarly packages from git repositories can optionally specify the branch, tag, or revision that should be installed. If a crate has multiple binaries, the &#8211;bin argument can selectively install only one of them, and if you&#8217;d rather install examples the &#8211;example argument can be used as well. </p>
<p> As a special convenience, omitting the &lt;crate&gt; specification entirely will install the crate in the current directory. That is, install is equivalent to the more explicit &quot;install &#8211;path .&quot;. </p>
<p> The &#8211;list option will list all installed packages (and their versions).</p>
<h2>OPTIONS</h2>
<h3>Query options</h3>
<dl>
<dt><code>&#8211;list</code></p>
<dd> List all installed packages (and their versions).</p>
<dl>
<dt>
<dd></dl>
</dl>
<h3>Specifying what crate to install</h3>
<dl>
<dt><code>&#8211;vers </code>VERS</p>
<dd> Specify a version to install from crates.io.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;git </code>URL</p>
<dd> Git URL to install the specified crate from.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;branch </code>BRANCH</p>
<dd> Branch to use when installing from git.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;tag </code>TAG</p>
<dd> Tag to use when installing from git.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;rev </code>SHA</p>
<dd> Specific commit to use when installing from git.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;path </code>PATH</p>
<dd> Filesystem path to local crate to install.</p>
<dl>
<dt>
<dd></dl>
</dl>
<h3>Built and install options</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this message.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-j </code>N, &#8211;jobs N</p>
<dd> Number of parallel jobs, defaults to # of CPUs.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;features </code>FEATURES</p>
<dd> Space-separated list of features to activate.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;all-features</code></p>
<dd> Build all available features.</p>
<dl>
<dt>
<dd></dl>
<dt><code>-f, &#8211;force</code></p>
<dd> Force overwriting existing crates or binaries</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-default-features</code></p>
<dd> Do not build the default feature.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;debug</code></p>
<dd> Build in debug mode instead of release mode.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;bin </code>NAME</p>
<dd> Only install the binary NAME.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;example </code>EXAMPLE</p>
<dd> Install the example EXAMPLE instead of binaries.</p>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;root </code>DIR</p>
<dd> Directory to install packages into.</p>
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
<p> <a href="/docs/linux/man/1-cargo/">cargo</a>(1), <a href="/docs/linux/man/1-cargo-search/">cargo-search</a>(1), <a href="/docs/linux/man/1-cargo-publish/">cargo-publish</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> This work is dual-licensed under Apache 2.0 and MIT terms. See COPYRIGHT file in the cargo source distribution. </p>
<h2>Index</h2>
