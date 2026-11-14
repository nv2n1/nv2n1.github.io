---
title: "fcconfigsetcurrent(3)"
name: "fcconfigsetcurrent"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigsetcurrent/"
description: "FcConfigSetCurrent – Set configuration as default"
---

<p>FcConfigSetCurrent &#8211; Set configuration as default </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigSetCurrent (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Sets the current default configuration to <i>config</i>. Implicitly calls FcConfigBuildFonts if necessary, and FcConfigReference() to inrease the reference count in <i>config</i> since 2.12.0, returning FcFalse if that call fails.</p>
