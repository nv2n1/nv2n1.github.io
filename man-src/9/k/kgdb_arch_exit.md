---
title: "kgdb_arch_exit(9)"
name: "kgdb_arch_exit"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kgdb_arch_exit/"
description: "kgdb_arch_exit – Perform any architecture specific uninitalization."
---

<p>kgdb_arch_exit &#8211; Perform any architecture specific uninitalization.</p>
<h2>Synopsis</h2>
<pre><code>void kgdb_arch_exit(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>This function will handle the uninitalization of any architecture specific callbacks, for dynamic registration and unregistration.</p>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
