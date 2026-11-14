---
title: "fcpatternfilter(3)"
name: "fcpatternfilter"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternfilter/"
description: "FcPatternFilter – Filter the objects of pattern"
---

<p>FcPatternFilter &#8211; Filter the objects of pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcPattern * FcPatternFilter (FcPattern *</code><i>p</i><code>, const FcObjectSet *</code><i></i><code>); </code></p>
<h2>Description</h2>
<p>Returns a new pattern that only has those objects from <i>p</i> that are in <i>os</i>. If <i>os</i> is NULL, a duplicate of <i>p</i> is returned.</p>
