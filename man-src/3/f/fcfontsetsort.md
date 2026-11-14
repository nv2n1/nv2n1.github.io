---
title: "fcfontsetsort(3)"
name: "fcfontsetsort"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfontsetsort/"
description: "FcFontSetSort – Add to a font set"
---

<p>FcFontSetSort &#8211; Add to a font set </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcFontSetSort (FcConfig *</code><i>config</i><code>, FcFontSet **</code><i>sets</i><code>, int</code><i>nsets</i><code>, FcPattern *</code><i>pattern</i><code>, FcBool </code><i>trim</i><code>, FcCharSet **</code><i>csp</i><code>, FcResult *</code><i>result</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the list of fonts from <i>sets</i> sorted by closeness to <i>pattern</i>. If <i>trim</i> is FcTrue, elements in the list which don&#8217;t include Unicode coverage not provided by earlier elements in the list are elided. The union of Unicode coverage of all of the fonts is returned in <i>csp</i>, if <i>csp</i> is not NULL. This function should be called only after FcConfigSubstitute and FcDefaultSubstitute have been called for <i>p</i>; otherwise the results will not be correct. </p>
<p> The returned FcFontSet references FcPattern structures which may be shared by the return value from multiple FcFontSort calls, applications cannot modify these patterns. Instead, they should be passed, along with <i>pattern</i> to <code>FcFontRenderPrepare</code> which combines them into a complete pattern. </p>
<p> The FcFontSet returned by FcFontSetSort is destroyed by calling FcFontSetDestroy.</p>
