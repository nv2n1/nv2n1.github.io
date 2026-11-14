---
title: "fcconfigsetsysroot(3)"
name: "fcconfigsetsysroot"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigsetsysroot/"
description: "FcConfigSetSysRoot – Set the system root directory"
---

<p>FcConfigSetSysRoot &#8211; Set the system root directory </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcConfigSetSysRoot (FcConfig *</code><i>config</i><code>, const FcChar8 *</code><i>sysroot</i><code>); </code></p>
<h2>Description</h2>
<p>Set &#8216;sysroot&#8217; as the system root directory. fontconfig prepend &#8216;sysroot&#8217; to the cache directories in order to allow people to generate caches at the build time. Note that this causes changing current config. i.e. this function calls FcConfigSetCurrent() internally.</p>
<h2>Since</h2>
<p>version 2.10.92</p>
