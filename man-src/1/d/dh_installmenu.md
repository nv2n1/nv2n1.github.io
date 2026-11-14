---
title: "dh_installmenu(1)"
name: "dh_installmenu"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installmenu/"
description: "dh_installmenu – install Debian menu files into package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_installmenu &#8211; install Debian menu files into package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installmenu</code> [<code>debhelper options</code>] [<code>-n</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installmenu</code> is a debhelper program that is responsible for installing files used by the Debian <code>menu</code> package into package build directories. </p>
<p> It also automatically generates the <i>postinst</i> and <i>postrm</i> commands needed to interface with the Debian <code>menu</code> package. These commands are inserted into the maintainer scripts by <i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1).</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.menu</p>
<dd> Debian menu files, installed into usr/share/menu/<i>package</i> in the package build directory. See <i><a href="/docs/linux/man/5-menufile/">menufile</a></i>(5) for its format.</p>
<dt>debian/<i>package</i>.menu-method</p>
<dd> Debian menu method files, installed into etc/menu-methods/<i>package</i> in the package build directory.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;no-scripts</code></p>
<dd> Do not modify <i>postinst</i>/<i>postrm</i> scripts.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) <i><a href="/docs/linux/man/1-update-menus/">update-menus</a></i>(1) <i><a href="/docs/linux/man/5-menufile/">menufile</a></i>(5) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
