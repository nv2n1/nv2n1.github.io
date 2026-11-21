---

title: "dh_bugfiles(1)"
name: "dh_bugfiles"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_bugfiles/"
description: "dh_bugfiles – install bug reporting customization files into package build directories"
---

<p> <code>dh_bugfiles</code> [<code>-A</code>] [<i>debhelper options</i>]</p>
<p> <code>dh_bugfiles</code> is a debhelper program that is responsible for installing bug reporting customization files (bug scripts and/or bug control files and/or presubj files) into package build directories.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.bug-script</dt>
<dd> This is the script to be run by the bug reporting program for generating a bug report template. This file is installed as <i>usr/share/bug/package</i> in the package build directory if no other types of bug reporting customization files are going to be installed for the package in question. Otherwise, this file is installed as <i>usr/share/bug/package/script</i>. Finally, the installed script is given execute permissions.</dd>
<dt>debian/<i>package</i>.bug-control</dt>
<dd> It is the bug control file containing some directions for the bug reporting tool. This file is installed as <i>usr/share/bug/package/control</i> in the package build directory.</dd>
<dt>debian/<i>package</i>.bug-presubj</dt>
<dd> The contents of this file are displayed to the user by the bug reporting tool before allowing the user to write a bug report on the package to the Debian Bug Tracking System. This file is installed as <i>usr/share/bug/package/presubj</i> in the package build directory.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></dt>
<dd> Install <i>debian/bug-*</i> files to <font SIZE="-1">ALL</font> packages acted on when respective <i>debian/package.bug-*</i> files do not exist. Normally, <i>debian/bug-*</i> will be installed to the first package only.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i>/usr/share/doc/reportbug/README.developers.gz</i> </p>
<p> <i>debhelper</i>(1) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Modestas Vainius &lt;modestas [at] vainius.eu&gt; </p>
