---
title: "xkbresizekeysyms(3)"
name: "xkbresizekeysyms"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbresizekeysyms/"
description: "XkbResizeKeySyms – Change the number of symbols bound to a key"
---

<p>XkbResizeKeySyms &#8211; Change the number of symbols bound to a key </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>KeySym * XkbResizeKeySyms</code> <code>(XkbDescRec *</code><i>xkb</i><code>,</code> <code>int </code><i>key</i><code>,</code> <code>int </code><i>needed</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description to be changed</p>
<dt><i>&#8211; key</i></p>
<dd>keycode for key to modify</p>
<dt><i>&#8211; needed</i></p>
<dd>new number of keysyms required for key</dl>
<h2>Description</h2>
<p><i>XkbResizeKeySyms </i> reserves the space needed for <i>needed </i> keysyms and returns a pointer to the beginning of the new array that holds the keysyms. It adjusts the <i>offset </i> field of the <i>key_sym_map </i> entry for the key if necessary and can also change the <i>syms, num_syms, </i> and <i>size_syms </i> fields of <i>xkb-&gt;map </i> if it is necessary to reallocate the <i>syms </i> array. <i>XkbResizeKeySyms </i> does not modify either the width or number of groups associated with the key. </p>
<p> If <i>needed </i> is greater than the current number of keysyms for the key, <i>XkbResizeKeySyms </i> initializes all new keysyms in the array to NoSymbol. </p>
<p> Because the number of symbols needed by a key is normally computed as width * number of groups, and <i>XkbResizeKeySyms </i> does not modify either the width or number of groups for the key, a discrepancy exists upon return from <i>XkbResizeKeySyms </i> between the space allocated for the keysyms and the number required. The unused entries in the list of symbols returned by <i>XkbResizeKeySyms </i> are not preserved across future calls to any of the map editing functions, so you must update the key symbol mapping (which updates the width and number of groups for the key) before calling another allocator function. A call to <i>XkbChangeTypesOfKey </i> will update the mapping. </p>
<p> If any allocation errors occur while resizing the number of symbols bound to the key, <i>XkbResizeKeySyms </i> returns NULL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangetypesofkey/">XkbChangeTypesOfKey</a></code>(3), <code><a href="/docs/linux/man/3-xkbresizekeyactions/">XkbResizeKeyActions</a></code>(3)</p>
<h2>Notes</h2>
<p>A change to the number of symbols bound to a key should be accompanied by a change in the number of actions bound to a key. Refer to XkbResizeKeyActions for more information on changing the number of actions bound to a key.</p>
