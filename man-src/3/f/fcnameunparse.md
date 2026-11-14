---
title: "fcnameunparse(3)"
name: "fcnameunparse"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcnameunparse/"
description: "FcNameUnparse – Convert a pattern back into a string that can be parsed"
---

<p>FcNameUnparse &#8211; Convert a pattern back into a string that can be parsed </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcNameUnparse (FcPattern *</code><i>pat</i><code>); </code></p>
<h2>Description</h2>
<p>Converts the given pattern into the standard text format described above. The return value is not static, but instead refers to newly allocated memory which should be freed by the caller using free().</p>
