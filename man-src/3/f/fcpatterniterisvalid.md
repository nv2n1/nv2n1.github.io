---
title: "fcpatterniterisvalid(3)"
name: "fcpatterniterisvalid"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatterniterisvalid/"
description: "FcPatternIterIsValid – Check whether the iterator is valid or not"
---

<p>FcPatternIterIsValid &#8211; Check whether the iterator is valid or not </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternIterIsValid (const FcPattern *</code><i>p</i><code>, FcPatternIter :</code><i>iter</i><code>); </code></p>
<h2>Description</h2>
<p>Returns FcTrue if <i>iter</i> point to the valid entry in <i>p</i>. returns FcFalse otherwise.</p>
<h2>Since</h2>
<p>version 2.13.1</p>
