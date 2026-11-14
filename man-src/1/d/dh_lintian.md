---
title: "dh_lintian(1)"
name: "dh_lintian"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_lintian/"
description: "dh_lintian – install lintian override files into package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_lintian &#8211; install lintian override files into package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_lintian</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_lintian</code> is a debhelper program that is responsible for installing override files used by lintian into package build directories.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.lintian-overrides</p>
<dd> Installed into usr/share/lintian/overrides/<i>package</i> in the package build directory. This file is used to suppress erroneous lintian diagnostics.</p>
<dt><i>debian/source/lintian-overrides</i></p>
<dd> These files are not installed, but will be scanned by lintian to provide overrides for the source package.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-debhelper/">debhelper</a></i>(1) </p>
<p> This program is a part of debhelper. </p>
<p> <i><a href="/docs/linux/man/1-lintian/">lintian</a></i>(1)</p>
<h2>AUTHOR</h2>
<p> Steve Robbins &lt;smr [at] debian.org&gt; </p>
<h2>Index</h2>
