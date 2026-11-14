---
title: "fcconfiggetconfigdirs(3)"
name: "fcconfiggetconfigdirs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfiggetconfigdirs/"
description: "FcConfigGetConfigDirs – Get config directories"
---

<p>FcConfigGetConfigDirs &#8211; Get config directories </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcStrList * FcConfigGetConfigDirs (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the list of font directories specified in the configuration files for <i>config</i>. Does not include any subdirectories. If <i>config</i> is NULL, the current configuration is used.</p>
