---
title: "crc_itu_t(9)"
name: "crc_itu_t"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crc_itu_t/"
description: "crc_itu_t – Compute the CRC-ITU-T for the data buffer"
---

<p>crc_itu_t &#8211; Compute the CRC-ITU-T for the data buffer</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u16 crc_itu_t(u16&nbsp;<wbr></code><i>crc</i><code>, const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>crc</i></p>
<dl>
<dd>
<dd>previous CRC value</dl>
<p> <i>buffer</i></p>
<dl>
<dd>data pointer</dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes in the buffer</dl>
<h2>Description</h2>
<p>Returns the updated CRC value</p>
<h2>Copyright</h2>
