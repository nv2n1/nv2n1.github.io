---
title: "fcfreetypecharindex(3)"
name: "fcfreetypecharindex"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfreetypecharindex/"
description: "FcFreeTypeCharIndex – map Unicode to glyph id"
---

<p>FcFreeTypeCharIndex &#8211; map Unicode to glyph id </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig.h&gt; #include &lt;fcfreetype.h&gt; </p>
<p> FT_UInt FcFreeTypeCharIndex (FT_Face </code><i>face</i><code>, FcChar32 </code><i>ucs4</i><code>); </code></p>
<h2>Description</h2>
<p>Maps a Unicode char to a glyph index. This function uses information from several possible underlying encoding tables to work around broken fonts. As a result, this function isn&#8217;t designed to be used in performance sensitive areas; results from this function are intended to be cached by higher level functions.</p>
