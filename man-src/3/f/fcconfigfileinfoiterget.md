---
title: "fcconfigfileinfoiterget(3)"
name: "fcconfigfileinfoiterget"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigfileinfoiterget/"
description: "FcConfigFileInfoIterGet – Obtain the configuration file information"
---

<p>FcConfigFileInfoIterGet &#8211; Obtain the configuration file information </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcConfigFileInfoIterGet (FcConfig *</code><i>config</i><code>, FcConfigFileInfoIter *</code><i>iter</i><code>, FcChar8 **</code><i>name</i><code>, FcChar8 **</code><i>description</i><code>, FcBool *</code><i>enabled</i><code>); </code></p>
<h2>Description</h2>
<p>Obtain the filename, the description and the flag whether it is enabled or not for &#8216;iter&#8217; where points to current configuration file information. If the iterator is invalid, FcFalse is returned.</p>
<h2>Since</h2>
<p>version 2.12.91</p>
