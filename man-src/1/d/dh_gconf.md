---
title: "dh_gconf(1)"
name: "dh_gconf"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_gconf/"
description: "dh_gconf – install GConf defaults files and register schemas"
---

<h2 class="name">NAME</h2>
<p> dh_gconf &#8211; install GConf defaults files and register schemas </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_gconf</code> [<i>debhelper options</i>] [<code>&#8211;priority=</code><i>priority</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_gconf</code> is a debhelper program that is responsible for installing GConf defaults files and registering GConf schemas. </p>
<p> An appropriate dependency on gconf2 will be generated in <code>${misc:Depends}</code>.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.gconf-defaults</p>
<dd> Installed into <i>usr/share/gconf/defaults/10_package</i> in the package build directory, with <i>package</i> replaced by the package name.</p>
<dt>debian/<i>package</i>.gconf-mandatory</p>
<dd> Installed into <i>usr/share/gconf/mandatory/10_package</i> in the package build directory, with <i>package</i> replaced by the package name.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;priority</code> <i>priority</i></p>
<dd> Use <i>priority</i> (which should be a 2-digit number) as the defaults priority instead of <code>10</code>. Higher values than ten can be used by derived distributions (<code>20</code>), <font SIZE="-1">CDD</font> distributions (<code>50</code>), or site-specific packages (<code>90</code>).</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Ross Burton &lt;ross [at] burtonini.com&gt; Josselin Mouette &lt;joss [at] debian.org&gt; </p>
<h2>Index</h2>
