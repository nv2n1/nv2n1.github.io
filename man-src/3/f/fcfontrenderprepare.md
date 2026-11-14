---
title: "fcfontrenderprepare(3)"
name: "fcfontrenderprepare"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfontrenderprepare/"
description: "FcFontRenderPrepare – Prepare pattern for loading font file"
---

<p>FcFontRenderPrepare &#8211; Prepare pattern for loading font file </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcPattern * FcFontRenderPrepare (FcConfig *</code><i>config</i><code>, FcPattern *</code><i>pat</i><code>, FcPattern *</code><i>font</i><code>); </code></p>
<h2>Description</h2>
<p>Creates a new pattern consisting of elements of <i>font</i> not appearing in <i>pat</i>, elements of <i>pat</i> not appearing in <i>font</i> and the best matching value from <i>pat</i> for elements appearing in both. The result is passed to FcConfigSubstituteWithPat with <i>kind</i> FcMatchFont and then returned.</p>
