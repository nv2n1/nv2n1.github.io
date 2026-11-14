---
title: "fcconfigdestroy(3)"
name: "fcconfigdestroy"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigdestroy/"
description: "FcConfigDestroy – Destroy a configuration"
---

<p>FcConfigDestroy &#8211; Destroy a configuration </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcConfigDestroy (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Decrements the config reference count. If all references are gone, destroys the configuration and any data associated with it. Note that calling this function with the return from FcConfigGetCurrent will cause a new configuration to be created for use as current configuration.</p>
