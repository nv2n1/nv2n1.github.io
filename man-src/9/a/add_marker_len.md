---
title: "add_marker_len(9)"
name: "add_marker_len"
section: "9"
letter: "a"
url: "/docs/linux/man/9-add_marker_len/"
description: "add_marker_len – compute the length of the marker in data area"
---

<p>add_marker_len &#8211; compute the length of the marker in data area</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u32 add_marker_len(struct nand_bbt_descr&nbsp;<wbr>*&nbsp;<wbr></code><i>td</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>td</i></p>
<dl>
<dd>
<dd>BBT descriptor used for computation</dl>
<h2>Description</h2>
<p>The length will be 0 if the marker is located in OOB area.</p>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
