---
title: "fcntl_setlease(9)"
name: "fcntl_setlease"
section: "9"
letter: "f"
url: "/docs/linux/man/9-fcntl_setlease/"
description: "fcntl_setlease – sets a lease on an open file"
---

<p>fcntl_setlease &#8211; sets a lease on an open file</p>
<h2>Synopsis</h2>
<pre><code>int fcntl_setlease(unsigned int fd, struct file *filp, long arg);</code></pre>
<h2>Arguments</h2>
<p><i>fd</i></p>
<dl>
<dd>
<dd>open file descriptor</dl>
<p> <i>filp</i></p>
<dl>
<dd>file pointer</dl>
<p> <i>arg</i></p>
<dl>
<dd>type of lease to obtain</dl>
<h2>Description</h2>
<p>Call this fcntl to establish a lease on the file. Note that you also need to call <code>F_SETSIG</code> to receive a signal when the lease is broken.</p>
<h2>Copyright</h2>
