---
title: "sk_page_frag(9)"
name: "sk_page_frag"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sk_page_frag/"
---

sk_page_frag - return an appropriate page_frag

<h2>Synopsis</h2>

<pre><code>struct page_frag *sk_page_frag(struct sock *sk);</code></pre>

<h2>Arguments</h2>

<i>sk</i>
<dl><dd><dd>socket</dl>

<h2>Description</h2>

If socket allocation mode allows current thread to sleep, it means its safe to use the per task page_frag instead of the per socket one.

<h2>Copyright</h2>


