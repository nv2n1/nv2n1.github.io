---
title: "fcucs4toutf8(3)"
name: "fcucs4toutf8"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcucs4toutf8/"
description: "FcUcs4ToUtf8 – convert UCS4 to UTF-8"
---

<p>FcUcs4ToUtf8 &#8211; convert UCS4 to UTF-8 </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> int FcUcs4ToUtf8 (FcChar32 </code><i>src</i><code>, FcChar8 </code><i>dst[FC_UTF8_MAX_LEN]</i><code>); </code></p>
<h2>Description</h2>
<p>Converts the Unicode char from <i>src</i> into <i>dst</i> and returns the number of bytes needed to encode the char.</p>
