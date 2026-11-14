---
title: "crc16(9)"
name: "crc16"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crc16/"
description: "crc16 – compute the CRC-16 for the data buffer"
---

<p>crc16 &#8211; compute the CRC-16 for the data buffer</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u16 crc16(u16&nbsp;<wbr></code><i>crc</i><code>, u8 const&nbsp;<wbr>*&nbsp;<wbr></code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></dl>
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
<p>Returns the updated CRC value.</p>
<h2>Copyright</h2>
