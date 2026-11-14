---
title: "airq_iv_scan(9)"
name: "airq_iv_scan"
section: "9"
letter: "a"
url: "/docs/linux/man/9-airq_iv_scan/"
description: "airq_iv_scan – scan interrupt vector for non-zero bits"
---

<p>airq_iv_scan &#8211; scan interrupt vector for non-zero bits</p>
<h2>Synopsis</h2>
<pre><code>unsigned long airq_iv_scan(struct airq_iv *iv, unsigned long start, unsigned long end);</code></pre>
<h2>Arguments</h2>
<p><i>iv</i></p>
<dl>
<dd>
<dd>pointer to interrupt vector structure</dl>
<p> <i>start</i></p>
<dl>
<dd>bit number to start the search</dl>
<p> <i>end</i></p>
<dl>
<dd>bit number to end the search</dl>
<h2>Description</h2>
<p>Returns the bit number of the next non-zero interrupt bit, or -1UL if the scan completed without finding any more any non-zero bits.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
