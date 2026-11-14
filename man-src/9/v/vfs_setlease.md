---
title: "vfs_setlease(9)"
name: "vfs_setlease"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vfs_setlease/"
---

vfs_setlease - sets a lease on an open file

<h2>Synopsis</h2>

<pre><code>int vfs_setlease(struct file *filp, long arg, struct file_lock **lease, void **priv);</code></pre>

<h2>Arguments</h2>

<i>filp</i>
<dl><dd><dd>file pointer</dl>
 

 <i>arg</i>
<dl><dd>type of lease to obtain</dl>
 

 <i>lease</i>
<dl><dd>file_lock to use when adding a lease</dl>
 

 <i>priv</i>
<dl><dd>private info for lm_setup when adding a lease (may be NULL if lm_setup doesn't require it)</dl>

<h2>Description</h2>

Call this to establish a lease on the file. The "lease" argument is not used for F_UNLCK requests and may be NULL. For commands that set or alter an existing lease, the (*lease)-&gt;fl_lmops-&gt;lm_break operation must be set; if not, this function will return -ENOLCK (and generate a scary-looking stack trace). 

 The "priv" pointer is passed directly to the lm_setup function as-is. It may be NULL if the lm_setup operation doesn't require it.

<h2>Copyright</h2>


