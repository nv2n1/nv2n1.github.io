---
title: "plugctl(1)"
name: "plugctl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plugctl/"
description: "plugctl – a program to get or set any MPR or PCR register value"
---

<h2>NAME</h2>
<p> plugctl &#8211; a program to get or set any MPR or PCR register value</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>plugctl</code> [<code>-p&nbsp;<wbr></code><i>port</i>] [<code>-n&nbsp;<wbr></code><i>node</i>]<i> plug</i>.<i>attribute</i>[=<i>value</i>] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>plugctl</code> is a program to get or set the value of a plug&#8217;s attribute. </p>
<p> <i>plug</i> is one of oMPR, iMPR, oPCR[n], or iPCR[n] (case insensitive). Please supply a numerical index for [n]. </p>
<dd>This manual page was written for the Debian distribution because the original program does not have a manual page. </p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax. A summary of options is included below. </p>
<dl>
<dt><code>-p </code><i>port</i></p>
<dd> Get or set the value of a plug&#8217;s attribute into this port. </p>
<dt><code>-n </code><i>node</i></p>
<dd> Get or set the value of a plug&#8217;s attribute into this node. </p>
</dl>
<h2>SEE ALSO</h2>
<p> plugreport (1) </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Marcio Roberto Teixeira &lt;marciotex [at] gmail.com&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>AUTHOR</h2>
<p> Marcio Teixeira. </p>
<h2>Index</h2>
