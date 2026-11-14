---
title: "ata_mode_string(9)"
name: "ata_mode_string"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_mode_string/"
description: "ata_mode_string – convert xfer_mask to string"
---

<p>ata_mode_string &#8211; convert xfer_mask to string</p>
<h2>Synopsis</h2>
<pre><code>const char *ata_mode_string(unsigned long xfer_mask);</code></pre>
<h2>Arguments</h2>
<p><i>xfer_mask</i></p>
<dl>
<dd>
<dd>mask of bits supported; only highest bit counts.</dl>
<h2>Description</h2>
<p>Determine string which represents the highest speed (highest bit in <i>modemask</i>). </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>Constant C string representing highest speed listed in <i>mode_mask</i>, or the constant C string &#8220;&lt;n/a&gt;&#8221;.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
