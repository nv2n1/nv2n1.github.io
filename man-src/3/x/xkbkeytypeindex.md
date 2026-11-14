---
title: "xkbkeytypeindex(3)"
name: "xkbkeytypeindex"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbkeytypeindex/"
description: "XkbKeyTypeIndex – Obtain the index of a key type or the pointer to a key type"
---

<p>XkbKeyTypeIndex &#8211; Obtain the index of a key type or the pointer to a key type </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>int XkbKeyTypeIndex</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>KeyCode </code><i>keycode</i><code>,</code> <code>int </code><i>group</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>Xkb description of interest</p>
<dt><i>&#8211; keycode</i></p>
<dd>keycode of interest</p>
<dt><i>&#8211; group</i></p>
<dd>group index</dl>
<h2>Description</h2>
<p><i>XkbKeyTypeIndex </i> computes an index into the <i>types </i> vector of the client map in <i>xkb </i> from the given <i>keycode </i> and <i>group </i> index.</p>
