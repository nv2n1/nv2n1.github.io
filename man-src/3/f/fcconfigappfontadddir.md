---
title: "fcconfigappfontadddir(3)"
name: "fcconfigappfontadddir"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigappfontadddir/"
description: "FcConfigAppFontAddDir – Add fonts from directory to font database"
---

<p>FcConfigAppFontAddDir &#8211; Add fonts from directory to font database </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigAppFontAddDir (FcConfig *</code><i>config</i><code>, const FcChar8 *</code><i>dir</i><code>); </code></p>
<h2>Description</h2>
<p>Scans the specified directory for fonts, adding each one found to the application-specific set of fonts. Returns FcFalse if the fonts cannot be added (due to allocation failure). Otherwise returns FcTrue. If <i>config</i> is NULL, the current configuration is used.</p>
