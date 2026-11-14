---
title: "dh_installmodules(1)"
name: "dh_installmodules"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installmodules/"
description: "dh_installmodules – register kernel modules"
---

<h2 class="name">NAME</h2>
<p> dh_installmodules &#8211; register kernel modules </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installmodules</code> [<i>debhelper options</i>] [<code>-n</code>] [<code>&#8211;name=</code><i>name</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installmodules</code> is a debhelper program that is responsible for registering kernel modules. </p>
<p> Kernel modules are searched for in the package build directory and if found, <i>preinst</i>, <i>postinst</i> and <i>postrm</i> commands are automatically generated to run <code>depmod</code> and register the modules when the package is installed. These commands are inserted into the maintainer scripts by <i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1).</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.modprobe</p>
<dd> Installed to etc/modprobe.d/<i>package</i>.conf in the package build directory.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;no-scripts</code></p>
<dd> Do not modify <i>preinst</i>/<i>postinst</i>/<i>postrm</i> scripts.</p>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> When this parameter is used, <code>dh_installmodules</code> looks for and installs files named debian/<i>package</i>.<i>name</i>.modprobe instead of the usual debian/<i>package</i>.modprobe</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
