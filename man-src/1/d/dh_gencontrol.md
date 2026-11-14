---
title: "dh_gencontrol(1)"
name: "dh_gencontrol"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_gencontrol/"
description: "dh_gencontrol – generate and install control file"
---

<h2 class="name">NAME</h2>
<p> dh_gencontrol &#8211; generate and install control file </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_gencontrol</code> [<i>debhelper options</i>] [<code>&#8212;</code> <i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_gencontrol</code> is a debhelper program that is responsible for generating control files, and installing them into the <i></i><font SIZE="-1"><i>DEBIAN</i></font><i></i> directory with the proper permissions. </p>
<p> This program is merely a wrapper around <i><a href="/docs/linux/man/1-dpkg-gencontrol/">dpkg-gencontrol</a></i>(1), which calls it once for each package being acted on (plus related dbgsym packages), and passes in some additional useful flags. </p>
<p> <code>Note</code> that if you use <code>dh_gencontrol</code>, you must also use <i><a href="/docs/linux/man/1-dh_builddeb/">dh_builddeb</a></i>(1) to build the packages. Otherwise, your build may fail to build as <code>dh_gencontrol</code> (via <i><a href="/docs/linux/man/1-dpkg-gencontrol/">dpkg-gencontrol</a></i>(1)) declares which packages are built. As debhelper automatically generates dbgsym packages, it some times adds additional packages, which will be built by <i><a href="/docs/linux/man/1-dh_builddeb/">dh_builddeb</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8212;</code> <i>params</i></p>
<dd> Pass <i>params</i> to <i><a href="/docs/linux/man/1-dpkg-gencontrol/">dpkg-gencontrol</a></i>(1).</p>
<dt><code>-u</code><i>params</i>, <code>&#8211;dpkg-gencontrol-params=</code><i>params</i></p>
<dd> This is another way to pass <i>params</i> to <i><a href="/docs/linux/man/1-dpkg-gencontrol/">dpkg-gencontrol</a></i>(1). It is deprecated; use <code>&#8212;</code> instead.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
