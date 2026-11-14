---
title: "dh_movefiles(1)"
name: "dh_movefiles"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_movefiles/"
description: "dh_movefiles – move files out of debian/tmp into subpackages"
---

<h2 class="name">NAME</h2>
<p> dh_movefiles &#8211; move files out of debian/tmp into subpackages </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_movefiles</code> [<i>debhelper options</i>] [<code>&#8211;sourcedir=</code><i>dir</i>] [<code>-X</code><i>item</i>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_movefiles</code> is a debhelper program that is responsible for moving files out of <i>debian/tmp</i> or some other directory and into other package build directories. This may be useful if your package has a <i>Makefile</i> that installs everything into <i>debian/tmp</i>, and you need to break that up into subpackages. </p>
<p> Note: <code>dh_install</code> is a much better program, and you are recommended to use it instead of <code>dh_movefiles</code>.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.files</p>
<dd> Lists the files to be moved into a package, separated by whitespace. The filenames listed should be relative to <i>debian/tmp/</i>. You can also list directory names, and the whole directory will be moved.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;sourcedir=</code><i>dir</i></p>
<dd> Instead of moving files out of <i>debian/tmp</i> (the default), this option makes it move files out of some other directory. Since the entire contents of the sourcedir is moved, specifying something like <code>&#8211;sourcedir=/</code> is very unsafe, so to prevent mistakes, the sourcedir must be a relative filename; it cannot begin with a `<code>/</code>&#8216;.</p>
<dt><code>-Xitem</code>, <code>&#8211;exclude=item</code></p>
<dd> Exclude files that contain <code>item</code> anywhere in their filename from being installed.</p>
<dt><i>file</i> &#8230;</p>
<dd> Lists files to move. The filenames listed should be relative to <i>debian/tmp/</i>. You can also list directory names, and the whole directory will be moved. It is an error to list files here unless you use <code>-p</code>, <code>-i</code>, or <code>-a</code> to tell <code>dh_movefiles</code> which subpackage to put them in.</dl>
<h2>NOTES</h2>
<p> Note that files are always moved out of <i>debian/tmp</i> by default (even if you have instructed debhelper to use a compatibility level higher than one, which does not otherwise use debian/tmp for anything at all). The idea behind this is that the package that is being built can be told to install into <i>debian/tmp</i>, and then files can be moved by <code>dh_movefiles</code> from that directory. Any files or directories that remain are ignored, and get deleted by <code>dh_clean</code> later.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
