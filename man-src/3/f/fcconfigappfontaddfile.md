---
title: "fcconfigappfontaddfile(3)"
name: "fcconfigappfontaddfile"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigappfontaddfile/"
description: "FcConfigAppFontAddFile – Add font file to font database"
---

<p>FcConfigAppFontAddFile &#8211; Add font file to font database </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigAppFontAddFile (FcConfig *</code><i>config</i><code>, const FcChar8 *</code><i>file</i><code>); </code></p>
<h2>Description</h2>
<p>Adds an application-specific font to the configuration. Returns FcFalse if the fonts cannot be added (due to allocation failure or no fonts found). Otherwise returns FcTrue. If <i>config</i> is NULL, the current configuration is used.</p>
