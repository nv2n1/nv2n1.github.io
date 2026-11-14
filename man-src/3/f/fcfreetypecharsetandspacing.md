---
title: "fcfreetypecharsetandspacing(3)"
name: "fcfreetypecharsetandspacing"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfreetypecharsetandspacing/"
description: "FcFreeTypeCharSetAndSpacing – compute Unicode coverage and spacing type"
---

<p>FcFreeTypeCharSetAndSpacing &#8211; compute Unicode coverage and spacing type </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig.h&gt; #include &lt;fcfreetype.h&gt; </p>
<p> FcCharSet * FcFreeTypeCharSetAndSpacing (FT_Face </code><i>face</i><code>, FcBlanks *</code><i>blanks</i><code>, int *</code><i>spacing</i><code>); </code></p>
<h2>Description</h2>
<p>Scans a FreeType face and returns the set of encoded Unicode chars. FcBlanks is deprecated, <i>blanks</i> is ignored and accepted only for compatibility with older code. <i>spacing</i> receives the computed spacing type of the font, one of FC_MONO for a font where all glyphs have the same width, FC_DUAL, where the font has glyphs in precisely two widths, one twice as wide as the other, or FC_PROPORTIONAL where the font has glyphs of many widths.</p>
