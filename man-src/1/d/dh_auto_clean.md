---
title: "dh_auto_clean(1)"
name: "dh_auto_clean"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_auto_clean/"
description: "dh_auto_clean – automatically cleans up after a build"
---

<h2 class="name">NAME</h2>
<p> dh_auto_clean &#8211; automatically cleans up after a build </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_auto_clean</code> [<i>build system options</i>] [<i>debhelper options</i>] [<code>&#8212;</code> <i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_auto_clean</code> is a debhelper program that tries to automatically clean up after a package build. It does so by running the appropriate command for the build system it detects the package uses. For example, if there&#8217;s a <i>Makefile</i> and it contains a <code>distclean</code>, <code>realclean</code>, or <code>clean</code> target, then this is done by running <code>make</code> (or <font SIZE="-1"><code>MAKE</code></font>, if the environment variable is set). If there is a <i>setup.py</i> or <i>Build.PL</i>, it is run to clean the package. </p>
<p> This is intended to work for about 90% of packages. If it doesn&#8217;t work, or tries to use the wrong clean target, you&#8217;re encouraged to skip using <code>dh_auto_clean</code> at all, and just run <code>make clean</code> manually.</p>
<h2>OPTIONS</h2>
<p> See &quot;<font SIZE="-1"><code>BUILD SYSTEM OPTIONS</code></font>&quot; in <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) for a list of common build system selection and control options.</p>
<dl>
<dt><code>&#8212;</code> <i>params</i></p>
<dd> Pass <i>params</i> to the program that is run, after the parameters that <code>dh_auto_clean</code> usually passes.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
