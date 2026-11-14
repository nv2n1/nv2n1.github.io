---
title: "fcconfigparseandload(3)"
name: "fcconfigparseandload"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigparseandload/"
description: "FcConfigParseAndLoad – load a configuration file"
---

<p>FcConfigParseAndLoad &#8211; load a configuration file </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigParseAndLoad (FcConfig *</code><i>config</i><code>, const FcChar8 *</code><i>file</i><code>, FcBool </code><i>complain</i><code>); </code></p>
<h2>Description</h2>
<p>Walks the configuration in &#8216;file&#8217; and constructs the internal representation in &#8216;config&#8217;. Any include files referenced from within &#8216;file&#8217; will be loaded and parsed. If &#8216;complain&#8217; is FcFalse, no warning will be displayed if &#8216;file&#8217; does not exist. Error and warning messages will be output to stderr. Returns FcFalse if some error occurred while loading the file, either a parse error, semantic error or allocation failure. Otherwise returns FcTrue.</p>
