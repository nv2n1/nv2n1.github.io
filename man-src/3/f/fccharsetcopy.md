---
title: "fccharsetcopy(3)"
name: "fccharsetcopy"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fccharsetcopy/"
description: "FcCharSetCopy – Copy a charset"
---

<p>FcCharSetCopy &#8211; Copy a charset </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcCharSet * FcCharSetCopy (FcCharSet *</code><i>src</i><code>); </code></p>
<h2>Description</h2>
<p>Makes a copy of <i>src</i>; note that this may not actually do anything more than increment the reference count on <i>src</i>.</p>
