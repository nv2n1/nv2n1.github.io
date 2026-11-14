---
title: "fclangsetequal(3)"
name: "fclangsetequal"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclangsetequal/"
description: "FcLangSetEqual – test for matching langsets"
---

<p>FcLangSetEqual &#8211; test for matching langsets </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcLangSetEqual (const FcLangSet *</code><i>ls_a</i><code>, const FcLangSet *</code><i>ls_b</i><code>); </code></p>
<h2>Description</h2>
<p>Returns FcTrue if and only if <i>ls_a</i> supports precisely the same language and territory combinations as <i>ls_b</i>.</p>
