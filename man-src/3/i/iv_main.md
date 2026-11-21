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
<p> <code>#include &lt;iv.h&gt;</code> </p>
<p> <code>void iv_main(void);</code> </p>
<p> <code>iv_main</code> enters the current thread&#8217;s ivykis main loop. </p>
<p> The ivykis main loop consists of checking the status of the registered file descriptors, timers and tasks, and either calling callback functions corresponding to active objects, or blocking until an event arrives. </p>
<p> Each thread that wants to use ivykis must individually call <code>iv_main</code> to enter the ivykis main loop &#8212; but only after having called <code>iv_init</code>(3) earlier.</p>
<h2>SEE ALSO</h2>
<p> <code>ivykis</code>(3), <code>iv_examples</code>(3), <code>iv_quit</code>(3) </p>
