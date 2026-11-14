---
title: "fcpatternremove(3)"
name: "fcpatternremove"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternremove/"
description: "FcPatternRemove – Remove one object of the specified type from the pattern"
---

<p>FcPatternRemove &#8211; Remove one object of the specified type from the pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternRemove (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>id</i><code>); </code></p>
<h2>Description</h2>
<p>Removes the value associated with the property `object&#8217; at position `id&#8217;, returning whether the property existed and had a value at that position or not.</p>
