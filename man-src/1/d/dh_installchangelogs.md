---
title: "dh_installchangelogs(1)"
name: "dh_installchangelogs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installchangelogs/"
description: "dh_installchangelogs – install changelogs into package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_installchangelogs &#8211; install changelogs into package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installchangelogs</code> [<i>debhelper options</i>] [<code>-k</code>] [<code>-X</code><i>item</i>] [<i>upstream</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installchangelogs</code> is a debhelper program that is responsible for installing changelogs into package build directories. </p>
<p> An upstream <i>changelog</i> file may be specified as an option. </p>
<p> If there is an upstream <i>changelog</i> file, it will be installed as <i>usr/share/doc/package/changelog</i> in the package build directory. </p>
<p> If the upstream changelog is an <i>html</i> file (determined by file extension), it will be installed as <i>usr/share/doc/package/changelog.html</i> instead. If the html changelog is converted to plain text, that variant can be specified as a second upstream changelog file. When no plain text variant is specified, a short <i>usr/share/doc/package/changelog</i> is generated, pointing readers at the html changelog file.</p>
<h2>FILES</h2>
<dl>
<dt><i>debian/changelog</i></p>
<dd>
<dt><i>debian/NEWS</i></p>
<dd>
<dt>debian/<i>package</i>.changelog</p>
<dd>
<dt>debian/<i>package</i>.NEWS</p>
<dd> Automatically installed into usr/share/doc/<i>package</i>/ in the package build directory. </p>
<p> Use the package specific name if <i>package</i> needs a different <i></i><font SIZE="-1"><i>NEWS</i></font><i></i> or <i>changelog</i> file. </p>
<p> The <i>changelog</i> file is installed with a name of changelog for native packages, and <i>changelog.Debian</i> for non-native packages. The <i></i><font SIZE="-1"><i>NEWS</i></font><i></i> file is always installed with a name of <i></i><font SIZE="-1"><i>NEWS</i></font><i>.Debian</i>.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Keep the original name of the upstream changelog. This will be accomplished by installing the upstream changelog as <i>changelog</i>, and making a symlink from that to the original name of the <i>changelog</i> file. This can be useful if the upstream changelog has an unusual name, or if other documentation in the package refers to the <i>changelog</i> file.</p>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude upstream <i>changelog</i> files that contain <i>item</i> anywhere in their filename from being installed.</p>
<dt><i>upstream</i></p>
<dd> Install this file as the upstream changelog.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
