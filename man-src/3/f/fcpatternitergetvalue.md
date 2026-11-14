---
title: "fcpatternitergetvalue(3)"
name: "fcpatternitergetvalue"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternitergetvalue/"
description: "FcPatternIterGetValue – Returns a value which the iterator point to"
---

<p>FcPatternIterGetValue &#8211; Returns a value which the iterator point to </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcResult FcPatternIterGetValue (const FcPattern *</code><i>p</i><code>, FcPatternIter *</code><i>iter</i><code>, int</code><i>id</i><code>, FcValue *</code><i>v</i><code>, FcValueBinding *</code><i>b</i><code>); </code></p>
<h2>Description</h2>
<p>Returns in <i>v</i> the <i>id</i>&#8216;th value which <i>iter</i> point to. also binding to <i>b</i> if given. The value returned is not a copy, but rather refers to the data stored within the pattern directly. Applications must not free this value.</p>
<h2>Since</h2>
<p>version 2.13.1</p>
