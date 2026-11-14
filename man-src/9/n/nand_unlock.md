---
title: "nand_unlock(9)"
name: "nand_unlock"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_unlock/"
description: "nand_unlock – [REPLACEABLE] unlocks specified locked blocks"
---

<p>nand_unlock &#8211; [REPLACEABLE] unlocks specified locked blocks</p>
<h2>Synopsis</h2>
<pre><code>int nand_unlock(struct mtd_info *mtd, loff_t ofs, uint64_t len);</code></pre>
<h2>Arguments</h2>
<p><i>mtd</i></p>
<dl>
<dd>
<dd>mtd info</dl>
<p> <i>ofs</i></p>
<dl>
<dd>offset to start unlock from</dl>
<p> <i>len</i></p>
<dl>
<dd>length to unlock</dl>
<h2>Description</h2>
<p>Returns unlock status.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
