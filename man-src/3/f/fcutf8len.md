---
title: "fcutf8len(3)"
name: "fcutf8len"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcutf8len/"
description: "FcUtf8Len – count UTF-8 encoded chars"
---

<p>FcUtf8Len &#8211; count UTF-8 encoded chars </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcUtf8Len (FcChar8 *</code><i>src</i><code>, int </code><i>len</i><code>, int *</code><i>nchar</i><code>, int *</code><i>wchar</i><code>); </code></p>
<h2>Description</h2>
<p>Counts the number of Unicode chars in <i>len</i> bytes of <i>src</i>. Places that count in <i>nchar</i>. <i>wchar</i> contains 1, 2 or 4 depending on the number of bytes needed to hold the largest Unicode char counted. The return value indicates whether <i>src</i> is a well-formed UTF8 string.</p>
