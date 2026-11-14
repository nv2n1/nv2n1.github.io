---
title: "dh_missing(1)"
name: "dh_missing"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_missing/"
description: "dh_missing – check for missing files"
---

<h2 class="name">NAME</h2>
<p> dh_missing &#8211; check for missing files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_missing</code> [<code>-X</code><i>item</i>] [<code>&#8211;sourcedir=</code><i>dir</i>] [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_missing</code> compares the list of installed files with the files in the source directory. If any of the files (and symlinks) in the source directory were not installed to somewhere, it will warn on stderr about that (<code>&#8211;list-missing</code>) or fail (<code>&#8211;fail-missing</code>). Please note that without either of these options, <code>dh_missing</code> will silently do nothing. </p>
<p> This may be useful if you have a large package and want to make sure that you don&#8217;t miss installing newly added files in new upstream releases. </p>
<p> Remember to test different kinds of builds (dpkg-buildpackage -A/-B/&#8230;) as you may experience varying results when only a subset of the packages are built.</p>
<h2>FILES</h2>
<dl>
<dt>debian/not-installed</p>
<dd> List the files that are deliberately not installed in <i>any</i> binary package. Paths listed in this file are ignored by <code>dh_missing</code>. However, it is <code>not</code> a method to exclude files from being installed by any of the debhelper tool. If you want a tool to not install a given file, please use its <code>&#8211;exclude</code> option (where available). </p>
<p> <code>dh_missing</code> will expand wildcards in this file (since debhelper 11.1). Wildcards without matches will be ignored.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;list-missing</code></p>
<dd> Warn on stderr about source files not installed to somewhere. </p>
<p> Note that files that are excluded from being moved via the <code>-X</code> option are not warned about. </p>
<p> This is the default in compat 12 and later.</p>
<dt><code>&#8211;fail-missing</code></p>
<dd> This option is like <code>&#8211;list-missing</code>, except if a file was missed, it will not only list the missing files, but also fail with a nonzero exit code.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Michael Stapelberg &lt;stapelberg [at] debian.org&gt; </p>
<h2>Index</h2>
