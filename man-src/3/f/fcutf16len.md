---
title: "fcutf16len(3)"
name: "fcutf16len"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcutf16len/"
description: "FcUtf16Len – count UTF-16 encoded chars"
---

<p>FcUtf16Len &#8211; count UTF-16 encoded chars </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcUtf16Len (FcChar8 *</code><i>src</i><code>, FcEndian </code><i>endian</i><code>, int </code><i>len</i><code>, int *</code><i>nchar</i><code>, int *</code><i>wchar</i><code>); </code></p>
<h2>Description</h2>
<p>Counts the number of Unicode chars in <i>len</i> bytes of <i>src</i>. Bytes of <i>src</i> are combined into 16-bit units according to <i>endian</i>. Places that count in <i>nchar</i>. <i>wchar</i> contains 1, 2 or 4 depending on the number of bytes needed to hold the largest Unicode char counted. The return value indicates whether <i>string</i> is a well-formed UTF16 string.</p>
