---
title: "eventfd_ctx_remove_wait_queue(9)"
name: "eventfd_ctx_remove_wait_queue"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eventfd_ctx_remove_wait_queue/"
description: "eventfd_ctx_remove_wait_queue – Read the current counter and removes wait queue."
---

<p>eventfd_ctx_remove_wait_queue &#8211; Read the current counter and removes wait queue.</p>
<h2>Synopsis</h2>
<pre><code>int eventfd_ctx_remove_wait_queue(struct eventfd_ctx *ctx, wait_queue_t *wait, __u64 *cnt);</code></pre>
<h2>Arguments</h2>
<p><i>ctx</i></p>
<dl>
<dd>[in] Pointer to eventfd context.</dl>
<p> <i>wait</i></p>
<dl>
<dd>[in] Wait queue to be removed.</dl>
<p> <i>cnt</i></p>
<dl>
<dd>[out] Pointer to the 64-bit counter value.</dl>
<h2>Description</h2>
<dd>Returns <code>0</code> if successful, or the following error codes: </p>
<p> -EAGAIN : The operation would have blocked. </p>
<p> This is used to atomically remove a wait queue entry from the eventfd wait queue head, and read/reset the counter value.</p>
<h2>Copyright</h2>
