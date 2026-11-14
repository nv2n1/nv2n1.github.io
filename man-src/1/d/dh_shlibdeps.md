---
title: "dh_shlibdeps(1)"
name: "dh_shlibdeps"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_shlibdeps/"
description: "dh_shlibdeps – calculate shared library dependencies"
---

<h2 class="name">NAME</h2>
<p> dh_shlibdeps &#8211; calculate shared library dependencies </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_shlibdeps</code> [<i>debhelper options</i>] [<code>-L</code><i>package</i>] [<code>-l</code><i>directory</i>] [<code>-X</code><i>item</i>] [<code>&#8212;</code> <i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_shlibdeps</code> is a debhelper program that is responsible for calculating shared library dependencies for packages. </p>
<p> This program is merely a wrapper around <i><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></i>(1) that calls it once for each package listed in the <i>control</i> file, passing it a list of <font SIZE="-1">ELF</font> executables and shared libraries it has found.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being passed to <code>dpkg-shlibdeps</code>. This will make their dependencies be ignored. This may be useful in some situations, but use it with caution. This option may be used more than once to exclude more than one thing.</p>
<dt><code>&#8212;</code> <i>params</i></p>
<dd> Pass <i>params</i> to <i><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></i>(1).</p>
<dt><code>-u</code><i>params</i>, <code>&#8211;dpkg-shlibdeps-params=</code><i>params</i></p>
<dd> This is another way to pass <i>params</i> to <i><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></i>(1). It is deprecated; use <code>&#8212;</code> instead.</p>
<dt><code>-l</code><i>directory</i>[<code>:</code><i>directory</i> &#8230;]</p>
<dd> With recent versions of <code>dpkg-shlibdeps</code>, this option is generally not needed. </p>
<p> It tells <code>dpkg-shlibdeps</code> (via its <code>-l</code> parameter), to look for private package libraries in the specified directory (or directories &#8212; separate with colons). With recent versions of <code>dpkg-shlibdeps</code>, this is mostly only useful for packages that build multiple flavors of the same library, or other situations where the library is installed into a directory not on the regular library search path.</p>
<dt><code>-L</code><i>package</i>, <code>&#8211;libpackage=</code><i>package</i></p>
<dd> With recent versions of <code>dpkg-shlibdeps</code>, this option is generally not needed, unless your package builds multiple flavors of the same library or is relying on <i>debian/shlibs.local</i> for an internal library. </p>
<p> It tells <code>dpkg-shlibdeps</code> (via its <code>-S</code> parameter) to look first in the package build directory for the specified package, when searching for libraries, symbol files, and shlibs files. </p>
<p> If needed, this can be passed multiple times with different package names.</dl>
<h2>EXAMPLES</h2>
<p> Suppose that your source package produces libfoo1, libfoo-dev, and libfoo-bin binary packages. libfoo-bin links against libfoo1, and should depend on it. In your rules file, first run <code>dh_makeshlibs</code>, then <code>dh_shlibdeps</code>: </p>
<pre>
        dh_makeshlibs
        dh_shlibdeps
</pre>
<p> This will have the effect of generating automatically a shlibs file for libfoo1, and using that file and the libfoo1 library in the <i>debian/libfoo1/usr/lib</i> directory to calculate shared library dependency information. </p>
<p> If a libbar1 package is also produced, that is an alternate build of libfoo, and is installed into <i>/usr/lib/bar/</i>, you can make libfoo-bin depend on libbar1 as follows: </p>
<pre>
        dh_shlibdeps -Llibbar1 -l/usr/lib/bar
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7), <i><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></i>(1) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
