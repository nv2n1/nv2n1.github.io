---
title: "dh_prep(1)"
name: "dh_prep"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_prep/"
description: "dh_prep – perform cleanups in preparation for building a binary package"
---

<h2 class="name">NAME</h2>
<p> dh_prep &#8211; perform cleanups in preparation for building a binary package </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_prep</code> [<i>debhelper options</i>] [<code>-X</code><i>item</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_prep</code> is a debhelper program that performs some file cleanups in preparation for building a binary package. (This is what <code>dh_clean -k</code> used to do.) It removes the package build directories, <i>debian/tmp</i>, and some temp files that are generated when building a binary package. </p>
<p> It is typically run at the top of the <code>binary-arch</code> and <code>binary-indep</code> targets, or at the top of a target such as install that they depend on.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-X</code><i>item</i> <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being deleted, even if they would normally be deleted. You may use this option multiple times to build up a list of things to exclude.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
