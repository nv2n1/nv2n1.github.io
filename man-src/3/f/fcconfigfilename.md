---
title: "fcconfigfilename(3)"
name: "fcconfigfilename"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcconfigfilename/"
description: "FcConfigFilename – Find a config file"
---

<p>FcConfigFilename &#8211; Find a config file </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcChar8 * FcConfigFilename (const FcChar8 *</code><i>name</i><code>); </code></p>
<h2>Description</h2>
<p>Given the specified external entity name, return the associated filename. This provides applications a way to convert various configuration file references into filename form. </p>
<p> A null or empty <i>name</i> indicates that the default configuration file should be used; which file this references can be overridden with the FONTCONFIG_FILE environment variable. Next, if the name starts with <i>~</i>, it refers to a file in the current users home directory. Otherwise if the name doesn&#8217;t start with &#8216;/&#8217;, it refers to a file in the default configuration directory; the built-in default directory can be overridden with the FONTCONFIG_PATH environment variable.</p>
