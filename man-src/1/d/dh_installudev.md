---
title: "dh_installudev(1)"
name: "dh_installudev"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installudev/"
description: "dh_installudev – install udev rules files"
---

<h2 class="name">NAME</h2>
<p> dh_installudev &#8211; install udev rules files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installudev</code> [<i>debhelper options</i>] [<code>-n</code>] [<code>&#8211;name=</code><i>name</i>] [<code>&#8211;priority=</code><i>priority</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installudev</code> is a debhelper program that is responsible for installing <code>udev</code> rules files.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.udev</p>
<dd> Installed into <i>lib/udev/rules.d/</i> in the package build directory.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> When this parameter is used, <code>dh_installudev</code> looks for and installs files named debian/<i>package</i>.<i>name</i>.udev instead of the usual debian/<i>package</i>.udev.</p>
<dt><code>&#8211;priority=</code><i>priority</i></p>
<dd> Sets the priority the file. Default is 60.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
