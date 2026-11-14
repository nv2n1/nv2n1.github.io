---
title: "open_init_pty(8)"
name: "open_init_pty"
section: "8"
letter: "o"
url: "/docs/linux/man/8-open_init_pty/"
description: "open_init_pty – run an program under a psuedo terminal"
---

<p>open_init_pty &#8211; run an program under a psuedo terminal</p>
<h2>Synopsis</h2>
<p><code>open_init_pty</code> <i>SCRIPT</i> [[<i>ARGS</i>]&#8230;]</p>
<h2>Description</h2>
<p>Run a program under a psuedo terminal. This is used by <code>run_init</code> to run actually run the program after setting up the proper context. This program acquires a new Psuedo terminal, forks a child process that binds to the psueado terminal, and then sits around and connects the physical terminal it was invoked upon with the pseudo terminal, passing keyboard input into to the child process, and passing the output of the child process to the physical terminal. </p>
<p> It sets up the pseudo terminal properly based on the physical terminal attributes, and then sets the user&#8217;s terminal to RAW mode, taking care to reset it on exit.</p>
<h2>Author</h2>
<p>This manual page was written by Manoj Srivastava &lt;srivasta [at] debian.org&gt;, for the Debian GNU/Linux system.</p>
