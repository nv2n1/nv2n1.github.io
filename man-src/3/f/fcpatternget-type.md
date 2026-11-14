---
title: "fcpatternget-type(3)"
name: "fcpatternget-type"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcpatternget-type/"
description: "FcPatternGetInteger, FcPatternGetDouble, FcPatternGetString, FcPatternGetMatrix, FcPatternGetCharSet, FcPatternGetBool, FcPatternGetFTFace, FcPatternGetLangSet, FcPatternGetRange – Return a typed v..."
---

<p>FcPatternGetInteger, FcPatternGetDouble, FcPatternGetString, FcPatternGetMatrix, FcPatternGetCharSet, FcPatternGetBool, FcPatternGetFTFace, FcPatternGetLangSet, FcPatternGetRange &#8211; Return a typed value from a pattern </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcResult FcPatternGetInteger (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>n</i><code>, int *</code><i>i</i><code>); </p>
<p> FcResult FcPatternGetDouble (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>n</i><code>, double *</code><i>d</i><code>); </p>
<p> FcResult FcPatternGetString (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>n</i><code>, FcChar8 **</code><i>s</i><code>); </p>
<p> FcResult FcPatternGetMatrix (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>n</i><code>, FcMatrix **</code><i>s</i><code>); </p>
<p> FcResult FcPatternGetCharSet (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>n</i><code>, FcCharSet **</code><i>c</i><code>); </p>
<p> FcResult FcPatternGetBool (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>n</i><code>, FcBool *</code><i>b</i><code>); </p>
<p> FcResult FcPatternGetFTFace (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>n</i><code>, FT_Face *</code><i>f</i><code>); </p>
<p> FcResult FcPatternGetLangSet (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>n</i><code>, FcLangSet **</code><i>l</i><code>); </p>
<p> FcResult FcPatternGetRange (FcPattern *</code><i>p</i><code>, const char *</code><i>object</i><code>, int </code><i>n</i><code>, FcRange **</code><i>r</i><code>); </code></p>
<h2>Description</h2>
<p>These are convenience functions that call FcPatternGet and verify that the returned data is of the expected type. They return FcResultTypeMismatch if this is not the case. Note that these (like FcPatternGet) do not make a copy of any data structure referenced by the return value. Use these in preference to FcPatternGet to provide compile-time typechecking. <code>FcPatternGetRange</code> are available since 2.11.91.</p>
