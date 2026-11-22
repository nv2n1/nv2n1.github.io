---

title: "gcov-dump(1)"
name: "gcov-dump"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcov-dump/"
description: "gcov-dump – offline gcda and gcno profile dump tool"
---

<p> gcov-dump &#8211; offline gcda and gcno profile dump tool </p>
<h2>SYNOPSIS</h2>
<p> gcov-dump [<code>-v</code>|<code>&#8211;version</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-h</code>|<code>&#8211;help</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-l</code>|<code>&#8211;long</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-p</code>|<code>&#8211;positions</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-r</code>|<code>&#8211;raw</code>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>gcovfiles</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gcov-dump</code> is a tool you can use in conjunction with GCC to dump content of gcda and gcno profile files offline.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd> Display help about using <code>gcov-dump</code> (on the standard output), and exit without doing any further processing.</dd>
<dt><code>-l</code></dt>
<dd>
</dd><dt><code>&#8211;long</code></dt>
<dd> Dump content of records.</dd>
<dt><code>-p</code></dt>
<dd>
</dd><dt><code>&#8211;positions</code></dt>
<dd> Dump positions of records.</dd>
<dt><code>-r</code></dt>
<dd>
</dd><dt><code>&#8211;raw</code></dt>
<dd> Print content records in raw format.</dd>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display the <code>gcov-dump</code> version number (on the standard output), and exit without doing any further processing.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2017-2021 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with the Invariant Sections being &#8220;GNU General Public License&#8221; and &#8220;Funding Free Software&#8221;, the Front-Cover texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the <i>gfdl</i>(7) man page. </p>
<p> (a) The FSF&#8216;s Front-Cover Text is: </p>
<pre>
     A GNU Manual
</pre>
<p> (b) The FSF&#8216;s Back-Cover Text is: </p>
<pre>
     You have freedom to copy and modify this GNU Manual, like GNU
     software.  Copies published by the Free Software Foundation raise
     funds for GNU development.
</pre>
