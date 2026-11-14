---
title: "fccachecopyset(3)"
name: "fccachecopyset"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccachecopyset/"
description: "FcCacheCopySet – Returns a copy of the fontset from cache"
---

<p>FcCacheCopySet &#8211; Returns a copy of the fontset from cache </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcFontSet * FcCacheCopySet (const FcCache *</code><i>cache</i><code>); </code></p>
<h2>Description</h2>
<p>The returned fontset contains each of the font patterns from <i>cache</i>. This fontset may be modified, but the patterns from the cache are read-only.</p>
