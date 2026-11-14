---
title: "fcconfigreference(3)"
name: "fcconfigreference"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigreference/"
description: "FcConfigReference – Increment config reference count"
---

<p>FcConfigReference &#8211; Increment config reference count </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcConfig * FcConfigReference (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Add another reference to <i>config</i>. Configs are freed only when the reference count reaches zero. If <i>config</i> is NULL, the current configuration is used. In that case this function will be similar to FcConfigGetCurrent() except that it increments the reference count before returning and the user is responsible for destroying the configuration when not needed anymore.</p>
