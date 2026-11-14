---
title: "rnano(1)"
name: "rnano"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rnano/"
description: "rnano – a restricted nano"
---

<h2 class="name">NAME</h2>
<p> rnano &#8211; a restricted nano</p>
<h2>SYNOPSIS</h2>
<p> <code>rnano</code> [<i>options</i>] [[+<i>line</i>[,<i>column</i>]]&nbsp;<i>file</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>rnano</code> runs the <code>nano</code> editor in restricted mode. This allows editing only the specified file or files, and doesn&#8217;t allow the user access to the filesystem nor to a command shell. </p>
<p> In restricted mode, <code>nano</code> will:</p>
<dl>
<dt>&bull;</p>
<dd> not allow suspending;</p>
<dt>&bull;</p>
<dd> not allow saving the current buffer under a different name;</p>
<dt>&bull;</p>
<dd> not allow inserting another file or opening a new buffer;</p>
<dt>&bull;</p>
<dd> not allow appending or prepending to any file;</p>
<dt>&bull;</p>
<dd> not make backup files nor do spell checking. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show the available command-line options and exit.</dl>
<p> For all existing options, see the <code><a href="/docs/linux/man/1-nano/">nano</a></code>(1) man page. </p>
<h2>BUGS</h2>
<p> Please report bugs via <i><a rel="nofollow" href="https://savannah.gnu.org/bugs/?group=nano">https://savannah.gnu.org/bugs/?group=nano</a></i>. </p>
<h2>HOMEPAGE</h2>
<p> <i><a rel="nofollow" href="https://nano-editor.org/">https://nano-editor.org/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nano/">nano</a></code>(1) </p>
<h2>Index</h2>
