---
title: "fcconfigenablehome(3)"
name: "fcconfigenablehome"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigenablehome/"
description: "FcConfigEnableHome – controls use of the home directory."
---

<p>FcConfigEnableHome &#8211; controls use of the home directory. </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigEnableHome (FcBool </code><i>enable</i><code>); </code></p>
<h2>Description</h2>
<p>If <i>enable</i> is FcTrue, then Fontconfig will use various files which are specified relative to the user&#8217;s home directory (using the ~ notation in the configuration). When <i>enable</i> is FcFalse, then all use of the home directory in these contexts will be disabled. The previous setting of the value is returned.</p>
