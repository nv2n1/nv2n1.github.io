---
title: "fcinitreinitialize(3)"
name: "fcinitreinitialize"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcinitreinitialize/"
description: "FcInitReinitialize – re-initialize library"
---

<p>FcInitReinitialize &#8211; re-initialize library </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcInitReinitialize (void</code><i></i><code>); </code></p>
<h2>Description</h2>
<p>Forces the default configuration file to be reloaded and resets the default configuration. Returns FcFalse if the configuration cannot be reloaded (due to configuration file errors, allocation failures or other issues) and leaves the existing configuration unchanged. Otherwise returns FcTrue.</p>
