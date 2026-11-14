---
title: "eventfd_signal(9)"
name: "eventfd_signal"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eventfd_signal/"
description: "eventfd_signal – Adds n to the eventfd counter."
---

<p>eventfd_signal &#8211; Adds <i>n</i> to the eventfd counter.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>__u64 eventfd_signal(struct eventfd_ctx&nbsp;<wbr>*&nbsp;<wbr></code><i>ctx</i><code>, __u64&nbsp;<wbr></code><i>n</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>ctx</i></p>
<dl>
<dd>[in] Pointer to the eventfd context.</dl>
<p> <i>n</i></p>
<dl>
<dd>[in] Value of the counter to be added to the eventfd internal counter. The value cannot be negative.</dl>
<h2>Description</h2>
<dd>This function is supposed to be called by the kernel in paths that do not allow sleeping. In this function we allow the counter to reach the ULLONG_MAX value, and we signal this as overflow condition by returning a POLLERR to <a href="/docs/linux/man/2-poll/">poll</a>(2). </p>
<p> Returns the amount by which the counter was incremented. This will be less than <i>n</i> if the counter has overflowed.</p>
<h2>Copyright</h2>
