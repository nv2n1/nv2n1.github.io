---
title: "fcfontsetsortdestroy(3)"
name: "fcfontsetsortdestroy"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfontsetsortdestroy/"
description: "FcFontSetSortDestroy – DEPRECATED destroy a font set"
---

<p>FcFontSetSortDestroy &#8211; DEPRECATED destroy a font set </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcFontSetSortDestroy (FcFontSet *</code><i>set</i><code>); </code></p>
<h2>Description</h2>
<p>This function is DEPRECATED. <code>FcFontSetSortDestroy</code> destroys <i>set</i> by calling <code>FcFontSetDestroy</code>. Applications should use <code>FcFontSetDestroy</code> directly instead.</p>
