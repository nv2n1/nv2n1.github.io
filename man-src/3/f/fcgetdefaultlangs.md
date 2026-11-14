---
title: "fcgetdefaultlangs(3)"
name: "fcgetdefaultlangs"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcgetdefaultlangs/"
description: "FcGetDefaultLangs – Get the default languages list"
---

<p>FcGetDefaultLangs &#8211; Get the default languages list </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcStrSet * FcGetDefaultLangs (void</code><i></i><code>); </code></p>
<h2>Description</h2>
<p>Returns a string set of the default languages according to the environment variables on the system. This function looks for them in order of FC_LANG, LC_ALL, LC_CTYPE and LANG then. If there are no valid values in those environment variables, &quot;en&quot; will be set as fallback.</p>
<h2>Since</h2>
<p>version 2.9.91</p>
