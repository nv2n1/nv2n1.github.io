---
title: "fcobjectsetadd(3)"
name: "fcobjectsetadd"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcobjectsetadd/"
description: "FcObjectSetAdd – Add to an object set"
---

<p>FcObjectSetAdd &#8211; Add to an object set </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcObjectSetAdd (FcObjectSet *</code><i>os</i><code>, const char *</code><i>object</i><code>); </code></p>
<h2>Description</h2>
<p>Adds a property name to the set. Returns FcFalse if the property name cannot be inserted into the set (due to allocation failure). Otherwise returns FcTrue.</p>
