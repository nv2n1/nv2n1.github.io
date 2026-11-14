---
title: "fcconfiggetcache(3)"
name: "fcconfiggetcache"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfiggetcache/"
description: "FcConfigGetCache – DEPRECATED used to return per-user cache filename"
---

<p>FcConfigGetCache &#8211; DEPRECATED used to return per-user cache filename </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcConfigGetCache (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>With fontconfig no longer using per-user cache files, this function now simply returns NULL to indicate that no per-user file exists.</p>
