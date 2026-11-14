---
title: "iv_inited(3)"
name: "iv_inited"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_inited/"
description: "iv_init, iv_deinit, iv_inited – initialise and deinitialise ivykis"
---

<h2>NAME</h2>
<p> iv_init, iv_deinit, iv_inited &#8211; initialise and deinitialise ivykis</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv.h&gt;</code> </p>
<p> <code>void iv_init(void);</code><br />
 <code>void iv_deinit(void);</code><br />
 <code>int iv_inited(void);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_init</code> initialises the current thread&#8217;s ivykis event loop. </p>
<p> Each thread that wants to use ivykis must call <code>iv_init</code> before any other ivykis functions are called. </p>
<p> The very first call to <code>iv_init</code> in a process must run to completion before other threads are allowed to call <code>iv_init,</code> but subsequent calls to <code>iv_init</code> can be done concurrently. </p>
<p> <code>iv_deinit</code> frees all resources allocated by ivykis in this thread, and should be called before this thread exits. </p>
<p> <code>iv_inited</code> returns true if <code>iv_init</code> has been called in this thread. After <code>iv_deinit</code> is called, it will return false.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) </p>
<h2>Index</h2>
