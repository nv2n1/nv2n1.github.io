---
title: "ucfq(1)"
name: "ucfq"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ucfq/"
description: "ucfq – query the ucf database"
---

<h2 class="name">NAME</h2>
<p> ucfq &#8211; query the ucf database </p>
<h2>SYNOPSIS</h2>
<pre><code>
usage : ucfq[options](/ path / to / file | package)[/ path / to / file | package...]
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code> <code>h</code> Print out a usage message.</p>
<dd>
<dt><code>&#8211;debug</code> <code>-d</code> Turn on debugging mode.</p>
<dd>
<dt><code>&#8211;verbose</code> <code>-v</code> Make the script more verbose..</p>
<dd>
<dt><code>&#8211;with-colons</code> <code>-w</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Normally, the script presents the information in a human readable tabular format, but that may be harder for a machine to parse. With this option, the output is a compact, colon separated line, with no dividers, headers, or footer.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;state-dr</code> dir</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Set the state directory to <tt>&quot;/path/to/dir&quot;</tt> instead of the default <tt>&quot;/var/lib/ucf&quot;</tt>. Used mostly for testing.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> This script takes a set of arguments, each of which is a package name (and thus does not contain a /) or a full path to a configuration file, and outputs the associated package, if any, if the file exists on disk, and whether it has been modified by the user. The output is either a human readable tabular form, or a compact colon-separated machine friendly format. </p>
<p> This script can potentially be used in package <tt>&quot;postrm&quot;</tt> scripts during purge to query the system for configuration files that may still exist on the system, and whether these files have been locally modified by the user &#8212; assuming that the package registered all the configuration files with <code>ucf</code> using <tt>&quot;ucfr&quot;</tt>.</p>
<h2>CAVEATS</h2>
<p> This is very inchoate, at the moment, and needs testing.</p>
<h2>BUGS</h2>
<p> None Known so far.</p>
<h2>AUTHOR</h2>
<p> Manoj Srivastava &lt;srivasta\@debian.org&gt;</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> This script is a part of the Ucf package, and is </p>
<p> Copyright (c) 2006 Manoj Srivastava &lt;srivasta\@debian.org&gt; </p>
<p> This program is free software; you can redistribute it and / or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, <font SIZE="-1">MA</font> 02111-1307 <font SIZE="-1">USA</font> </p>
<h2>Index</h2>
