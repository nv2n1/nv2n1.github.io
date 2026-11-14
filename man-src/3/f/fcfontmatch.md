---
title: "fcfontmatch(3)"
name: "fcfontmatch"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfontmatch/"
description: "FcFontMatch – Return best font"
---

<p>FcFontMatch &#8211; Return best font </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcPattern * FcFontMatch (FcConfig *</code><i>config</i><code>, FcPattern *</code><i>p</i><code>, FcResult *</code><i>result</i><code>); </code></p>
<h2>Description</h2>
<p>Finds the font in <i>sets</i> most closely matching <i>pattern</i> and returns the result of <code>FcFontRenderPrepare</code> for that font and the provided pattern. This function should be called only after <code>FcConfigSubstitute</code> and <code>FcDefaultSubstitute</code> have been called for <i>p</i>; otherwise the results will not be correct. If <i>config</i> is NULL, the current configuration is used.</p>
