---

title: "deallocvt(1)"
name: "deallocvt"
section: "1"
letter: "d"
url: "/docs/linux/man/1-deallocvt/"
description: "deallocvt – deallocate unused virtual consoles"
---

<p> deallocvt &#8211; deallocate unused virtual consoles </p>
<h2>SYNOPSIS</h2>
<p> <code>deallocvt</code> [<i>,option/</i>&#8230;] [<i>N</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The command <code>deallocvt</code> deallocates kernel memory and data structures for all unused virtual consoles. If one or more arguments <i>N</i> &#8230; are given, only the corresponding consoles <i>/dev/ttyN</i> are deallocated. </p>
<p> A virtual console is unused if it is not the foreground console, and no process has it open for reading or writing, and no text has been selected on its screen.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-V, &#8211;version</i></dt>
<dd> print program version and exit.</dd>
<dt><i>-h, &#8211;help</i></dt>
<dd> show this text and exit.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chvt/">chvt</a></code>(1), <code><a href="/docs/linux/man/1-openvt/">openvt</a></code>(1) </p>
