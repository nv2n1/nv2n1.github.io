---
title: "iv_thread_create(3)"
name: "iv_thread_create"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_thread_create/"
description: "iv_thread_create, iv_thread_set_debug_state – ivykis thread convenience functions"
---

<h2>NAME</h2>
<p> iv_thread_create, iv_thread_set_debug_state &#8211; ivykis thread convenience functions</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv_thread.h&gt;</code> </p>
<p> <code>int iv_thread_create(char *</code><i>name</i><code>, void (*</code><i>start_routine</i><code>)(void *), void *</code><i>arg</i><code>);</code><br />
 <code>void iv_thread_set_debug_state(int </code><i>state</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>iv_thread_create</code> is a wrapper around <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) which will maintain an ivykis main loop reference in the calling thread (which must be an <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3) thread, i.e. have had <code><a href="/docs/linux/man/3-iv_init/">iv_init</a></code>(3) called in it) for as long as the created thread is alive. </p>
<p> Maintaining a reference on the calling thread&#8217;s ivykis event loop makes sure that the calling thread will not return from its ivykis main loop before the created thread exits, as that could cause cleanup still happening in the created thread to be interrupted when the calling thread subsequently calls <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3). </p>
<p> The created thread need not be an ivykis thread. </p>
<p> Enabling debugging by calling <code>iv_thread_set_debug</code> with a nonzero argument will print a debug message to standard error whenever a thread is created via <code>iv_thread_create,</code> whenever a thread so created terminates normally by returning from its <code>start_routine,</code> self-terminates by calling <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3), or is successfully canceled by <code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), and whenever destruction of such a thread is signaled back to the calling thread. </p>
<p> For inter-thread signaling, <code>iv_thread</code> uses <code><a href="/docs/linux/man/3-iv_event/">iv_event</a></code>(3). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_event/">iv_event</a></code>(3), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3) </p>
<h2>Index</h2>
