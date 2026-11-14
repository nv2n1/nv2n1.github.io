---
title: "fcfini(3)"
name: "fcfini"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfini/"
description: "FcFini – finalize fontconfig library"
---

<p>FcFini &#8211; finalize fontconfig library </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> void FcFini (void</code><i></i><code>); </code></p>
<h2>Description</h2>
<p>Frees all data structures allocated by previous calls to fontconfig functions. Fontconfig returns to an uninitialized state, requiring a new call to one of the FcInit functions before any other fontconfig function may be called.</p>
