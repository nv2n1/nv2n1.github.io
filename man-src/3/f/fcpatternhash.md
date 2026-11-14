---
title: "fcpatternhash(3)"
name: "fcpatternhash"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternhash/"
description: "FcPatternHash – Compute a pattern hash value"
---

<p>FcPatternHash &#8211; Compute a pattern hash value </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar32 FcPatternHash (const FcPattern *</code><i>p</i><code>); </code></p>
<h2>Description</h2>
<p>Returns a 32-bit number which is the same for any two patterns which are equal.</p>
