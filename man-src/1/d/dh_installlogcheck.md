---
title: "dh_installlogcheck(1)"
name: "dh_installlogcheck"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installlogcheck/"
description: "dh_installlogcheck – install logcheck rulefiles into etc/logcheck/"
---

<h2 class="name">NAME</h2>
<p> dh_installlogcheck &#8211; install logcheck rulefiles into etc/logcheck/ </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installlogcheck</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installlogcheck</code> is a debhelper program that is responsible for installing logcheck rule files.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.logcheck.cracking</p>
<dd>
<dt>debian/<i>package</i>.logcheck.violations</p>
<dd>
<dt>debian/<i>package</i>.logcheck.violations.ignore</p>
<dd>
<dt>debian/<i>package</i>.logcheck.ignore.workstation</p>
<dd>
<dt>debian/<i>package</i>.logcheck.ignore.server</p>
<dd>
<dt>debian/<i>package</i>.logcheck.ignore.paranoid</p>
<dd> Each of these files, if present, are installed into corresponding subdirectories of <i>etc/logcheck/</i> in package build directories.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Look for files named <i>debian/package.name.logcheck.*</i> and install them into the corresponding subdirectories of <i>etc/logcheck/</i>, but use the specified name instead of that of the package.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Jon Middleton &lt;jjm [at] debian.org&gt; </p>
<h2>Index</h2>
