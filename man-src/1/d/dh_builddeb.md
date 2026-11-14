---
title: "dh_builddeb(1)"
name: "dh_builddeb"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_builddeb/"
description: "dh_builddeb – build Debian binary packages"
---

<h2 class="name">NAME</h2>
<p> dh_builddeb &#8211; build Debian binary packages </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_builddeb</code> [<i>debhelper options</i>] [<code>&#8211;destdir=</code><i>directory</i>] [<code>&#8211;filename=</code><i>name</i>] [<code>&#8212;</code> <i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_builddeb</code> simply calls <i><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></i>(1) to build a Debian package or packages. It will also build dbgsym packages when <i><a href="/docs/linux/man/1-dh_strip/">dh_strip</a></i>(1) and <i><a href="/docs/linux/man/1-dh_gencontrol/">dh_gencontrol</a></i>(1) have prepared them. </p>
<p> It supports building multiple binary packages in parallel, when enabled by <font SIZE="-1">DEB_BUILD_OPTIONS.</font> </p>
<p> When the <i>Rules-Requires-Root</i> field is not (effectively) <i>binary-targets</i>, <code>dh_builddeb</code> will pass <code>&#8211;root-owner-group</code> to <i><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></i>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;destdir=</code><i>directory</i></p>
<dd> Use this if you want the generated <i>.deb</i> files to be put in a directory other than the default of &quot;<i>..</i>&quot;.</p>
<dt><code>&#8211;filename=</code><i>name</i></p>
<dd> Use this if you want to force the generated .deb file to have a particular file name. Does not work well if more than one .deb is generated!</p>
<dt><code>&#8212;</code> <i>params</i></p>
<dd> Pass <i>params</i> to <i><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></i>(1) when it is used to build the package.</p>
<dt><code>-u</code><i>params</i></p>
<dd> This is another way to pass <i>params</i> to <i><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></i>(1). It is deprecated; use <code>&#8212;</code> instead.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
