---
title: "ata_id_string(9)"
name: "ata_id_string"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_id_string/"
description: "ata_id_string – Convert IDENTIFY DEVICE page into string"
---

<p>ata_id_string &#8211; Convert IDENTIFY DEVICE page into string</p>
<h2>Synopsis</h2>
<pre><code>void ata_id_string(const u16 *id, unsigned char *s, unsigned int ofs, unsigned int len);</code></pre>
<h2>Arguments</h2>
<p><i>id</i></p>
<dl>
<dd>
<dd>IDENTIFY DEVICE results we will examine</dl>
<p> <i>s</i></p>
<dl>
<dd>string into which data is output</dl>
<p> <i>ofs</i></p>
<dl>
<dd>offset into identify device page</dl>
<p> <i>len</i></p>
<dl>
<dd>length of string to return. must be an even number.</dl>
<h2>Description</h2>
<p>The strings in the IDENTIFY DEVICE page are broken up into 16-bit chunks. Run through the string, and output each 8-bit chunk linearly, regardless of platform. </p>
<p> LOCKING: caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
