---
title: "dh_installexamples(1)"
name: "dh_installexamples"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installexamples/"
description: "dh_installexamples – install example files into package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_installexamples &#8211; install example files into package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installexamples</code> [<i>debhelper options</i>] [<code>-A</code>] [<code>-X</code><i>item</i>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installexamples</code> is a debhelper program that is responsible for installing examples into <i>usr/share/doc/package/examples</i> in package build directories. </p>
<p> From debhelper compatibility level 11 on, <code>dh_install</code> will fall back to looking in <i>debian/tmp</i> for files, if it does not find them in the current directory (or wherever you&#8217;ve told it to look using <code>&#8211;sourcedir</code>).</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.examples</p>
<dd> Lists example files or directories to be installed.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> Install any files specified by command line parameters in <font SIZE="-1">ALL</font> packages acted on.</p>
<dt><code>&#8211;sourcedir=</code><i>dir</i></p>
<dd> Look in the specified directory for files to be installed. This option requires compat 11 or later (it is silently ignored in compat 10 or earlier). </p>
<p> Note that this is not the same as the <code>&#8211;sourcedirectory</code> option used by the <code>dh_auto_</code><i>*</i> commands. You rarely need to use this option, since <code>dh_installexamples</code> automatically looks for files in <i>debian/tmp</i> in debhelper compatibility level 11 and above.</p>
<dt><code>&#8211;doc-main-package=</code><i>main-package</i></p>
<dd> Set the main package for a documentation package. This is used to install the documentation of the documentation package in <i>/usr/share/doc/main-package</i> as recommended by the Debian policy manual 3.9.7 in §12.3. </p>
<p> In compat 11 (or later), this option is only useful if debhelper&#8217;s auto-detection of the main package is wrong. The option can also be used to silence a warning from debhelper when the auto-detection fails but the default happens to be correct. </p>
<p> This option cannot be used when <code>dh_installexamples</code> is instructed to act on multiple packages. If you need this option, you will generally need to combine it with <code>-p</code> to ensure exactly one package is acted on.</p>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude files that contain <i>item</i> anywhere in their filename from being installed.</p>
<dt><i>file</i> &#8230;</p>
<dd> Install these files (or directories) as examples into the first package acted on. (Or into all packages if <code>-A</code> is specified.)</dl>
<h2>NOTES</h2>
<p> Note that <code>dh_installexamples</code> will happily copy entire directory hierarchies if you ask it to (similar to <code>cp -a</code>). If it is asked to install a directory, it will install the complete contents of the directory.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
