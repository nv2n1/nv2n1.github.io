---
title: "xkbresizekeyactions(3)"
name: "xkbresizekeyactions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbresizekeyactions/"
description: "XkbResizeKeyActions – Change the number of actions bound to a key"
---

<p>XkbResizeKeyActions &#8211; Change the number of actions bound to a key </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbAction * XkbResizeKeyActions</code> <code>(XkbDescRec *</code><i>xkb</i><code>,</code> <code>int </code><i>key</i><code>,</code> <code>int </code><i>needed</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description to change</p>
<dt><i>&#8211; key</i></p>
<dd>keycode of key to change</p>
<dt><i>&#8211; needed</i></p>
<dd>new number of actions required</dl>
<h2>Description</h2>
<p>The <i>xkb </i> parameter points to the keyboard description containing the <i>key </i> whose number of actions is to be changed. The <i>key </i> parameter is the keycode of the key to change, and needed specifies the new number of actions required for the key. </p>
<p> <i>XkbResizeKeyActions </i> reserves the space needed for the actions and returns a pointer to the beginning of the new array that holds the actions. It can change the <i>acts, num_acts, </i> and <i>size_acts </i> fields of <i>xkb-&gt;server </i> if it is necessary to reallocate the <i>acts </i> array. </p>
<p> If <i>needed </i> is greater than the current number of keysyms for the key, <i>XkbResizeKeyActions </i> initializes all new actions in the array to NoAction. </p>
<p> Because the number of actions needed by a key is normally computed as width * number of groups, and <i>XkbResizeKeyActions </i> does not modify either the width or number of groups for the key, a discrepancy exists on return from <i>XkbResizeKeyActions </i> between the space allocated for the actions and the number required. The unused entries in the list of actions returned by <i>XkbResizeKeyActions </i> are not preserved across future calls to any of the map editing functions, so you must update the key actions (which updates the width and number of groups for the key) before calling another allocator function. A call to <i>XkbChangeTypesOfKey </i> updates these. </p>
<p> If any allocation errors occur while resizing the number of actions bound to the key, <i>XkbResizeKeyActions </i> returns NULL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangetypesofkey/">XkbChangeTypesOfKey</a></code>(3), <code><a href="/docs/linux/man/3-xkbresizekeysyms/">XkbResizeKeySyms</a></code>(3)</p>
<h2>Notes</h2>
<p>A change to the number of actions bound to a key should be accompanied by a change in the number of symbols bound to a key. Refer to <i>XkbResizeKeySyms </i> for more information on changing the number of symbols bound to a key.</p>
