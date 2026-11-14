---
title: "fcconfigbuildfonts(3)"
name: "fcconfigbuildfonts"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigbuildfonts/"
description: "FcConfigBuildFonts – Build font database"
---

<p>FcConfigBuildFonts &#8211; Build font database </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigBuildFonts (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Builds the set of available fonts for the given configuration. Note that any changes to the configuration after this call have indeterminate effects. Returns FcFalse if this operation runs out of memory. If <i>config</i> is NULL, the current configuration is used.</p>
