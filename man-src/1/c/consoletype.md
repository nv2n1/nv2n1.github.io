---
title: "consoletype(1)"
name: "consoletype"
section: "1"
letter: "c"
url: "/docs/linux/man/1-consoletype/"
description: "consoletype – print type of the console connected to standard input"
---

<h2>NAME</h2>
<p> <code>consoletype &#8211; print type of the console connected to standard input </code></p>
<h2>SYNOPSIS</h2>
<p> <code>consoletype [</code><i>stdout</i>] [<i>fg</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>consoletype prints the type of console connected to standard input, and checks whether the console connected to standard input is the current foreground virtual console. With no arguments, it prints </code><i>vt</i> if console is a virtual terminal (/dev/tty* or /dev/console device if not on a serial console), <i>serial</i> if standard input is a serial console (/dev/console or /dev/ttyS*) and <i>pty</i> if standard input is a pseudo terminal.</p>
<h2>RETURN VALUE</h2>
<p> <code>consoletype when passed no arguments returns</p>
<dl>
<dt></code><i>0</dt>
<dd> if on virtual terminal</dd>
<dt>1</dt>
<dd> if on serial console</dd>
<dt>2</dt>
<dd> if on a pseudo terminal.</dd>
<dt>When passed the stdout</i> argument, <code>consoletype</code> returns</dt>
<dd>
</dd><dt><i>0</dt>
<dd> in all cases, and prints the console type to stdout.</dd>
<dt>When passed the fg</i> argument, <code>consoletype</code> returns</dt>
<dd>
</dd><dt><i>0</dt>
<dd> if the console connected to standard input is the current virtual terminal</dd>
<dt>1</dt>
<dd> otherwise. </dd>
</dl>
<p> </i></p>
<h2>Index</h2>
