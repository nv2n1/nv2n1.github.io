---
title: "update-texmf(8)"
name: "update-texmf"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-texmf/"
description: "update-texmf – shell script to generate /etc/texmf/texmf.cnf"
---

<p>update-texmf &#8211; shell script to generate /etc/texmf/texmf.cnf</p>
<h2>Synopsis</h2>
<p><code>update-texmf</code> <i>[options]</i></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>update-texmf</code> command. This manual page was written for the Debian GNU/Linux distribution because the original script was designed for Debian packaging system. </p>
<p> <code>update-texmf</code> is a shell script to generate /etc/texmf/web2c/texmf.cnf from files in /etc/texmf/texmf.d/*.cnf </p>
<p> A user who wants to customize /etc/texmf/web2c/texmf.cnf should add, for example, 22mymacro.cnf in /etc/texmf/texmf.d/ and run &#8216;update-texmf&#8217;.</p>
<h2>Options</h2>
<dl>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Show verbose messages.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd>Show debugging information, and don&#8217;t delete temporary files. Implies &#8211;verbose.</p>
<dt><code>-o, &#8211;output FILE</code></p>
<dd>Generate output in FILE instead of /etc/texmf/web2c/texmf.cnf.</dl>
<h2>See Also</h2>
<p>Further information can be found in /usr/share/doc/tex-common/README.Debian.{txt,pdf.html} </p>
<h2>Author</h2>
<p>This manual page was written by Atsuhito Kohda &lt;kohda [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
