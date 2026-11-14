---
title: "dh_installpam(1)"
name: "dh_installpam"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installpam/"
description: "dh_installpam – install pam support files"
---

<h2 class="name">NAME</h2>
<p> dh_installpam &#8211; install pam support files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installpam</code> [<i>debhelper options</i>] [<code>&#8211;name=</code><i>name</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installpam</code> is a debhelper program that is responsible for installing files used by <font SIZE="-1">PAM</font> into package build directories.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.pam</p>
<dd> Installed into etc/pam.d/<i>package</i> in the package build directory.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Look for files named debian/<i>package</i>.<i>name</i>.pam and install them as etc/pam.d/<i>name</i>, instead of using the usual files and installing them using the package name.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
