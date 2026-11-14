---
title: "dh_installinfo(1)"
name: "dh_installinfo"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installinfo/"
description: "dh_installinfo – install info files"
---

<h2 class="name">NAME</h2>
<p> dh_installinfo &#8211; install info files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installinfo</code> [<i>debhelper options</i>] [<code>-A</code>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installinfo</code> is a debhelper program that is responsible for installing info files into <i>usr/share/info</i> in the package build directory. </p>
<p> From debhelper compatibility level 11 on, <code>dh_install</code> will fall back to looking in <i>debian/tmp</i> for files, if it does not find them in the current directory (or wherever you&#8217;ve told it to look using <code>&#8211;sourcedir</code>).</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.info</p>
<dd> List info files to be installed.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> Install all files specified by command line parameters in <font SIZE="-1">ALL</font> packages acted on.</p>
<dt><code>&#8211;sourcedir=</code><i>dir</i></p>
<dd> Look in the specified directory for files to be installed. This option requires compat 11 or later (it is silently ignored in compat 10 or earlier). </p>
<p> Note that this is not the same as the <code>&#8211;sourcedirectory</code> option used by the <code>dh_auto_</code><i>*</i> commands. You rarely need to use this option, since <code>dh_installinfo</code> automatically looks for files in <i>debian/tmp</i> in debhelper compatibility level 11 and above.</p>
<dt><i>file</i> &#8230;</p>
<dd> Install these info files into the first package acted on. (Or in all packages if <code>-A</code> is specified).</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
