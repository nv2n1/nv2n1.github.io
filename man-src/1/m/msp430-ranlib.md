---
title: "msp430-ranlib(1)"
name: "msp430-ranlib"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msp430-ranlib/"
description: "ranlib – generate index to archive."
---

<h2>NAME</h2>
<p> ranlib &#8211; generate index to archive.</p>
<h2>SYNOPSIS</h2>
<p> ranlib [<code>-vVt</code>] <i>archive</i></p>
<h2>DESCRIPTION</h2>
<p> <code>ranlib</code> generates an index to the contents of an archive and stores it in the archive. The index lists each symbol defined by a member of an archive that is a relocatable object file. </p>
<p> You may use <code>nm -s</code> or <code>nm &#8211;print-armap</code> to list this index. </p>
<p> An archive with such an index speeds up linking to the library and allows routines in the library to call each other without regard to their placement in the archive. </p>
<p> The <font SIZE="-1">GNU</font> <code>ranlib</code> program is another form of <font SIZE="-1">GNU</font> <code>ar</code>; running <code>ranlib</code> is completely equivalent to executing <code>ar -s</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Show the version number of <code>ranlib</code>.</p>
<dt><code>-t</code></p>
<dd> Update the timestamp of the symbol map of an archive.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1), <i><a href="/docs/linux/man/1-nm/">nm</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
