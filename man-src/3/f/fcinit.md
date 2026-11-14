---
title: "fcinit(3)"
name: "fcinit"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcinit/"
description: "FcInit – initialize fontconfig library"
---

<p>FcInit &#8211; initialize fontconfig library </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcInit (void</code><i></i><code>); </code></p>
<h2>Description</h2>
<p>Loads the default configuration file and the fonts referenced therein and sets the default configuration to that result. Returns whether this process succeeded or not. If the default configuration has already been loaded, this routine does nothing and returns FcTrue.</p>
