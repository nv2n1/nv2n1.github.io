---
title: "fcfilescan(3)"
name: "fcfilescan"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcfilescan/"
description: "FcFileScan – scan a font file"
---

<p>FcFileScan &#8211; scan a font file </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> FcBool FcFileScan (FcFontSet *</code><i>set</i><code>, FcStrSet *</code><i>dirs</i><code>, FcFileCache *</code><i>cache</i><code>, FcBlanks *</code><i>blanks</i><code>, const FcChar8 *</code><i>file</i><code>, FcBool </code><i>force</i><code>); </code></p>
<h2>Description</h2>
<p>Scans a single file and adds all fonts found to <i>set</i>. If <i>force</i> is FcTrue, then the file is scanned even if associated information is found in <i>cache</i>. If <i>file</i> is a directory, it is added to <i>dirs</i>. Whether fonts are found depends on fontconfig policy as well as the current configuration. Internally, fontconfig will ignore BDF and PCF fonts which are not in Unicode (or the effectively equivalent ISO Latin-1) encoding as those are not usable by Unicode-based applications. The configuration can ignore fonts based on filename or contents of the font file itself. Returns FcFalse if any of the fonts cannot be added (due to allocation failure). Otherwise returns FcTrue.</p>
