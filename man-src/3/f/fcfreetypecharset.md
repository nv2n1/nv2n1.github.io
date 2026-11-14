---
title: "fcfreetypecharset(3)"
name: "fcfreetypecharset"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfreetypecharset/"
description: "FcFreeTypeCharSet – compute Unicode coverage"
---

<p>FcFreeTypeCharSet &#8211; compute Unicode coverage </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig.h&gt; #include &lt;fcfreetype.h&gt; </p>
<p> FcCharSet * FcFreeTypeCharSet (FT_Face </code><i>face</i><code>, FcBlanks *</code><i>blanks</i><code>); </code></p>
<h2>Description</h2>
<p>Scans a FreeType face and returns the set of encoded Unicode chars. FcBlanks is deprecated, <i>blanks</i> is ignored and accepted only for compatibility with older code.</p>
