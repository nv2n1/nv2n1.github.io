---
title: "eventfd_ctx_read(9)"
name: "eventfd_ctx_read"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eventfd_ctx_read/"
description: "eventfd_ctx_read – Reads the eventfd counter or wait if it is zero."
---

<p>eventfd_ctx_read &#8211; Reads the eventfd counter or wait if it is zero.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t eventfd_ctx_read(struct eventfd_ctx&nbsp;<wbr>*&nbsp;<wbr></code><i>ctx</i><code>, int&nbsp;<wbr></code><i>no_wait</i><code>, __u64&nbsp;<wbr>*&nbsp;<wbr></code><i>cnt</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>ctx</i></p>
<dl>
<dd>[in] Pointer to eventfd context.</dl>
<p> <i>no_wait</i></p>
<dl>
<dd>[in] Different from zero if the operation should not block.</dl>
<p> <i>cnt</i></p>
<dl>
<dd>[out] Pointer to the 64-bit counter value.</dl>
<h2>Description</h2>
<dd>Returns <code>0</code> if successful, or the following error codes: </p>
<p> -EAGAIN : The operation would have blocked but <i>no_wait</i> was non-zero. -ERESTARTSYS : A signal interrupted the wait operation. </p>
<p> If <i>no_wait</i> is zero, the function might sleep until the eventfd internal counter becomes greater than zero.</p>
<h2>Copyright</h2>
