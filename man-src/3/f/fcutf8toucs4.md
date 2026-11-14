---
title: "fcutf8toucs4(3)"
name: "fcutf8toucs4"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcutf8toucs4/"
description: "FcUtf8ToUcs4 – convert UTF-8 to UCS4"
---

<p>FcUtf8ToUcs4 &#8211; convert UTF-8 to UCS4 </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> int FcUtf8ToUcs4 (FcChar8 *</code><i>src</i><code>, FcChar32 *</code><i>dst</i><code>, int </code><i>len</i><code>); </code></p>
<h2>Description</h2>
<p>Converts the next Unicode char from <i>src</i> into <i>dst</i> and returns the number of bytes containing the char. <i>src</i> must be at least <i>len</i> bytes long.</p>
