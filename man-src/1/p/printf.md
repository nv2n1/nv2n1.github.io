---
title: "printf(1)"
name: "printf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-printf/"
description: "printf – format and print data"
---

<h2 class="name">NAME</h2>
<p> printf &#8211; format and print data </p>
<h2>SYNOPSIS</h2>
<p> <code>printf</code> <i>,FORMAT /</i>[<i>,ARGUMENT/</i>]&#8230;<br />
 <code>printf</code> <i>,OPTION/</i></p>
<h2>DESCRIPTION</h2>
<p> Print ARGUMENT(s) according to FORMAT, or execute according to OPTION:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> FORMAT controls the output as in C printf. Interpreted sequences are:</p>
<dl>
<dt>\&quot;</p>
<dd> double quote</p>
<dt>\</p>
<dd> backslash</p>
<dt></p>
<dd> alert (BEL)</p>
<dt></p>
<dd> backspace</p>
<dt>
