---
title: "ata_id_c_string(9)"
name: "ata_id_c_string"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_id_c_string/"
description: "ata_id_c_string – Convert IDENTIFY DEVICE page into C string"
---

<p>ata_id_c_string &#8211; Convert IDENTIFY DEVICE page into C string</p>
<h2>Synopsis</h2>
<pre><code>void ata_id_c_string(const u16 *id, unsigned char *s, unsigned int ofs, unsigned int len);</code></pre>
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
<dd>length of string to return. must be an odd number.</dl>
<h2>Description</h2>
<p>This function is identical to ata_id_string except that it trims trailing spaces and terminates the resulting string with null. <i>len</i> must be actual maximum length (even number) + 1. </p>
<p> LOCKING: caller.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
