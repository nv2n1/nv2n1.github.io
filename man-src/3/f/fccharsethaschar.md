---
title: "fccharsethaschar(3)"
name: "fccharsethaschar"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsethaschar/"
description: "FcCharSetHasChar – Check a charset for a char"
---

<p>FcCharSetHasChar &#8211; Check a charset for a char </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcCharSetHasChar (const FcCharSet *</code><i>fcs</i><code>, FcChar32 </code><i>ucs4</i><code>); </code></p>
<h2>Description</h2>
<p>Returns whether <i>fcs</i> contains the char <i>ucs4</i>.</p>
