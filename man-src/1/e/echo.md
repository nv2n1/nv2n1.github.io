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
<dt><code>-n</code></dt>
<dd> do not output the trailing newline</dd>
<dt><code>-e</code></dt>
<dd> enable interpretation of backslash escapes</dd>
<dt><code>-E</code></dt>
<dd> disable interpretation of backslash escapes (default)</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> If <code>-e</code> is in effect, the following sequences are recognized:</p>
<dl>
<dt>\</dt>
<dd> backslash</dd>
<dt></dt>
<dd> alert (BEL)</dd>
<dt></dt>
<dd> backspace</dd>
<dt>
</dt></dl>