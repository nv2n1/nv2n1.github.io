---
title: "fcpatterngetwithbinding(3)"
name: "fcpatterngetwithbinding"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatterngetwithbinding/"
description: "FcPatternGetWithBinding – Return a value with binding from a pattern"
---

<p>FcPatternGetWithBinding &#8211; Return a value with binding from a pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcResult FcPatternGetWithBinding (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>id</i><code>, FcValue *</code><i>v</i><code>, FcValueBinding *</code><i>b</i><code>); </code></p>
<h2>Description</h2>
<p>Returns in <i>v</i> the <i>id</i>&#8216;th value and <i>b</i> binding for that associated with the property <i>object</i>. The Value returned is not a copy, but rather refers to the data stored within the pattern directly. Applications must not free this value.</p>
<h2>Since</h2>
<p>version 2.12.5</p>
