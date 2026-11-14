---
title: "struct_w1_reg_num(9)"
name: "struct_w1_reg_num"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_w1_reg_num/"
description: "struct_w1_reg_num – broken out slave device id"
---

<p>struct_w1_reg_num &#8211; broken out slave device id</p>
<h2>Synopsis</h2>
<pre><code>struct w1_reg_num {
#if defined(__LITTLE_ENDIAN_BITFIELD)
    __u64 family : 8;
    __u64 id : 48;
    __u64 crc : 8;
#elif defined(__BIG_ENDIAN_BITFIELD)
    __u64 crc : 8;
    __u64 id : 48;
    __u64 family : 8;
#else
#error &quot;Please fix &lt;asm/byteorder.h&gt;&quot;
#endif
};</code></pre>
<h2>Members</h2>
<p>family</p>
<dl>
<dd>identifies the type of device</dl>
<p> id</p>
<dl>
<dd>along with family is the unique device id</dl>
<p> crc</p>
<dl>
<dd>checksum of the other bytes</dl>
<p> crc</p>
<dl>
<dd>checksum of the other bytes</dl>
<p> id</p>
<dl>
<dd>along with family is the unique device id</dl>
<p> family</p>
<dl>
<dd>identifies the type of device</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
