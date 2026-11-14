---
title: "xkbcopykeytype(3)"
name: "xkbcopykeytype"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbcopykeytype/"
description: "XkbCopyKeyType – Copy one XkbKeyTypeRec structures"
---

<p>XkbCopyKeyType &#8211; Copy one XkbKeyTypeRec structures </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbCopyKeyType</code> <code>(XkbKeyTypePtr </code><i>from</i><code>,</code> <code>XkbKeyTypePtr </code><i>into</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; from</i></p>
<dd>
<dd>pointer to XkbKeyTypeRec to be copied</p>
<dt><i>&#8211; into</i></p>
<dd>pointer to XkbKeyTypeRec to be changed</dl>
<h2>Description</h2>
<p><i>XkbCopyKeyType </i> copies the key type specified by <i>from </i> to the key type specified by <i>into. </i> Both must point to legal XkbKeyTypeRec structures. Xkb assumes <i>from </i> and <i>into </i> point to different places. As a result, overlaps can be fatal. <i>XkbCopyKeyType </i> frees any existing <i>map, preserve, </i> and <i>level_names </i> in <i>into </i> prior to copying. If any allocation errors occur while copying <i>from </i> to <i>into, XkbCopyKeyType </i> returns BadAlloc. Otherwise, <i>XkbCopyKeyType </i> copies <i>from </i> to <i>into </i> and returns Success.</p>
<h2>Structures</h2>
<p>Key types are used to determine the shift level of a key given the current state of the keyboard. The set of all possible key types for the Xkb keyboard description are held in the <i>types </i> field of the client map, whose total size is stored in <i>size_types, </i> and whose total number of valid entries is stored in <i>num_types. </i> Key types are defined using the following structure: </p>
<pre>typedef struct { /* Key Type */
 XkbModsRec mods; /* modifiers used to compute shift level */
 unsigned char num_levels; /* total # shift levels, do not modify directly */
 unsigned char map_count; /* # entries in map, preserve (if non-NULL) */
 XkbKTMapEntryPtr map; /* vector of modifiers for each shift level */
 XkbModsPtr preserve; /* mods to preserve for corresponding map entry */
 Atom name; /* name of key type */
 Atom * level_names; /* array of names of each shift level */
} XkbKeyTypeRec, *XkbKeyTypePtr;</pre>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage </p>
</dl>
