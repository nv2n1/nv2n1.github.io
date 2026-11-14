---
title: "fcfontsetadd(3)"
name: "fcfontsetadd"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfontsetadd/"
description: "FcFontSetAdd – Add to a font set"
---

<p>FcFontSetAdd &#8211; Add to a font set </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcFontSetAdd (FcFontSet *</code><i>s</i><code>, FcPattern *</code><i>font</i><code>); </code></p>
<h2>Description</h2>
<p>Adds a pattern to a font set. Note that the pattern is not copied before being inserted into the set. Returns FcFalse if the pattern cannot be inserted into the set (due to allocation failure). Otherwise returns FcTrue.</p>
