---
title: "xkbkeyhasactions(3)"
name: "xkbkeyhasactions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbkeyhasactions/"
description: "XkbKeyHasActions – Determines if the key corresponding to keycode has any actions associated with it"
---

<p>XkbKeyHasActions &#8211; Determines if the key corresponding to <i>keycode</i> has any actions associated with it </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>int XkbKeyHasActions</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>KeyCode </code><i>keycode</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>Xkb description of interest</p>
<dt><i>&#8211; keycode</i></p>
<dd>keycode of interest</dl>
<h2>Description</h2>
<p>A key action defines the effect key presses and releases have on the internal state of the server. For example, the expected key action associated with pressing the Shift key is to set the Shift modifier. There is zero or one key action associated with each keysym bound to each key. </p>
<p> Just as the entire list of key symbols for the keyboard mapping is held in the <i>syms </i> field of the client map, the entire list of key actions for the keyboard mapping is held in the <i>acts </i> array of the server map. The total size of <i>acts </i> is specified by <i>size_acts, </i> and the number of entries is specified by <i>num_acts. </i> </p>
<p> The <i>key_acts </i> array, indexed by keycode, describes the actions associated with a key. The <i>key_acts </i> array has <i>min_key_code </i> unused entries at the start to allow direct indexing using a keycode. If a <i>key_acts </i> entry is zero, it means the key does not have any actions associated with it. If an entry is not zero, the entry represents an index into the <i>acts </i> field of the server map, much as the <i>offset </i> field of a KeySymMapRec structure is an index into the <i>syms </i> field of the client map. </p>
<p> The reason the <i>acts </i> field is a linear list of XkbActions is to reduce the memory consumption associated with a keymap. Because Xkb allows individual keys to have multiple shift levels and a different number of groups per key, a single two-dimensional array of KeySyms would potentially be very large and sparse. Instead, Xkb provides a small two-dimensional array of XkbActions for each key. To store all of these individual arrays, Xkb concatenates each array together in the <i>acts </i> field of the server map. </p>
<p> The key action structures consist only of fields of type char or unsigned char. This is done to optimize data transfer when the server sends bytes over the wire. If the fields are anything but bytes, the server has to sift through all of the actions and swap any nonbyte fields. Because they consist of nothing but bytes, it can just copy them out. </p>
<p> <i>XkbKeyHasActions </i> returns True if the key corresponding to <i>keycode </i> has any actions associated with it; otherwise, it returns False.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbKeyHasActions </i> function will return True if the key corresponding to <i>keycode </i> has any actions associated with it.</p>
<dt>False</p>
<dd>The <i>XkbKeyHasActions </i> function will return False if the key corresponding to <i>keycode </i> does not have any actions associated with it.</dl>
<h2>Structures</h2>
<p>The KeySymMapRec structure is defined as follows: </p>
<pre> #define XkbNumKbdGroups 4
 #define XkbMaxKbdGroup (XkbNumKbdGroups-1)
 
 typedef struct { /* map to keysyms for a single keycode */
 unsigned char kt_index[XkbNumKbdGroups]; /* key type index for each group */
 unsigned char group_info; /* # of groups and out of range group handling */
 unsigned char width; /* max # of shift levels for key */
 unsigned short offset; /* index to keysym table in syms array */
} XkbSymMapRec, *XkbSymMapPtr;</pre>
