---
title: "w1_triplet(9)"
name: "w1_triplet"
section: "9"
letter: "w"
url: "/docs/linux/man/9-w1_triplet/"
description: "w1_triplet – * Does a triplet – used for searching ROM addresses."
---

<p>w1_triplet &#8211; * Does a triplet &#8211; used for searching ROM addresses.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 w1_triplet(struct w1_master&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, int&nbsp;<wbr></code><i>bdir</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the master device</dl>
<p> <i>bdir</i></p>
<dl>
<dd>the bit to write if both id_bit and comp_bit are 0</dl>
<h2>Description</h2>
<p>Return bits: bit 0 = id_bit bit 1 = comp_bit bit 2 = dir_taken If both bits 0 &amp; 1 are set, the search should be restarted.</p>
<h2>Return</h2>
<p>bit fields &#8211; see above</p>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
