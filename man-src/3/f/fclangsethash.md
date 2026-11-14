---
title: "fclangsethash(3)"
name: "fclangsethash"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fclangsethash/"
description: "FcLangSetHash – return a hash value for a langset"
---

<p>FcLangSetHash &#8211; return a hash value for a langset </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar32 FcLangSetHash (const FcLangSet *</code><i>ls</i><code>); </code></p>
<h2>Description</h2>
<p>This function returns a value which depends solely on the languages supported by <i>ls</i>. Any language which equals <i>ls</i> will have the same result from <code>FcLangSetHash</code>. However, two langsets with the same hash value may not be equal.</p>
