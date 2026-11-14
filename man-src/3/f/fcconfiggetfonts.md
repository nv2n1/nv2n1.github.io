---
title: "fcconfiggetfonts(3)"
name: "fcconfiggetfonts"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfiggetfonts/"
description: "FcConfigGetFonts – Get config font set"
---

<p>FcConfigGetFonts &#8211; Get config font set </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcFontSet * FcConfigGetFonts (FcConfig *</code><i>config</i><code>, FcSetName </code><i>set</i><code>); </code></p>
<h2>Description</h2>
<p>Returns one of the two sets of fonts from the configuration as specified by <i>set</i>. This font set is owned by the library and must not be modified or freed. If <i>config</i> is NULL, the current configuration is used.</p>
