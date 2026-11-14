---
title: "fcfreetypequeryface(3)"
name: "fcfreetypequeryface"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfreetypequeryface/"
description: "FcFreeTypeQueryFace – compute pattern from FT_Face"
---

<p>FcFreeTypeQueryFace &#8211; compute pattern from FT_Face </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig.h&gt; #include &lt;fcfreetype.h&gt; </p>
<p> FcPattern * FcFreeTypeQueryFace (const FT_Face </code><i>face</i><code>, const FcChar8 *</code><i>file</i><code>, int </code><i>id</i><code>, FcBlanks *</code><i>blanks</i><code>); </code></p>
<h2>Description</h2>
<p>Constructs a pattern representing &#8216;face&#8217;. &#8216;file&#8217; and &#8216;id&#8217; are used solely as data for pattern elements (FC_FILE, FC_INDEX and sometimes FC_FAMILY). FcBlanks is deprecated, <i>blanks</i> is ignored and accepted only for compatibility with older code.</p>
