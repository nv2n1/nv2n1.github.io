---
title: "fcdircachecreateuuid(3)"
name: "fcdircachecreateuuid"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcdircachecreateuuid/"
description: "FcDirCacheCreateUUID – Create .uuid file at a directory"
---

<p>FcDirCacheCreateUUID &#8211; Create .uuid file at a directory </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcDirCacheCreateUUID (FcChar8 *</code><i>dir</i><code>, FcBool</code><i>force</i><code>, FcConfig *</code><i>config</i><code>); </code></p>
<h2>Description</h2>
<p>This is to create .uuid file containing an UUID at a font directory of <i>dir</i>. The UUID will be used to identify the font directory and is used to determine the cache filename if available.</p>
<h2>Since</h2>
<p>version 2.12.92</p>
