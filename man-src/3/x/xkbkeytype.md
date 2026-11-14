---
title: "xkbkeytype(3)"
name: "xkbkeytype"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbkeytype/"
description: "XkbKeyType – Obtain the index of a key type or the pointer to a key type"
---

<p>XkbKeyType &#8211; Obtain the index of a key type or the pointer to a key type </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbKeyTypePtr XkbKeyType</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>KeyCode </code><i>keycode</i><code>,</code> <code>int </code><i>group</i><code>);</code><br />
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
<p><i>XkbKeyType </i> returns a pointer to the key type in the <i>types </i> vector of the client map in <i>xkb </i> corresponding to the given <i>keycode </i> and <i>group </i> index.</p>
<h2>Structures</h2>
<pre>typedef struct { /* Key Type */
 XkbModsRec mods; /* modifiers used to compute shift level */
 unsigned char num_levels; /* total # shift levels, do not modify directly */
 unsigned char map_count; /* # entries in map, preserve (if non-NULL) */
 XkbKTMapEntryPtr map; /* vector of modifiers for each shift level */
 XkbModsPtr preserve; /* mods to preserve for corresponding map entry */
 Atom name; /* name of key type */
 Atom * level_names; /* array of names of each shift level */
} XkbKeyTypeRec, *XkbKeyTypePtr;</pre>
