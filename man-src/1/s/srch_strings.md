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
<dt><code>-a</code></p>
<dd> Scan the entire file, not just the data section.</p>
<dt><code>-f</code></p>
<dd> Print the name of the file before each string.</p>
<dt><code>-n</code> number, <code>-number</code></p>
<dd> Locate and print any NUL-terminated sequence of at least number characters (default 4).</p>
<dt><code>-t</code> {o,x,d}</p>
<dd> Print the location of the string in base 8, 10 or 16.</p>
<dt><code>-o</code></p>
<dd> An alias for <code>&#8211;radix</code>=o.</p>
<dt><code>-e</code> {s,S,b,l,B,L}</p>
<dd> Select character size and endianness: s = 7-bit, S = 8-bit, {b,l} = 16-bit, {B,L} = 32-bit.</p>
<dt><code>-h</code></p>
<dd> Display command line help.</p>
<dt><code>-v</code></p>
<dd> Print the program&#8217;s version number.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-strings/">strings</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The SleuthKit is copyright (c) Brian Carrier. </p>
<p> This manual page was written by Martin A. Godisch for Debian GNU/Linux, but may be used by others. </p>
<h2>Index</h2>
