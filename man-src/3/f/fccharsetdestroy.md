---
title: "fccharsetdestroy(3)"
name: "fccharsetdestroy"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetdestroy/"
description: "FcCharSetDestroy – Destroy a character set"
---

<p>FcCharSetDestroy &#8211; Destroy a character set </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcCharSetDestroy (FcCharSet *</code><i>fcs</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcCharSetDestroy</code> decrements the reference count <i>fcs</i>. If the reference count becomes zero, all memory referenced is freed.</p>
