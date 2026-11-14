---
title: "fcstrsetequal(3)"
name: "fcstrsetequal"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcstrsetequal/"
description: "FcStrSetEqual – check sets for equality"
---

<p>FcStrSetEqual &#8211; check sets for equality </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcStrSetEqual (FcStrSet *</code><i>set_a</i><code>, FcStrSet *</code><i>set_b</i><code>); </code></p>
<h2>Description</h2>
<p>Returns whether <i>set_a</i> contains precisely the same strings as <i>set_b</i>. Ordering of strings within the two sets is not considered.</p>
