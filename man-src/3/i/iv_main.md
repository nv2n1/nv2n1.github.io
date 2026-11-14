---
title: "iv_main(3)"
name: "iv_main"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_main/"
description: "iv_main – enter the ivykis main loop"
---

<h2>NAME</h2>
<p> iv_main &#8211; enter the ivykis main loop</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv.h&gt;</code> </p>
<p> <code>void iv_main(void);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_main</code> enters the current thread&#8217;s ivykis main loop. </p>
<p> The ivykis main loop consists of checking the status of the registered file descriptors, timers and tasks, and either calling callback functions corresponding to active objects, or blocking until an event arrives. </p>
<p> Each thread that wants to use ivykis must individually call <code>iv_main</code> to enter the ivykis main loop &#8212; but only after having called <code><a href="/docs/linux/man/3-iv_init/">iv_init</a></code>(3) earlier.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3), <code><a href="/docs/linux/man/3-iv_quit/">iv_quit</a></code>(3) </p>
<h2>Index</h2>
