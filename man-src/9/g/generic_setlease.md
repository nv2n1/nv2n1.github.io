---
title: "generic_setlease(9)"
name: "generic_setlease"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_setlease/"
description: "generic_setlease – sets a lease on an open file"
---

<p>generic_setlease &#8211; sets a lease on an open file</p>
<h2>Synopsis</h2>
<pre><code>int generic_setlease(struct file *filp, long arg, struct file_lock **flp, void **priv);</code></pre>
<h2>Arguments</h2>
<p><i>filp</i></p>
<dl>
<dd>
<dd>file pointer</dl>
<p> <i>arg</i></p>
<dl>
<dd>type of lease to obtain</dl>
<p> <i>flp</i></p>
<dl>
<dd>input &#8211; file_lock to use, output &#8211; file_lock inserted</dl>
<p> <i>priv</i></p>
<dl>
<dd>private data for lm_setup (may be NULL if lm_setup doesn&#8217;t require it)</dl>
<h2>Description</h2>
<p>The (input) flp-&gt;fl_lmops-&gt;lm_break function is required by <code>break_lease</code>.</p>
<h2>Copyright</h2>
