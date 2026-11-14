---
title: "dh_doxygen(1)"
name: "dh_doxygen"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_doxygen/"
description: "dh_doxygen – helps with packaging doxygen-generated documentation"
---

<h2 class="name">NAME</h2>
<p> dh_doxygen &#8211; helps with packaging doxygen-generated documentation </p>
<h2>SYNOPSIS</h2>
<p> dh_doxygen [<i>debhelper options</i>] [<code>-X</code><i>item</i>] [<i>directory</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_doxygen</code> is a debhelper program that prepares doxygen-generated documentation for inclusion in a Debian package. More specifically:</p>
<dl>
<dt>&bull;</p>
<dd> It removes <i>*.md5</i> and <i>*.map</i> files. These are created by doxygen to speed up incremental runs.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><i>directory</i></p>
<dd> By default, <code>dh_doxygen</code> scans your package looking for directories looking like they contain doxygen-generated documentation. However, if you explicitly provide one or more directories, only they will be processed.</p>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being symlinked, removed or checked for existence.</dl>
<h2>BUGS</h2>
<p> Probably.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-debhelper/">debhelper</a></code>(7), <code><a href="/docs/linux/man/1-dh/">dh</a></code>(1). </p>
<p> This program is meant to be used together with debhelper.</p>
<h2>AUTHORS</h2>
<p> Jakub Wilk &lt;jwilk [at] debian.org&gt; Helmut Grohne &lt;helmut [at] subdivi.de&gt; </p>
<h2>Index</h2>
