---
title: "fcvaluesave(3)"
name: "fcvaluesave"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcvaluesave/"
description: "FcValueSave – Copy a value"
---

<p>FcValueSave &#8211; Copy a value </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcValue FcValueSave (FcValue </code><i>v</i><code>); </code></p>
<h2>Description</h2>
<p>Returns a copy of <i>v</i> duplicating any object referenced by it so that <i>v</i> may be safely destroyed without harming the new value.</p>
