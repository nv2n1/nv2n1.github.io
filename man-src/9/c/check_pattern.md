---
title: "check_pattern(9)"
name: "check_pattern"
section: "9"
letter: "c"
url: "/docs/linux/man/9-check_pattern/"
description: "check_pattern – [GENERIC] check if a pattern is in the buffer"
---

<p>check_pattern &#8211; [GENERIC] check if a pattern is in the buffer</p>
<h2>Synopsis</h2>
<pre><code>int check_pattern(uint8_t *buf, int len, int paglen, struct nand_bbt_descr *td);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>the buffer to search</dl>
<p> <i>len</i></p>
<dl>
<dd>the length of buffer to search</dl>
<p> <i>paglen</i></p>
<dl>
<dd>the pagelength</dl>
<p> <i>td</i></p>
<dl>
<dd>search pattern descriptor</dl>
<h2>Description</h2>
<p>Check for a pattern at the given place. Used to search bad block tables and good / bad block identifiers.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
