---
title: "kgdb_skipexception(9)"
name: "kgdb_skipexception"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kgdb_skipexception/"
description: "kgdb_skipexception – (optional) exit kgdb_handle_exception early"
---

<p>kgdb_skipexception &#8211; (optional) exit kgdb_handle_exception early</p>
<h2>Synopsis</h2>
<pre><code>int kgdb_skipexception(int exception, struct pt_regs *regs);</code></pre>
<h2>Arguments</h2>
<p><i>exception</i></p>
<dl>
<dd>
<dd>Exception vector number</dl>
<p> <i>regs</i></p>
<dl>
<dd>Current struct pt_regs.</dl>
<h2>Description</h2>
<p>On some architectures it is required to skip a breakpoint exception when it occurs after a breakpoint has been removed. This can be implemented in the architecture specific portion of kgdb.</p>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
