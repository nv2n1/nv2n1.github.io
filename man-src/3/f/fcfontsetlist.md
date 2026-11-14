---
title: "fcfontsetlist(3)"
name: "fcfontsetlist"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfontsetlist/"
description: "FcFontSetList – List fonts from a set of font sets"
---

<p>FcFontSetList &#8211; List fonts from a set of font sets </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcFontSet * FcFontSetList (FcConfig *</code><i>config</i><code>, FcFontSet **</code><i>sets</i><code>, int</code><i>nsets</i><code>, FcPattern *</code><i>pattern</i><code>, FcObjectSet *</code><i>object_set</i><code>); </code></p>
<h2>Description</h2>
<p>Selects fonts matching <i>pattern</i> from <i>sets</i>, creates patterns from those fonts containing only the objects in <i>object_set</i> and returns the set of unique such patterns. If <i>config</i> is NULL, the default configuration is checked to be up to date, and used.</p>
