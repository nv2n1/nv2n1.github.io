---
title: "fcpatternprint(3)"
name: "fcpatternprint"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternprint/"
description: "FcPatternPrint – Print a pattern for debugging"
---

<p>FcPatternPrint &#8211; Print a pattern for debugging </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcPatternPrint (const FcPattern *</code><i>p</i><code>); </code></p>
<h2>Description</h2>
<p>Prints an easily readable version of the pattern to stdout. There is no provision for reparsing data in this format, it&#8217;s just for diagnostics and debugging.</p>
