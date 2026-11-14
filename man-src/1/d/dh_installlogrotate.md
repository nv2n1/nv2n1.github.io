---
title: "dh_installlogrotate(1)"
name: "dh_installlogrotate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installlogrotate/"
description: "dh_installlogrotate – install logrotate config files"
---

<h2 class="name">NAME</h2>
<p> dh_installlogrotate &#8211; install logrotate config files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installlogrotate</code> [<i>debhelper options</i>] [<code>&#8211;name=</code><i>name</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installlogrotate</code> is a debhelper program that is responsible for installing logrotate config files into <i>etc/logrotate.d</i> in package build directories. Files named <i>debian/package.logrotate</i> are installed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Look for files named <i>debian/package.name.logrotate</i> and install them as <i>etc/logrotate.d/name</i>, instead of using the usual files and installing them as the package name.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
