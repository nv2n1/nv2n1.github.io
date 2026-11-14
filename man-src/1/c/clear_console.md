---
title: "clear_console(1)"
name: "clear_console"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clear_console/"
description: "clear_console – clear the console"
---

<h2 class="name">NAME</h2>
<p> <code>clear_console</code> &#8211; clear the console </p>
<h2>SYNOPSIS</h2>
<p> <code>clear_console</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>clear_console</code> clears your console if this is possible. It looks in the environment for the terminal type and then in the <code>terminfo</code> database to figure out how to clear the screen. To clear the buffer, it then changes the foreground virtual terminal to another terminal and then back to the original terminal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-clear/">clear</a></code>(1), <code><a href="/docs/linux/man/1-chvt/">chvt</a></code>(1) </p>
<h2>Index</h2>
