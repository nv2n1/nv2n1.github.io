---
title: "xkbaddsyminterpret(3)"
name: "xkbaddsyminterpret"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbaddsyminterpret/"
description: "XkbAddSymInterpret – Add a symbol interpretation to the list of symbol interpretations in an XkbCompatRec"
---

<p>XkbAddSymInterpret &#8211; Add a symbol interpretation to the list of symbol interpretations in an XkbCompatRec </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbSymInterpretPtr XkbAddSymInterpret</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>XkbSymInterpretPtr </code><i>si</i><code>,</code> <code>Bool </code><i>updateMap</i><code>,</code> <code>XkbChangesPtr </code><i>changes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description to be updated</p>
<dt><i>&#8211; si</i></p>
<dd>symbol interpretation to be added</p>
<dt><i>&#8211; updateMap</i></p>
<dd>True=&gt;apply compatibility map to keys</p>
<dt><i>&#8211; changes</i></p>
<dd>changes are put here</dl>
<h2>Description</h2>
<p><i>XkbAddSymInterpret </i> adds <i>si </i> to the list of symbol interpretations in <i>xkb. </i> If <i>updateMap </i> is True, it (re)applies the compatibility map to all of the keys on the keyboard. If <i>changes </i> is non-NULL, it reports the parts of the keyboard that were affected (unless <i>updateMap </i> is True, not much changes). <i>XkbAddSymInterpret </i> returns a pointer to the actual new symbol interpretation in the list or NULL if it failed.</p>
