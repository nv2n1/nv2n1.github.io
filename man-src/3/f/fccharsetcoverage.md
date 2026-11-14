---
title: "fccharsetcoverage(3)"
name: "fccharsetcoverage"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetcoverage/"
description: "FcCharSetCoverage – DEPRECATED return coverage for a Unicode page"
---

<p>FcCharSetCoverage &#8211; DEPRECATED return coverage for a Unicode page </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar32 FcCharSetCoverage (const FcCharSet *</code><i>a</i><code>, FcChar32</code><i>page</i><code>, FcChar32[8]</code><i>result</i><code>); </code></p>
<h2>Description</h2>
<p>DEPRECATED This function returns a bitmask in <i>result</i> which indicates which code points in <i>page</i> are included in <i>a</i>. <code>FcCharSetCoverage</code> returns the next page in the charset which has any coverage.</p>
