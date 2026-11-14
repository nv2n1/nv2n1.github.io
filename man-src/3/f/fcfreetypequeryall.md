---
title: "fcfreetypequeryall(3)"
name: "fcfreetypequeryall"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfreetypequeryall/"
description: "FcFreeTypeQueryAll – compute all patterns from font file (and index)"
---

<p>FcFreeTypeQueryAll &#8211; compute all patterns from font file (and index) </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig.h&gt; #include &lt;fcfreetype.h&gt; </p>
<p> unsigned int FcFreeTypeQueryAll (const FcChar8 *</code><i>file</i><code>, int </code><i>id</i><code>, FcBlanks *</code><i>blanks</i><code>, int *</code><i>count</i><code>, FcFontSet *</code><i>set</i><code>); </code></p>
<h2>Description</h2>
<p>Constructs patterns found in &#8216;file&#8217;. If id is -1, then all patterns found in &#8216;file&#8217; are added to &#8216;set&#8217;. Otherwise, this function works exactly like FcFreeTypeQuery(). The number of faces in &#8216;file&#8217; is returned in &#8216;count&#8217;. The number of patterns added to &#8216;set&#8217; is returned. FcBlanks is deprecated, <i>blanks</i> is ignored and accepted only for compatibility with older code.</p>
<h2>Since</h2>
<p>version 2.12.91</p>
