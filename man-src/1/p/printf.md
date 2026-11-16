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
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> FORMAT controls the output as in C printf. Interpreted sequences are:</p>
<dl>
<dt>\&quot;</dt>
<dd> double quote</dd>
<dt>\</dt>
<dd> backslash</dd>
<dt></dt>
<dd> alert (BEL)</dd>
<dt></dt>
<dd> backspace</dd>
<dt>
</dt></dl>