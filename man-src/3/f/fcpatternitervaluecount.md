---
title: "fcpatternitervaluecount(3)"
name: "fcpatternitervaluecount"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternitervaluecount/"
description: "FcPatternIterValueCount – Returns the number of the values which the iterator point to"
---

<p>FcPatternIterValueCount &#8211; Returns the number of the values which the iterator point to </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> int FcPatternIterValueCount (const FcPattern *</code><i>p</i><code>, FcPatternIter *</code><i>iter</i><code>); </code></p>
<h2>Description</h2>
<p>Returns the number of the values in the object which <i>iter</i> point to. if <i>iter</i> isn&#8217;t valid, returns 0.</p>
<h2>Since</h2>
<p>version 2.13.1</p>
