---
title: "dpkg-realpath(1)"
name: "dpkg-realpath"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-realpath/"
description: "dpkg-realpath – print the resolved pathname with DPKG_ROOT support"
---

<h2 class="name">NAME</h2>
<p> dpkg-realpath &#8211; print the resolved pathname with DPKG_ROOT support </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-realpath</code> [<i>option</i>&#8230;] <i>pathname</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-realpath</code> is a tool (since dpkg 1.20.1) to resolve a pathname, that takes the <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) root directory into account, either implicitly from the <font SIZE="-1"><code>DPKG_ROOT</code></font> environment variable or from the command-line <code>&#8211;root</code> or <code>&#8211;instdir</code> options, and returns an absolute <i>pathname</i> relative to the root directory. The root directory must not be prefixed to the <i>pathname</i> to be resolved. </p>
<p> This is intended to be used by other <code>dpkg</code> helpers, or by maintainer scripts instead of using <code><a href="/docs/linux/man/1-realpath/">realpath</a></code>(1) or <code><a href="/docs/linux/man/1-readlink/">readlink</a></code>(1) to canonicalize pathnames, as these latter commands do not support canonicalization relative to a different root than <i>/</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd> Use a <font SIZE="-1">NUL</font> byte to end output lines instead of a new line character (since dpkg 1.20.6).</p>
<dt><code>&#8211;instdir</code> <i>directory</i></p>
<dd>
<dt><code>&#8211;root</code> <i>directory</i></p>
<dd> Set the root directory to <i>directory</i>, which is the base directory that pathnames get canonicalized against. Defaults to &laquo;<code>/</code>&raquo;.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_ROOT</code></font></p>
<dd> If set and the <code>&#8211;instdir</code> or <code>&#8211;root</code> options have not been specified, it will be used as the filesystem root directory.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode. The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-realpath/">realpath</a></code>(1), <code><a href="/docs/linux/man/1-readlink/">readlink</a></code>(1). </p>
<h2>Index</h2>
