---
title: "fcconfigappfontclear(3)"
name: "fcconfigappfontclear"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigappfontclear/"
description: "FcConfigAppFontClear – Remove all app fonts from font database"
---

<p>FcConfigAppFontClear &#8211; Remove all app fonts from font database </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcConfigAppFontClear (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Clears the set of application-specific fonts. If <i>config</i> is NULL, the current configuration is used.</p>
