---
title: "fcconfiguptodate(3)"
name: "fcconfiguptodate"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfiguptodate/"
description: "FcConfigUptoDate – Check timestamps on config files"
---

<p>FcConfigUptoDate &#8211; Check timestamps on config files </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigUptoDate (FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>Checks all of the files related to <i>config</i> and returns whether any of them has been modified since the configuration was created. If <i>config</i> is NULL, the current configuration is used.</p>
