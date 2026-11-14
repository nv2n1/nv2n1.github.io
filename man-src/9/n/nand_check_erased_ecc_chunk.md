---
title: "nand_check_erased_ecc_chunk(9)"
name: "nand_check_erased_ecc_chunk"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nand_check_erased_ecc_chunk/"
description: "nand_check_erased_ecc_chunk – check if an ECC chunk contains (almost) only 0xff data"
---

<p>nand_check_erased_ecc_chunk &#8211; check if an ECC chunk contains (almost) only 0xff data</p>
<h2>Synopsis</h2>
<pre><code>int nand_check_erased_ecc_chunk(void *data, int datalen, void *ecc, int ecclen, void *extraoob, int extraooblen, int bitflips_threshold);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>data buffer to test</dl>
<p> <i>datalen</i></p>
<dl>
<dd>data length</dl>
<p> <i>ecc</i></p>
<dl>
<dd>ECC buffer</dl>
<p> <i>ecclen</i></p>
<dl>
<dd>ECC length</dl>
<p> <i>extraoob</i></p>
<dl>
<dd>extra OOB buffer</dl>
<p> <i>extraooblen</i></p>
<dl>
<dd>extra OOB length</dl>
<p> <i>bitflips_threshold</i></p>
<dl>
<dd>maximum number of bitflips</dl>
<h2>Description</h2>
<p>Check if a data buffer and its associated ECC and OOB data contains only 0xff pattern, which means the underlying region has been erased and is ready to be programmed. The bitflips_threshold specify the maximum number of bitflips before considering the region as not erased.</p>
<h2>Note</h2>
<p>1/ ECC algorithms are working on pre-defined block sizes which are usually different from the NAND page size. When fixing bitflips, ECC engines will report the number of errors per chunk, and the NAND core infrastructure expect you to return the maximum number of bitflips for the whole page. This is why you should always use this function on a single chunk and not on the whole page. After checking each chunk you should update your max_bitflips value accordingly. 2/ When checking for bitflips in erased pages you should not only check the payload data but also their associated ECC data, because a user might have programmed almost all bits to 1 but a few. In this case, we shouldn&#8217;t consider the chunk as erased, and checking ECC bytes prevent this case. 3/ The extraoob argument is optional, and should be used if some of your OOB data are protected by the ECC engine. It could also be used if you support subpages and want to attach some extra OOB data to an ECC chunk. </p>
<p> Returns a positive number of bitflips less than or equal to bitflips_threshold, or -ERROR_CODE for bitflips in excess of the threshold. In case of success, the passed buffers are filled with 0xff.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
