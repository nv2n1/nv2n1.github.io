---
title: "fcconfiggetrescaninterval(3)"
name: "fcconfiggetrescaninterval"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfiggetrescaninterval/"
description: "FcConfigGetRescanInterval – Get config rescan interval"
---

<p>FcConfigGetRescanInterval &#8211; Get config rescan interval </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> int FcConfigGetRescanInterval (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the interval between automatic checks of the configuration (in seconds) specified in <i>config</i>. The configuration is checked during a call to FcFontList when this interval has passed since the last check. An interval setting of zero disables automatic checks. If <i>config</i> is NULL, the current configuration is used.</p>
