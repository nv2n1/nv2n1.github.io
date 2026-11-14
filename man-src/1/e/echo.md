---
title: "echo(1)"
name: "echo"
section: "1"
letter: "e"
url: "/docs/linux/man/1-echo/"
description: "echo – display a line of text"
---

<h2 class="name">NAME</h2>
<p> echo &#8211; display a line of text </p>
<h2>SYNOPSIS</h2>
<p> <code>echo</code> [<i>,SHORT-OPTION/</i>]&#8230; [<i>,STRING/</i>]&#8230;<br />
 <code>echo</code> <i>,LONG-OPTION/</i></p>
<h2>DESCRIPTION</h2>
<p> Echo the STRING(s) to standard output.</p>
<dl>
<dt><code>-n</code></p>
<dd> do not output the trailing newline</p>
<dt><code>-e</code></p>
<dd> enable interpretation of backslash escapes</p>
<dt><code>-E</code></p>
<dd> disable interpretation of backslash escapes (default)</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> If <code>-e</code> is in effect, the following sequences are recognized:</p>
<dl>
<dt>\</p>
<dd> backslash</p>
<dt></p>
<dd> alert (BEL)</p>
<dt></p>
<dd> backspace</p>
<dt>
