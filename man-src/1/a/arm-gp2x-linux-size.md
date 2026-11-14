---
title: "arm-gp2x-linux-size(1)"
name: "arm-gp2x-linux-size"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arm-gp2x-linux-size/"
description: "size – list section sizes and total size."
---

<h2>NAME</h2>
<p> size &#8211; list section sizes and total size.</p>
<h2>SYNOPSIS</h2>
<p> size [<code>-A</code>|<code>-B</code>|<code>&#8211;format=</code><i>compatibility</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;help</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-d</code>|<code>-o</code>|<code>-x</code>|<code>&#8211;radix=</code><i>number</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-t</code>|<code>&#8211;totals</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;target=</code><i>bfdname</i>]&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>[<i>objfile</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The <font SIZE="-1">GNU</font> <code>size</code> utility lists the section sizes&#8212;and the total size&#8212;for each of the object or archive files <i>objfile</i> in its argument list. By default, one line of output is generated for each object file or each module in an archive. </p>
<p> <i>objfile</i>&#8230; are the object files to be examined. If none are specified, the file <tt>&quot;a.out&quot;</tt> will be used.</p>
<h2>OPTIONS</h2>
<p> The command line options have the following meanings:</p>
<dl>
<dt><code>-A</code></p>
<dd>
<dt><code>-B</code></p>
<dd>
<dt><code>&#8211;format=</code><i>compatibility</i></p>
<dd> Using one of these options, you can choose whether the output from <font SIZE="-1">GNU</font> <code>size</code> resembles output from System V <code>size</code> (using <code>-A</code>, or <code>&#8211;format=sysv</code>), or Berkeley <code>size</code> (using <code>-B</code>, or <code>&#8211;format=berkeley</code>). The default is the one-line format similar to Berkeley&#8217;s. </p>
<p> Here is an example of the Berkeley (default) format of output from <code>size</code>: </p>
<pre>
        $ size --format=Berkeley ranlib size
        text    data    bss     dec     hex     filename
        294880  81920   11592   388392  5ed28   ranlib
        294880  81920   11888   388688  5ee50   size
</pre>
<p> This is the same data, but displayed closer to System V conventions: </p>
<pre>
        $ size --format=SysV ranlib size
        ranlib  :
        section         size         addr
        .text         294880         8192       
        .data          81920       303104       
        .bss           11592       385024       
        Total         388392
</pre>
<pre>
        size  :
        section         size         addr
        .text         294880         8192       
        .data          81920       303104       
        .bss           11888       385024       
        Total         388688
</pre>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of acceptable arguments and options.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>-o</code></p>
<dd>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;radix=</code><i>number</i></p>
<dd> Using one of these options, you can control whether the size of each section is given in decimal (<code>-d</code>, or <code>&#8211;radix=10</code>); octal (<code>-o</code>, or <code>&#8211;radix=8</code>); or hexadecimal (<code>-x</code>, or <code>&#8211;radix=16</code>). In <code>&#8211;radix=</code><i>number</i>, only the three values (8, 10, 16) are supported. The total size is always given in two radices; decimal and hexadecimal for <code>-d</code> or <code>-x</code> output, or octal and hexadecimal if you&#8217;re using <code>-o</code>.</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;totals</code></p>
<dd> Show totals of all objects listed (Berkeley format listing mode only).</p>
<dt><code>&#8211;target=</code><i>bfdname</i></p>
<dd> Specify that the object-code format for <i>objfile</i> is <i>bfdname</i>. This option may not be necessary; <code>size</code> can automatically recognize many formats.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display the version number of <code>size</code>.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ar/">ar</a></i>(1), <i><a href="/docs/linux/man/1-objdump/">objdump</a></i>(1), <i><a href="/docs/linux/man/1-readelf/">readelf</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
