---
title: "struct_w1_family(9)"
name: "struct_w1_family"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_w1_family/"
description: "struct_w1_family – reference counted family structure."
---

<p>struct_w1_family &#8211; reference counted family structure.</p>
<h2>Synopsis</h2>
<pre><code>struct w1_family {
    struct list_head family_entry;
    u8 fid;
    struct w1_family_ops *fops;
    atomic_t refcnt;
};</code></pre>
<h2>Members</h2>
<p>family_entry</p>
<dl>
<dd>family linked list</dl>
<p> fid</p>
<dl>
<dd>8 bit family identifier</dl>
<p> fops</p>
<dl>
<dd>operations for this family</dl>
<p> refcnt</p>
<dl>
<dd>reference counter</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
