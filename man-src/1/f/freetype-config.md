---
title: "freetype-config(1)"
name: "freetype-config"
section: "1"
letter: "f"
url: "/docs/linux/man/1-freetype-config/"
description: "freetype-config – Get information about a libfreetype installation"
---

<h2 class="name">NAME</h2>
<p> freetype-config &#8211; Get information about a libfreetype installation </p>
<h2>SYNOPSIS</h2>
<p> <code>freetype-config</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>freetype-config</code> returns information needed for compiling and linking programs with the FreeType library, such as linker flags and compilation parameters. Alternatively, it can be used to query information about the FreeType library version installed on the system, such as the installation (directory path) prefix or the FreeType version number. </p>
<p> If <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) is found in the path, <code>freetype-config</code> acts as a wrapper for <code>pkg-config</code>. </p>
<p> This program is part of the FreeType package.</p>
<h2>OPTIONS</h2>
<p> There are two types of options: output/display selection options, and path override options.</p>
<h3>Output selection options</h3>
<p> Only one of the output selection options should be given at each program invocation.</p>
<dl>
<dt><code>&#8211;prefix</code></p>
<dd> Return the prefix value of the installed FreeType library (the default prefix will be `/usr&#8217; in most cases for distribution-installed packages).</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd> Return the executable prefix value of the installed FreeType library (will often be the same as the prefix value).</p>
<dt><code>&#8211;ftversion</code></p>
<dd> Return the FreeType version number, directly derived from file `freetype.h&#8217;.</p>
<dt><code>&#8211;version</code></p>
<dd> Return the `libtool version&#8217; of the FreeType library.</p>
<dt><code>&#8211;libtool</code></p>
<dd> Return the library name for linking with libtool.</p>
<dt><code>&#8211;libs</code></p>
<dd> Return compiler flags for linking with the installed FreeType library.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Return compiler flags for compiling against the installed FreeType library.</p>
<dt><code>&#8211;static</code></p>
<dd> Make command line options display flags for static linking.</p>
<dt><code>&#8211;help</code></p>
<dd> Show help and exit.</dl>
<h3>Path override options</h3>
<p> These affect any selected output option, except the libtool version returned by <code>&#8211;version</code>.</p>
<dl>
<dt><code>&#8211;prefix=</code><i>PREFIX</i></p>
<dd> Override <code>&#8211;prefix</code> value with <i>PREFIX</i>. This also sets <code>&#8211;exec-prefix=</code><i>PREFIX</i> if option <code>&#8211;exec-prefix</code> is not explicitly given.</p>
<dt><code>&#8211;exec-prefix=</code><i>EPREFIX</i></p>
<dd> Override <code>&#8211;exec-prefix</code> value with <i>EPREFIX</i>.</dl>
<h2>BUGS</h2>
<p> In case the libraries FreeType links to are located in non-standard directories, and <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) is not available, the output from option <code>&#8211;libs</code> might be incomplete. It is thus recommended to use the <code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) interface instead, which is able to correctly resolve all dependencies. </p>
<p> Setting <code>&#8211;exec-prefix</code> (either explicitly or implicitly) might return incorrect results if combined with option <code>&#8211;static</code>. The same problem can occur if you set the <code>SYSROOT</code> environment variable.</p>
<h2>AUTHOR</h2>
<p> This manual page was contributed by Nis Martensen &lt;nis.martensen [at] web.de&gt;, with further refinements from the FreeType team. </p>
<h2>Index</h2>
