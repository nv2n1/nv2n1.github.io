---
title: "dh_ucf(1)"
name: "dh_ucf"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_ucf/"
description: "dh_ucf – register configuration files with ucf"
---

<h2 class="name">NAME</h2>
<p> dh_ucf &#8211; register configuration files with ucf </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_ucf</code> [<i>debhelper options</i>] [<code>-A</code>] [<code>-n</code>] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_ucf</code> is a debhelper program that is responsible for generating the <i>postinst</i> and <i>postrm</i> commands that register files with <i><a href="/docs/linux/man/1-ucf/">ucf</a></i>(1) and <i><a href="/docs/linux/man/1-ucfr/">ucfr</a></i>(1).</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.ucf</p>
<dd> List pairs of source and destination files to register with ucf. Each pair should be put on its own line, with the source and destination separated by whitespace. Both source and destination must be absolute paths. The source should be a file that is provided by your package, typically in /usr/share/, while the destination is typically a file in /etc/. </p>
<p> A dependency on ucf will be generated in <code>${misc:Depends}</code>.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> Install all files specified by command line parameters in <font SIZE="-1">ALL</font> packages acted on.</p>
<dt><code>-n</code>, <code>&#8211;no-scripts</code></p>
<dd> Do not modify <i>postinst</i>/<i>postrm</i> scripts. Turns this command into a no-op.</p>
<dt><i>file</i> &#8230;</p>
<dd> Install these info files into the first package acted on. (Or in all packages if <code>-A</code> is specified).</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; Jeroen Schot &lt;schot [at] a-eskwadraat.nl&gt; </p>
<h2>Index</h2>
