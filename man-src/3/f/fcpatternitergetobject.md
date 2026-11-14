---
title: "fcpatternitergetobject(3)"
name: "fcpatternitergetobject"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternitergetobject/"
description: "FcPatternIterGetObject – Returns an object name which the iterator point to"
---

<p>FcPatternIterGetObject &#8211; Returns an object name which the iterator point to </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> const char * FcPatternIterGetObject (const FcPattern *</code><i>p</i><code>, FcPatternIter *</code><i>iter</i><code>); </code></p>
<h2>Description</h2>
<p>Returns an object name in <i>p</i> which <i>iter</i> point to. returns NULL if <i>iter</i> isn&#8217;t valid.</p>
<h2>Since</h2>
<p>version 2.13.1</p>
