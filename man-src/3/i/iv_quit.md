---
title: "iv_quit(3)"
name: "iv_quit"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_quit/"
description: "iv_quit – signal ivykis to exit the main loop"
---

<h2>NAME</h2>
<p> iv_quit &#8211; signal ivykis to exit the main loop</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv.h&gt;</code> </p>
<p> <code>void iv_quit(void);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_quit</code> signals ivykis to exit the current thread&#8217;s main loop. </p>
<p> If called from any callback function, <code>iv_quit</code> will cause the <code><a href="/docs/linux/man/3-iv_main/">iv_main</a></code>(3) function called from the current thread to return. It is not meant to be used casually.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) </p>
<h2>Index</h2>
