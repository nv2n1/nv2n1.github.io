---
title: "dh_installwm(1)"
name: "dh_installwm"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installwm/"
description: "dh_installwm – register a window manager"
---

<h2 class="name">NAME</h2>
<p> dh_installwm &#8211; register a window manager </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installwm</code> [<i>debhelper options</i>] [<code>-n</code>] [<code>&#8211;priority=</code><i>n</i>] [<i>wm</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installwm</code> is a debhelper program that is responsible for generating the <i>postinst</i> and <i>prerm</i> commands that register a window manager with <i><a href="/docs/linux/man/8-update-alternatives/">update-alternatives</a></i>(8). The window manager&#8217;s man page is also registered as a slave symlink (in v6 mode and up). It must be installed in <i>usr/share/man/man1/</i> in the package build directory prior to calling <code>dh_installwm</code>. In compat 9 and earlier, the manpage was optional.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.wm</p>
<dd> List window manager programs to register.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;priority=</code><i>n</i></p>
<dd> Set the priority of the window manager. Default is 20, which is too low for most window managers; see the Debian Policy document for instructions on calculating the correct value.</p>
<dt><code>-n</code>, <code>&#8211;no-scripts</code></p>
<dd> Do not modify <i>postinst</i>/<i>prerm</i> scripts. Turns this command into a no-op.</p>
<dt><i>wm</i> &#8230;</p>
<dd> Window manager programs to register.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
