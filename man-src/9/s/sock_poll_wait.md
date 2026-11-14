---
title: "sock_poll_wait(9)"
name: "sock_poll_wait"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sock_poll_wait/"
---

sock_poll_wait - place memory barrier behind the poll_wait call.

<h2>Synopsis</h2>

<pre><code>void sock_poll_wait(struct file *filp, wait_queue_head_t *wait_address, poll_table *p);</code></pre>

<h2>Arguments</h2>

<i>filp</i>
<dl><dd><dd>file</dl>
 

 <i>wait_address</i>
<dl><dd>socket wait queue</dl>
 

 <i>p</i>
<dl><dd>poll_table</dl>

<h2>Description</h2>

See the comments in the wq_has_sleeper function.

<h2>Copyright</h2>


