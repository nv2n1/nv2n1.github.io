---
title: "fcatomicreplaceorig(3)"
name: "fcatomicreplaceorig"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcatomicreplaceorig/"
description: "FcAtomicReplaceOrig – replace original with new"
---

<p>FcAtomicReplaceOrig &#8211; replace original with new </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcAtomicReplaceOrig (FcAtomic *</code><i>atomic</i><code>); </code></p>
<h2>Description</h2>
<p>Replaces the original file referenced by <i>atomic</i> with the new file. Returns FcFalse if the file cannot be replaced due to permission issues in the filesystem. Otherwise returns FcTrue.</p>
