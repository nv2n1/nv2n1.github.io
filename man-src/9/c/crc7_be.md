---
title: "crc7_be(9)"
name: "crc7_be"
section: "9"
letter: "c"
url: "/docs/linux/man/9-crc7_be/"
description: "crc7_be – update the CRC7 for the data buffer"
---

<p>crc7_be &#8211; update the CRC7 for the data buffer</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 crc7_be(u8&nbsp;<wbr></code><i>crc</i><code>, const u8&nbsp;<wbr>*&nbsp;<wbr></code><i>buffer</i><code>, size_t&nbsp;<wbr></code><i>len</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>crc</i></p>
<dl>
<dd>
<dd>previous CRC7 value</dl>
<p> <i>buffer</i></p>
<dl>
<dd>data pointer</dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes in the buffer</dl>
<h2>Context</h2>
<p>any</p>
<h2>Description</h2>
<p>Returns the updated CRC7 value. The CRC7 is left-aligned in the byte (the lsbit is always 0), as that makes the computation easier, and all callers want it in that form.</p>
<h2>Copyright</h2>
