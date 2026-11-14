---
title: "fcpatterniterstart(3)"
name: "fcpatterniterstart"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatterniterstart/"
description: "FcPatternIterStart – Initialize the iterator with the first iterator in the pattern"
---

<p>FcPatternIterStart &#8211; Initialize the iterator with the first iterator in the pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcPatternIterStart (const FcPattern *</code><i>p</i><code>, FcPatternIter *</code><i>iter</i><code>); </code></p>
<h2>Description</h2>
<p>Initialize <i>iter</i> with the first iterator in <i>p</i>. If there are no objects in <i>p</i>, <i>iter</i> will not have any valid data.</p>
<h2>Since</h2>
<p>version 2.13.1</p>
