---
title: "fcconfiggetfontdirs(3)"
name: "fcconfiggetfontdirs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfiggetfontdirs/"
description: "FcConfigGetFontDirs – Get font directories"
---

<p>FcConfigGetFontDirs &#8211; Get font directories </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcStrList * FcConfigGetFontDirs (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the list of font directories in <i>config</i>. This includes the configured font directories along with any directories below those in the filesystem. If <i>config</i> is NULL, the current configuration is used.</p>
