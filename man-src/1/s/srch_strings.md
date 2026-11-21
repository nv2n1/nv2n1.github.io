---
title: "srch_strings(1)"
name: "srch_strings"
section: "1"
letter: "s"
url: "/docs/linux/man/1-srch_strings/"
description: "srch_strings – display printable strings in files"
---

<h2 class="name">NAME</h2>
<p> <code>srch_strings </code>&#8211; display printable strings in files </p>
<h2>SYNOPSIS</h2>
<pre><code>
srch_strings[options][files]
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Scan the entire file, not just the data section.</dd>
<dt><code>-f</code></dt>
<dd> Print the name of the file before each string.</dd>
<dt><code>-n</code> number, <code>-number</code></dt>
<dd> Locate and print any NUL-terminated sequence of at least number characters (default 4).</dd>
<dt><code>-t</code> {o,x,d}</dt>
<dd> Print the location of the string in base 8, 10 or 16.</dd>
<dt><code>-o</code></dt>
<dd> An alias for <code>&#8211;radix</code>=o.</dd>
<dt><code>-e</code> {s,S,b,l,B,L}</dt>
<dd> Select character size and endianness: s = 7-bit, S = 8-bit, {b,l} = 16-bit, {B,L} = 32-bit.</dd>
<dt><code>-h</code></dt>
<dd> Display command line help.</dd>
<dt><code>-v</code></dt>
<dd> Print the program&#8217;s version number.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-strings/">strings</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The SleuthKit is copyright (c) Brian Carrier. </p>
<p> This manual page was written by Martin A. Godisch for Debian GNU/Linux, but may be used by others. </p>
