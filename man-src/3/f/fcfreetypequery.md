---
title: "fcfreetypequery(3)"
name: "fcfreetypequery"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfreetypequery/"
description: "FcFreeTypeQuery – compute pattern from font file (and index)"
---

<p>FcFreeTypeQuery &#8211; compute pattern from font file (and index) </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig.h&gt; #include &lt;fcfreetype.h&gt; </p>
<p> FcPattern * FcFreeTypeQuery (const FcChar8 *</code><i>file</i><code>, int </code><i>id</i><code>, FcBlanks *</code><i>blanks</i><code>, int *</code><i>count</i><code>); </code></p>
<h2>Description</h2>
<p>Constructs a pattern representing the &#8216;id&#8217;th face in &#8216;file&#8217;. The number of faces in &#8216;file&#8217; is returned in &#8216;count&#8217;. FcBlanks is deprecated, <i>blanks</i> is ignored and accepted only for compatibility with older code.</p>
