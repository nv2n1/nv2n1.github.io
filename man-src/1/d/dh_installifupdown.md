---
title: "dh_installifupdown(1)"
name: "dh_installifupdown"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installifupdown/"
description: "dh_installifupdown – install if-up and if-down hooks"
---

<h2>SYNOPSIS</h2>
<p> <code>dh_installifupdown</code> [<i>debhelper options</i>] [<code>&#8211;name=</code><i>name</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installifupdown</code> is a debhelper program that is responsible for installing <i>if-up</i>, <i>if-down</i>, <i>if-pre-up</i>, and <i>if-post-down</i> hook scripts into package build directories.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.if-up</dt>
<dd>
</dd><dt>debian/<i>package</i>.if-down</dt>
<dd>
</dd><dt>debian/<i>package</i>.if-pre-up</dt>
<dd>
</dd><dt>debian/<i>package</i>.if-post-down</dt>
<dd> These files are installed into etc/network/if-*.d/<i>package</i> in the package build directory.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;name=</code><i>name</i></dt>
<dd> Look for files named <i>debian/package.name.if-*</i> and install them as <i>etc/network/if-*/name</i>, instead of using the usual files and installing them as the package name.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
