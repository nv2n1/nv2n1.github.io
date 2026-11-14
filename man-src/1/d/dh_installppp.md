---
title: "dh_installppp(1)"
name: "dh_installppp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installppp/"
description: "dh_installppp – install ppp ip-up and ip-down files"
---

<h2 class="name">NAME</h2>
<p> dh_installppp &#8211; install ppp ip-up and ip-down files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installppp</code> [<i>debhelper options</i>] [<code>&#8211;name=</code><i>name</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installppp</code> is a debhelper program that is responsible for installing ppp ip-up and ip-down scripts into package build directories.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.ppp.ip-up</p>
<dd> Installed into etc/ppp/ip-up.d/<i>package</i> in the package build directory.</p>
<dt>debian/<i>package</i>.ppp.ip-down</p>
<dd> Installed into etc/ppp/ip-down.d/<i>package</i> in the package build directory.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Look for files named <i>debian/package.name.ppp.ip-*</i> and install them as <i>etc/ppp/ip-*/name</i>, instead of using the usual files and installing them as the package name.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
