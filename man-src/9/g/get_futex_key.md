---
title: "get_futex_key(9)"
name: "get_futex_key"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_futex_key/"
description: "get_futex_key – Get parameters which are the keys for a futex"
---

<p>get_futex_key &#8211; Get parameters which are the keys for a futex</p>
<h2>Synopsis</h2>
<pre><code>int get_futex_key(u32 __user *uaddr, int fshared, union futex_key *key, int rw);</code></pre>
<h2>Arguments</h2>
<p><i>uaddr</i></p>
<dl>
<dd>
<dd>virtual address of the futex</dl>
<p> <i>fshared</i></p>
<dl>
<dd>0 for a PROCESS_PRIVATE futex, 1 for PROCESS_SHARED</dl>
<p> <i>key</i></p>
<dl>
<dd>address where result is stored.</dl>
<p> <i>rw</i></p>
<dl>
<dd>mapping needs to be read/write (values: VERIFY_READ, VERIFY_WRITE)</dl>
<h2>Return</h2>
<p>a negative error code or 0 </p>
<p> The key words are stored in *key on success. </p>
<p> For shared mappings, it&#8217;s (page-&gt;index, file_inode(vma-&gt;vm_file), offset_within_page). For private mappings, it&#8217;s (uaddr, current-&gt;mm). We can usually work out the index without swapping in the page. </p>
<p> <code>lock_page</code> might sleep, the caller should not hold a spinlock.</p>
<h2>Author</h2>
<p><code>Rusty Russell</code> &lt;rusty [at] rustcorp.com.au&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
