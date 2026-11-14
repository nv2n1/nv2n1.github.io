---
title: "xkbkeysymentry(3)"
name: "xkbkeysymentry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbkeysymentry/"
description: "XkbKeySymEntry – Returns the keysym corresponding to shift level shift and group grp from the two-dimensional array of keysyms for the key corresponding to keycode"
---

<p>XkbKeySymEntry &#8211; Returns the keysym corresponding to shift level <i>shift </i> and group <i>grp </i> from the two-dimensional array of keysyms for the key corresponding to <i>keycode</i> </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>KeySym XkbKeySymEntry</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>KeyCode </code><i>keycode</i><code>,</code> <code>int </code><i>shift</i><code>,</code> <code>int </code><i>grp</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>Xkb description of interest</p>
<dt><i>&#8211; keycode</i></p>
<dd>keycode of interest</p>
<dt><i>&#8211; shift</i></p>
<dd>shift level of interest</p>
<dt><i>&#8211; grp</i></p>
<dd>group of interest</dl>
<h2>Description</h2>
<p>The key width and number of groups associated with a key are used to form a small two-dimensional array of KeySyms for a key. This array may be different sizes for different keys. The array for a single key is stored as a linear list, in row-major order. The arrays for all of the keys are stored in the <i>syms </i> field of the client map. There is one row for each group associated with a key and one column for each level. The index corresponding to a given group and shift level is computed as: </p>
<pre> idx = group_index * key_width + shift_level</pre>
<p>The <i>offset </i> field of the <i>key_sym_map </i> entry for a key is used to access the beginning of the array. </p>
<p> <i>XkbKeySymEntry </i> returns the keysym corresponding to shift level <i>shift </i> and group <i>grp </i> from the two-dimensional array of keysyms for the key corresponding to <i>keycode.</i></p>
