---
title: "bitmap_print_to_pagebuf(9)"
name: "bitmap_print_to_pagebuf"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_print_to_pagebuf/"
description: "bitmap_print_to_pagebuf – convert bitmap to list or hex format ASCII string"
---

<p>bitmap_print_to_pagebuf &#8211; convert bitmap to list or hex format ASCII string</p>
<h2>Synopsis</h2>
<pre><code>int bitmap_print_to_pagebuf(bool list, char *buf, const unsigned long *maskp, int nmaskbits);</code></pre>
<h2>Arguments</h2>
<p><i>list</i></p>
<dl>
<dd>
<dd>indicates whether the bitmap must be list</dl>
<p> <i>buf</i></p>
<dl>
<dd>page aligned buffer into which string is placed</dl>
<p> <i>maskp</i></p>
<dl>
<dd>pointer to bitmap to convert</dl>
<p> <i>nmaskbits</i></p>
<dl>
<dd>size of bitmap, in bits</dl>
<h2>Description</h2>
<p>Output format is a comma-separated list of decimal numbers and ranges if list is specified or hex digits grouped into comma-separated sets of 8 digits/set. Returns the number of characters written to buf. </p>
<p> It is assumed that <i>buf</i> is a pointer into a PAGE_SIZE area and that sufficient storage remains at <i>buf</i> to accommodate the <code>bitmap_print_to_pagebuf</code> output.</p>
<h2>Copyright</h2>
