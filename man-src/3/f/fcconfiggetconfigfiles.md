---
title: "fcconfiggetconfigfiles(3)"
name: "fcconfiggetconfigfiles"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfiggetconfigfiles/"
description: "FcConfigGetConfigFiles – Get config files"
---

<p>FcConfigGetConfigFiles &#8211; Get config files </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcStrList * FcConfigGetConfigFiles (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the list of known configuration files used to generate <i>config</i>. If <i>config</i> is NULL, the current configuration is used.</p>
