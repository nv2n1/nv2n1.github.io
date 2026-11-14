---
title: "fcconfigsetrescaninterval(3)"
name: "fcconfigsetrescaninterval"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigsetrescaninterval/"
description: "FcConfigSetRescanInterval – Set config rescan interval"
---

<p>FcConfigSetRescanInterval &#8211; Set config rescan interval </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigSetRescanInterval (FcConfig *</code><i>config</i><code>, int </code><i>rescanInterval</i><code>); </code></p>
<h2>Description</h2>
<p>Sets the rescan interval. Returns FcFalse if the interval cannot be set (due to allocation failure). Otherwise returns FcTrue. An interval setting of zero disables automatic checks. If <i>config</i> is NULL, the current configuration is used.</p>
