---
title: "fcfontlist(3)"
name: "fcfontlist"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfontlist/"
description: "FcFontList – List fonts"
---

<p>FcFontList &#8211; List fonts </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcFontSet * FcFontList (FcConfig *</code><i>config</i><code>, FcPattern *</code><i>p</i><code>, FcObjectSet *</code><i>os</i><code>); </code></p>
<h2>Description</h2>
<p>Selects fonts matching <i>p</i>, creates patterns from those fonts containing only the objects in <i>os</i> and returns the set of unique such patterns. If <i>config</i> is NULL, the default configuration is checked to be up to date, and used.</p>
