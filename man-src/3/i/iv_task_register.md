---
title: "iv_task_register(3)"
name: "iv_task_register"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iv_task_register/"
description: "iv_task_register, iv_task_unregister, iv_task_registered – deal with ivykis tasks"
---

<h2>NAME</h2>
<p> iv_task_register, iv_task_unregister, iv_task_registered &#8211; deal with ivykis tasks</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;iv.h&gt;</code> </p>
<pre><code>
struct iv_task {
    void *cookie;
    void (*handler)(void *);
};
</code></pre>
<p> <code>void IV_TASK_INIT(struct iv_task *</code><i>task</i><code>);</code><br />
 <code>void iv_task_register(struct iv_task *</code><i>task</i><code>);</code><br />
 <code>void iv_task_unregister(struct iv_task *</code><i>task</i><code>);</code><br />
 <code>int iv_task_registered(struct iv_task *</code><i>task</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The functions <code>iv_task_register</code> and <code>iv_task_unregister</code> register, respectively unregister, a task with the current thread&#8217;s ivykis event loop. <code>iv_task_registered</code> on a task returns true if that task is currently registered with ivykis. </p>
<p> A task is like a timer, but with an immediate timeout. When a task is registered, unless it is unregistered again first, the callback function specified by <code>-&gt;handler</code> is guaranteed to be called once, in the thread that the task was registered in, some time after control returns to the ivykis main loop but before ivykis will sleep for more events, with <code>-&gt;cookie</code> as its first and sole argument. When this happens, the task is transparently unregistered. </p>
<p> Tasks are mainly used for scheduling code for execution where it is not appropriate to directly run that code in the calling context (for example, because the current context might be run as a callback function where the caller expects certain conditions to remain invariant after the callback completes). </p>
<p> The application is allowed to change the <code>-&gt;cookie</code> and <code>-&gt;handler</code> members at any time. </p>
<p> A given <code>struct iv_task</code> can only be registered in one thread at a time, and a task can only be unregistered in the thread that it was registered from. </p>
<p> There is no limit on the number of tasks registered at once. </p>
<p> See <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) for programming examples.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ivykis/">ivykis</a></code>(3), <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3) </p>
<h2>Index</h2>
