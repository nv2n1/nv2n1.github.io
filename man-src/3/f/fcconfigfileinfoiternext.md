---
title: "fcconfigfileinfoiternext(3)"
name: "fcconfigfileinfoiternext"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigfileinfoiternext/"
description: "FcConfigFileInfoIterNext – Set the iterator to point to the next list"
---

<p>FcConfigFileInfoIterNext &#8211; Set the iterator to point to the next list </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigFileInfoIterNext (FcConfig *</code><i>config</i><code>, FcConfigFileInfoIter *</code><i>iter</i><code>); </code></p>
<h2>Description</h2>
<p>Set &#8216;iter&#8217; to point to the next node in the config file information list. If there is no next node, FcFalse is returned.</p>
<h2>Since</h2>
<p>version 2.12.91</p>
