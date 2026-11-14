---
title: "nand_lock(9)"
name: "nand_lock"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_lock/"
description: "nand_lock – [REPLACEABLE] locks all blocks present in the device"
---

<p>nand_lock &#8211; [REPLACEABLE] locks all blocks present in the device</p>
<h2>Synopsis</h2>
<pre><code>int nand_lock(struct mtd_info *mtd, loff_t ofs, uint64_t len);</code></pre>
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
<p>This feature is not supported in many NAND parts. &#8216;Micron&#8217; NAND parts do have this feature, but it allows only to lock all blocks, not for specified range for block. Implementing &#8216;lock&#8217; feature by making use of &#8216;unlock&#8217;, for now. </p>
<p> Returns lock status.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
