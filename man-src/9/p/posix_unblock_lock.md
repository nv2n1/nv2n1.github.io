---
title: "posix_unblock_lock(9)"
name: "posix_unblock_lock"
section: "9"
letter: "p"
url: "/docs/linux/man/9-posix_unblock_lock/"
---

posix_unblock_lock - stop waiting for a file lock

<h2>Synopsis</h2>

<pre><code>int posix_unblock_lock(struct file_lock *waiter);</code></pre>

<h2>Arguments</h2>

<i>waiter</i>
<dl><dd><dd>the lock which was waiting</dl>

<h2>Description</h2>

lockd needs to block waiting for locks.

<h2>Copyright</h2>


