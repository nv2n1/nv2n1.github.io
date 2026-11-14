---
title: "fcntl_getlease(9)"
name: "fcntl_getlease"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fcntl_getlease/"
description: "fcntl_getlease – Enquire what lease is currently active"
---

<p>fcntl_getlease &#8211; Enquire what lease is currently active</p>
<h2>Synopsis</h2>
<pre><code>int fcntl_getlease(struct file *filp);</code></pre>
<h2>Arguments</h2>
<p><i>filp</i></p>
<dl>
<dd>
<dd>the file</dl>
<h2>Description</h2>
<p>The value returned by this function will be one of (if no lease break is pending): </p>
<p> <code>F_RDLCK</code> to indicate a shared lease is held. </p>
<p> <code>F_WRLCK</code> to indicate an exclusive lease is held. </p>
<p> <code>F_UNLCK</code> to indicate no lease is held. </p>
<p> (if a lease break is pending): </p>
<p> <code>F_RDLCK</code> to indicate an exclusive lease needs to be changed to a shared lease (or removed). </p>
<p> <code>F_UNLCK</code> to indicate the lease needs to be removed. </p>
<p> XXX: sfr &amp; willy disagree over whether F_INPROGRESS should be returned to userspace.</p>
<h2>Copyright</h2>
