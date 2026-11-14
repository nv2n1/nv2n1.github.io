---
title: "xkbfreekeyboard(3)"
name: "xkbfreekeyboard"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreekeyboard/"
description: "XkbFreeKeyboard – Destroys either an entire XkbDescRec or just some of its members"
---

<p>XkbFreeKeyboard &#8211; Destroys either an entire XkbDescRec or just some of its members </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeKeyboard</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>Bool </code><i>free_all</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>xkb</i></p>
<dd>
<dd>keyboard description with components to free</p>
<dt><i>which</i></p>
<dd>mask selecting components to free</p>
<dt><i>free_all</i></p>
<dd>True =&gt; free all components and <i>xkb</i></dl>
<h2>Description</h2>
<p><i>XkbFreeKeyboard </i> frees the components of <i>xkb </i> specified by <i>which </i> and sets the corresponding values to NULL. If <i>free_all </i> is True, <i>XkbFreeKeyboard </i> frees every non-NULL component of <i>xkb </i> and then frees the <i>xkb </i> structure itself. </p>
<p> If kbd is NULL, no operation is performed. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreeclientmap/">XkbFreeClientMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbfreeservermap/">XkbFreeServerMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbfreecompatmap/">XkbFreeCompatMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbfreeindicatormaps/">XkbFreeIndicatorMaps</a></code>(3), <code><a href="/docs/linux/man/3-xkbfreenames/">XkbFreeNames</a></code>(3), <code><a href="/docs/linux/man/3-xkbfreegeometry/">XkbFreeGeometry</a></code>(3), <code><a href="/docs/linux/man/3-xkbfreecontrols/">XkbFreeControls</a></code>(3)</p>
