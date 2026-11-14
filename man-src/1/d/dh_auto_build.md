---
title: "dh_auto_build(1)"
name: "dh_auto_build"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_auto_build/"
description: "dh_auto_build – automatically builds a package"
---

<h2 class="name">NAME</h2>
<p> dh_auto_build &#8211; automatically builds a package </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_auto_build</code> [<i>build system options</i>] [<i>debhelper options</i>] [<code>&#8212;</code> <i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_auto_build</code> is a debhelper program that tries to automatically build a package. It does so by running the appropriate command for the build system it detects the package uses. For example, if a <i>Makefile</i> is found, this is done by running <code>make</code> (or <font SIZE="-1"><code>MAKE</code></font>, if the environment variable is set). If there&#8217;s a <i>setup.py</i>, or <i>Build.PL</i>, it is run to build the package. </p>
<p> This is intended to work for about 90% of packages. If it doesn&#8217;t work, you&#8217;re encouraged to skip using <code>dh_auto_build</code> at all, and just run the build process manually.</p>
<h2>OPTIONS</h2>
<p> See &quot;<font SIZE="-1"><code>BUILD SYSTEM OPTIONS</code></font>&quot; in <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) for a list of common build system selection and control options.</p>
<dl>
<dt><code>&#8212;</code> <i>params</i></p>
<dd> Pass <i>params</i> to the program that is run, after the parameters that <code>dh_auto_build</code> usually passes.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
