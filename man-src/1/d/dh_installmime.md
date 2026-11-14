---
title: "dh_installmime(1)"
name: "dh_installmime"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installmime/"
description: "dh_installmime – install mime files into package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_installmime &#8211; install mime files into package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installmime</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installmime</code> is a debhelper program that is responsible for installing mime files into package build directories.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.mime</p>
<dd> Installed into usr/lib/mime/packages/<i>package</i> in the package build directory.</p>
<dt>debian/<i>package</i>.sharedmimeinfo</p>
<dd> Installed into /usr/share/mime/packages/<i>package</i>.xml in the package build directory.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
