---
title: "xkbfreeindicatormaps(3)"
name: "xkbfreeindicatormaps"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreeindicatormaps/"
description: "XkbFreeIndicatorMaps – Frees memory used by the indicators member of an XkbDescRec structure"
---

<p>XkbFreeIndicatorMaps &#8211; Frees memory used by the <i>indicators </i> member of an XkbDescRec structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeIndicatorMaps</code> <code>(XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description structure</dl>
<h2>Description</h2>
<p>If the <i>indicators </i> member of the keyboard description record pointed to by <i>xkb </i> is not NULL, <i>XkbFreeIndicatorMaps </i> frees the memory associated with the <i>indicators </i> member of <i>xkb.</i> </p>
<p> If xkb is NULL, no operation is performed. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocindicatormaps/">XkbAllocIndicatorMaps</a></code>(3)</p>
