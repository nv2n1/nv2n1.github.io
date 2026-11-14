---
title: "dh_installemacsen(1)"
name: "dh_installemacsen"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installemacsen/"
description: "dh_installemacsen – register an Emacs add on package"
---

<h2 class="name">NAME</h2>
<p> dh_installemacsen &#8211; register an Emacs add on package </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installemacsen</code> [<i>debhelper options</i>] [<code>-n</code>] [<code>&#8211;priority=</code><i>n</i>] [<code>&#8211;flavor=</code><i>foo</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installemacsen</code> is a debhelper program that is responsible for installing files used by the Debian <code>emacsen-common</code> package into package build directories. </p>
<p> It also automatically generates the <i>preinst</i> <i>postinst</i> and <i>prerm</i> commands needed to register a package as an Emacs add on package. The commands are added to the maintainer scripts by <code>dh_installdeb</code>. See <i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1) for an explanation of how this works.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.emacsen-compat</p>
<dd> Installed into <i>usr/lib/emacsen-common/packages/compat/package</i> in the package build directory.</p>
<dt>debian/<i>package</i>.emacsen-install</p>
<dd> Installed into <i>usr/lib/emacsen-common/packages/install/package</i> in the package build directory.</p>
<dt>debian/<i>package</i>.emacsen-remove</p>
<dd> Installed into <i>usr/lib/emacsen-common/packages/remove/package</i> in the package build directory.</p>
<dt>debian/<i>package</i>.emacsen-startup</p>
<dd> Installed into etc/emacs/site-start.d/50<i>package</i>.el in the package build directory. Use <code>&#8211;priority</code> to use a different priority than 50.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;no-scripts</code></p>
<dd> Do not modify <i>postinst</i>/<i>prerm</i> scripts.</p>
<dt><code>&#8211;priority=</code><i>n</i></p>
<dd> Sets the priority number of a <i>site-start.d</i> file. Default is 50.</p>
<dt><code>&#8211;flavor=</code><i>foo</i></p>
<dd> Sets the flavor a <i>site-start.d</i> file will be installed in. Default is <code>emacs</code>, alternatives include <code>xemacs</code> and <code>emacs20</code>.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) &#8220;usr/share/doc/emacsen-common/debian-emacs-policy.gz&#8221; </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
