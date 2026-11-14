---
title: "i3-input(1)"
name: "i3-input"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i3-input/"
---

<h2 class="name">NAME</h2>
 

 i3-input - interactively take a command for i3 window manager 

<h2>SYNOPSIS</h2>

 

 i3-input [-s &lt;socket&gt;] [-p &lt;prefix&gt;] [-l &lt;limit&gt;] [-P &lt;prompt&gt;] [-v]

<h2>DESCRIPTION</h2>

 

 i3-input is a tool to take commands (or parts of a command) composed by the user, and send it/them to i3. This is useful, for example, for the mark/goto command.

<h2>EXAMPLE</h2>

 

<dl>
<dt>
<dd> <pre>
i3-input -p 'mark ' -l 1 -P 'Mark: '
</pre></dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-i3/">i3</a>(1)

<h2>AUTHOR</h2>

 

 Michael Stapelberg and contributors 

<h2>Index</h2>


