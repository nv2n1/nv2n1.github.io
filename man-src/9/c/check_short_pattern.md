---
title: "check_short_pattern(9)"
name: "check_short_pattern"
section: "9"
letter: "c"
url: "/docs/linux/man/9-check_short_pattern/"
description: "check_short_pattern – [GENERIC] check if a pattern is in the buffer"
---

<p>check_short_pattern &#8211; [GENERIC] check if a pattern is in the buffer</p>
<h2>Synopsis</h2>
<pre><code>int check_short_pattern(uint8_t *buf, struct nand_bbt_descr *td);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>the buffer to search</dl>
<p> <i>td</i></p>
<dl>
<dd>search pattern descriptor</dl>
<h2>Description</h2>
<p>Check for a pattern at the given place. Used to search bad block tables and good / bad block identifiers. Same as check_pattern, but no optional empty check.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
