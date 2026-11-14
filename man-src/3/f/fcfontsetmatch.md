---
title: "fcfontsetmatch(3)"
name: "fcfontsetmatch"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfontsetmatch/"
description: "FcFontSetMatch – Return the best font from a set of font sets"
---

<p>FcFontSetMatch &#8211; Return the best font from a set of font sets </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcPattern * FcFontSetMatch (FcConfig *</code><i>config</i><code>, FcFontSet **</code><i>sets</i><code>, int</code><i>nsets</i><code>, FcPattern *</code><i>pattern</i><code>, FcResult *</code><i>result</i><code>); </code></p>
<h2>Description</h2>
<p>Finds the font in <i>sets</i> most closely matching <i>pattern</i> and returns the result of <code>FcFontRenderPrepare</code> for that font and the provided pattern. This function should be called only after <code>FcConfigSubstitute</code> and <code>FcDefaultSubstitute</code> have been called for <i>pattern</i>; otherwise the results will not be correct. If <i>config</i> is NULL, the current configuration is used. Returns NULL if an error occurs during this process.</p>
