---
title: "kgdb_breakpoint(9)"
name: "kgdb_breakpoint"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kgdb_breakpoint/"
description: "kgdb_breakpoint – compiled in breakpoint"
---

<p>kgdb_breakpoint &#8211; compiled in breakpoint</p>
<h2>Synopsis</h2>
<pre><code>void kgdb_breakpoint(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>This will be implemented as a static inline per architecture. This function is called by the kgdb core to execute an architecture specific trap to cause kgdb to enter the exception processing.</p>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
