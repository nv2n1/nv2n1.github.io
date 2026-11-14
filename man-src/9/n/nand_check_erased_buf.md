---
title: "nand_check_erased_buf(9)"
name: "nand_check_erased_buf"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_check_erased_buf/"
description: "nand_check_erased_buf – check if a buffer contains (almost) only 0xff data"
---

<p>nand_check_erased_buf &#8211; check if a buffer contains (almost) only 0xff data</p>
<h2>Synopsis</h2>
<pre><code>int nand_check_erased_buf(void *buf, int len, int bitflips_threshold);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>buffer to test</dl>
<p> <i>len</i></p>
<dl>
<dd>buffer length</dl>
<p> <i>bitflips_threshold</i></p>
<dl>
<dd>maximum number of bitflips</dl>
<h2>Description</h2>
<p>Check if a buffer contains only 0xff, which means the underlying region has been erased and is ready to be programmed. The bitflips_threshold specify the maximum number of bitflips before considering the region is not erased.</p>
<h2>Note</h2>
<p>The logic of this function has been extracted from the memweight implementation, except that nand_check_erased_buf function exit before testing the whole buffer if the number of bitflips exceed the bitflips_threshold value. </p>
<p> Returns a positive number of bitflips less than or equal to bitflips_threshold, or -ERROR_CODE for bitflips in excess of the threshold.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
