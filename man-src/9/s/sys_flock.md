---
title: "sys_flock(9)"
name: "sys_flock"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sys_flock/"
description: "sys_flock – flock system call."
---

<p>sys_flock &#8211; <code>flock</code> system call.</p>
<h2>Synopsis</h2>
<pre><code>long sys_flock(unsigned int fd, unsigned int cmd);</code></pre>
<h2>Arguments</h2>
<p><i>fd</i></p>
<dl>
<dd>
<dd>the file descriptor to lock.</dl>
<p> <i>cmd</i></p>
<dl>
<dd>the type of lock to apply.</dl>
<h2>Description</h2>
<p>Apply a <code>FL_FLOCK</code> style lock to an open file descriptor. The <i>cmd</i> can be one of </p>
<p> <code>LOCK_SH</code> &#8212; a shared lock. </p>
<p> <code>LOCK_EX</code> &#8212; an exclusive lock. </p>
<p> <code>LOCK_UN</code> &#8212; remove an existing lock. </p>
<p> <code>LOCK_MAND</code> &#8212; a `mandatory&#8217; flock. This exists to emulate Windows Share Modes. </p>
<p> <code>LOCK_MAND</code> can be combined with <code>LOCK_READ</code> or <code>LOCK_WRITE</code> to allow other processes read and write access respectively.</p>
<h2>Copyright</h2>
