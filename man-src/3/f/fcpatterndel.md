---
title: "fcpatterndel(3)"
name: "fcpatterndel"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatterndel/"
description: "FcPatternDel – Delete a property from a pattern"
---

<p>FcPatternDel &#8211; Delete a property from a pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternDel (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>); </code></p>
<h2>Description</h2>
<p>Deletes all values associated with the property `object&#8217;, returning whether the property existed or not.</p>
