---
title: "fcpatternget(3)"
name: "fcpatternget"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternget/"
description: "FcPatternGet – Return a value from a pattern"
---

<p>FcPatternGet &#8211; Return a value from a pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcResult FcPatternGet (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>id</i><code>, FcValue *</code><i>v</i><code>); </code></p>
<h2>Description</h2>
<p>Returns in <i>v</i> the <i>id</i>&#8216;th value associated with the property <i>object</i>. The value returned is not a copy, but rather refers to the data stored within the pattern directly. Applications must not free this value.</p>
