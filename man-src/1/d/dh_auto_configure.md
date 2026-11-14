---
title: "dh_auto_configure(1)"
name: "dh_auto_configure"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_auto_configure/"
description: "dh_auto_configure – automatically configure a package prior to building"
---

<h2 class="name">NAME</h2>
<p> dh_auto_configure &#8211; automatically configure a package prior to building </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_auto_configure</code> [<i>build system options</i>] [<i>debhelper options</i>] [<code>&#8212;</code> <i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_auto_configure</code> is a debhelper program that tries to automatically configure a package prior to building. It does so by running the appropriate command for the build system it detects the package uses. For example, it looks for and runs a <i>./configure</i> script, <i>Makefile.PL</i>, <i>Build.PL</i>, or <i>cmake</i>. A standard set of parameters is determined and passed to the program that is run. Some build systems, such as make, do not need a configure step; for these <code>dh_auto_configure</code> will exit without doing anything. </p>
<p> This is intended to work for about 90% of packages. If it doesn&#8217;t work, you&#8217;re encouraged to skip using <code>dh_auto_configure</code> at all, and just run <i>./configure</i> or its equivalent manually.</p>
<h2>OPTIONS</h2>
<p> See &quot;<font SIZE="-1"><code>BUILD SYSTEM OPTIONS</code></font>&quot; in <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) for a list of common build system selection and control options.</p>
<dl>
<dt><code>&#8212;</code> <i>params</i></p>
<dd> Pass <i>params</i> to the program that is run, after the parameters that <code>dh_auto_configure</code> usually passes. For example: </p>
<pre>
  dh_auto_configure -- --with-foo --enable-bar
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
