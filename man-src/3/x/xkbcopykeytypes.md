---
title: "xkbcopykeytypes(3)"
name: "xkbcopykeytypes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbcopykeytypes/"
description: "XkbCopyKeyTypes – Copy more than one XkbKeyTypeRec structure"
---

<p>XkbCopyKeyTypes &#8211; Copy more than one XkbKeyTypeRec structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbCopyKeyTypes</code> <code>(XkbKeyTypePtr </code><i>from</i><code>,</code> <code>XkbKeyTypePtr </code><i>into</i><code>,</code> <code>int </code><i>num_types</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; from</i></p>
<dd>
<dd>pointer to array of XkbKeyTypeRecs to copy</p>
<dt><i>&#8211; into</i></p>
<dd>pointer to array of XkbKeyTypeRecs to change</p>
<dt><i>&#8211; num_types</i></p>
<dd>number of types to copy</dl>
<h2>Description</h2>
<p><i>XkbCopyKeyTypes </i> copies <i>num_types </i> XkbKeyTypeRec structures from the array specified by <i>from </i> into the array specified by <i>into. </i> It is intended for copying between, rather than within, keyboard descriptions, so it doesn&#8217;t check for overlaps. The same rules that apply to the <i>from </i> and <i>into </i> parameters in <i>XkbCopyKeyType </i> apply to each entry of the <i>from </i> and <i>into </i> arrays of <i>XkbCopyKeyTypes. </i> If any allocation errors occur while copying <i>from </i> to <i>into, XkbCopyKeyTypes </i> returns BadAlloc. Otherwise, <i>XkbCopyKeyTypes </i> copies <i>from </i> to <i>into </i> and returns Success.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The XkbCopyKeyTypes function returns Success when there are no allocation errors.</dl>
<h2>Structures</h2>
<p>Key types are used to determine the shift level of a key given the current state of the keyboard. The set of all possible key types for the Xkb keyboard description are held in the <i>types </i> field of the client map, whose total size is stored in <i>size_types, </i> and whose total number of valid entries is stored in <i>num_types. </i> Key types are defined using the following structure: </p>
<pre>typedef struct { /* Key Type */
 XkbModsRec mods; /* modifiers used to compute shift level */
 unsigned char num_levels; /* total # shift levels, do not modify 
directly */
 unsigned char map_count; /* # entries in map, preserve (if non-NULL) 
*/
 XkbKTMapEntryPtr map; /* vector of modifiers for each shift level 
*/
 XkbModsPtr preserve; /* mods to preserve for corresponding map 
entry */
 Atom name; /* name of key type */
 Atom * level_names; /* array of names of each shift level */
} XkbKeyTypeRec, *XkbKeyTypePtr;</pre>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbcopykeytype/">XkbCopyKeyType</a></code>(3)</p>
