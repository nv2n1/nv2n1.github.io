---
title: "fcpatterniterequal(3)"
name: "fcpatterniterequal"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatterniterequal/"
description: "FcPatternIterEqual – Compare iterators"
---

<p>FcPatternIterEqual &#8211; Compare iterators </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternIterEqual (const FcPattern *</code><i>p1</i><code>, FcPatternIter *</code><i>i1</i><code>, const FcPattern *</code><i>p2</i><code>, FcPatternIter *</code><i>i2</i><code>); </code></p>
<h2>Description</h2>
<p>Return FcTrue if both <i>i1</i> and <i>i2</i> point to same object and contains same values. return FcFalse otherwise.</p>
<h2>Since</h2>
<p>version 2.13.1</p>
