---
title: "xkbkeysymsoffset(3)"
name: "xkbkeysymsoffset"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbkeysymsoffset/"
description: "XkbKeySymsOffset – Returns the offset of the two-dimensional array of keysyms for the key corresponding to keycode"
---

<p>XkbKeySymsOffset &#8211; Returns the offset of the two-dimensional array of keysyms for the key corresponding to <i>keycode</i> </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>int XkbKeySymsOffset</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>KeyCode </code><i>keycode</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>Xkb description of interest</p>
<dt><i>&#8211; keycode</i></p>
<dd>keycode of interest</dl>
<h2>Description</h2>
<p>The key width and number of groups associated with a key are used to form a small two-dimensional array of KeySyms for a key. This array may be different sizes for different keys. The array for a single key is stored as a linear list, in row-major order. The arrays for all of the keys are stored in the <i>syms </i> field of the client map. There is one row for each group associated with a key and one column for each level. The index corresponding to a given group and shift level is computed as: </p>
<pre> idx = group_index * key_width + shift_level</pre>
<p>The <i>offset </i> field of the <i>key_sym_map </i> entry for a key is used to access the beginning of the array. </p>
<p> <i>XkbKeySymsOffset </i> returns the offset of the two-dimensional array of keysyms for the key corresponding to <i>keycode.</i></p>
