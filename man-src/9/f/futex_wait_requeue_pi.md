---
title: "futex_wait_requeue_pi(9)"
name: "futex_wait_requeue_pi"
section: "9"
letter: "f"
url: "/docs/linux/man/9-futex_wait_requeue_pi/"
description: "futex_wait_requeue_pi – Wait on uaddr and take uaddr2"
---

<p>futex_wait_requeue_pi &#8211; Wait on uaddr and take uaddr2</p>
<h2>Synopsis</h2>
<pre><code>int futex_wait_requeue_pi(u32 __user *uaddr, unsigned int flags, u32 val, ktime_t *abs_time, u32 bitset, u32 __user *uaddr2);</code></pre>
<h2>Arguments</h2>
<p><i>uaddr</i></p>
<dl>
<dd>
<dd>the futex we initially wait on (non-pi)</dl>
<p> <i>flags</i></p>
<dl>
<dd>futex flags (FLAGS_SHARED, FLAGS_CLOCKRT, etc.), they must be the same type, no requeueing from private to shared, etc.</dl>
<p> <i>val</i></p>
<dl>
<dd>the expected value of uaddr</dl>
<p> <i>abs_time</i></p>
<dl>
<dd>absolute timeout</dl>
<p> <i>bitset</i></p>
<dl>
<dd>32 bit wakeup bitset set by userspace, defaults to all</dl>
<p> <i>uaddr2</i></p>
<dl>
<dd>the pi futex we will take prior to returning to user-space</dl>
<h2>Description</h2>
<p>The caller will wait on uaddr and will be requeued by <code>futex_requeue</code> to uaddr2 which must be PI aware and unique from uaddr. Normal wakeup will wake on uaddr2 and complete the acquisition of the rt_mutex prior to returning to userspace. This ensures the rt_mutex maintains an owner when it has waiters; without one, the pi logic would not know which task to boost/deboost, if there was a need to. </p>
<p> We call schedule in <code>futex_wait_queue_me</code> when we enqueue and return there via the following&#8211; 1) wakeup on uaddr2 after an atomic lock acquisition by <code>futex_requeue</code> 2) wakeup on uaddr2 after a requeue 3) signal 4) timeout </p>
<p> If 3, cleanup and return -ERESTARTNOINTR. </p>
<p> If 2, we may then block on trying to take the rt_mutex and return via: 5) successful lock 6) signal 7) timeout 8) other lock acquisition failure </p>
<p> If 6, return -EWOULDBLOCK (restarting the syscall would do the same). </p>
<p> If 4 or 7, we cleanup and return with -ETIMEDOUT.</p>
<h2>Return</h2>
<p>0 &#8211; On success; &lt;0 &#8211; On error</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
