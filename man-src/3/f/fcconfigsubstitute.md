---
title: "fcconfigsubstitute(3)"
name: "fcconfigsubstitute"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigsubstitute/"
description: "FcConfigSubstitute – Execute substitutions"
---

<p>FcConfigSubstitute &#8211; Execute substitutions </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigSubstitute (FcConfig *</code><i>config</i><code>, FcPattern *</code><i>p</i><code>, FcMatchKind </code><i>kind</i><code>); </code></p>
<h2>Description</h2>
<p>Calls FcConfigSubstituteWithPat setting p_pat to NULL. Returns FcFalse if the substitution cannot be performed (due to allocation failure). Otherwise returns FcTrue. If <i>config</i> is NULL, the current configuration is used.</p>
