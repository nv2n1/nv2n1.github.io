---
title: "fcpatternadd-type(3)"
name: "fcpatternadd-type"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternadd-type/"
description: "FcPatternAddInteger, FcPatternAddDouble, FcPatternAddString, FcPatternAddMatrix, FcPatternAddCharSet, FcPatternAddBool, FcPatternAddFTFace, FcPatternAddLangSet, FcPatternAddRange – Add a typed valu..."
---

<p>FcPatternAddInteger, FcPatternAddDouble, FcPatternAddString, FcPatternAddMatrix, FcPatternAddCharSet, FcPatternAddBool, FcPatternAddFTFace, FcPatternAddLangSet, FcPatternAddRange &#8211; Add a typed value to a pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcPatternAddInteger (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>i</i><code>); </p>
<p> FcBool FcPatternAddDouble (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, double </code><i>d</i><code>); </p>
<p> FcBool FcPatternAddString (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, const FcChar8 *</code><i>s</i><code>); </p>
<p> FcBool FcPatternAddMatrix (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, const FcMatrix *</code><i>m</i><code>); </p>
<p> FcBool FcPatternAddCharSet (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, const FcCharSet *</code><i>c</i><code>); </p>
<p> FcBool FcPatternAddBool (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, FcBool </code><i>b</i><code>); </p>
<p> FcBool FcPatternAddFTFace (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, const FT_Face</code><i>f</i><code>); </p>
<p> FcBool FcPatternAddLangSet (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, const FcLangSet *</code><i>l</i><code>); </p>
<p> FcBool FcPatternAddRange (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, const FcRange *</code><i>r</i><code>); </code></p>
<h2>Description</h2>
<p>These are all convenience functions that insert objects of the specified type into the pattern. Use these in preference to FcPatternAdd as they will provide compile-time typechecking. These all append values to any existing list of values. <code>FcPatternAddRange</code> are available since 2.11.91.</p>
