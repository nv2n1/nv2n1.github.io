---
title: "fcconfigsubstitutewithpat(3)"
name: "fcconfigsubstitutewithpat"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigsubstitutewithpat/"
description: "FcConfigSubstituteWithPat – Execute substitutions"
---

<p>FcConfigSubstituteWithPat &#8211; Execute substitutions </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigSubstituteWithPat (FcConfig *</code><i>config</i><code>, FcPattern *</code><i>p</i><code>, FcPattern *</code><i>p_pat</i><code>, FcMatchKind </code><i>kind</i><code>); </code></p>
<h2>Description</h2>
<p>Performs the sequence of pattern modification operations, if <i>kind</i> is FcMatchPattern, then those tagged as pattern operations are applied, else if <i>kind</i> is FcMatchFont, those tagged as font operations are applied and p_pat is used for &lt;test&gt; elements with target=pattern. Returns FcFalse if the substitution cannot be performed (due to allocation failure). Otherwise returns FcTrue. If <i>config</i> is NULL, the current configuration is used.</p>
