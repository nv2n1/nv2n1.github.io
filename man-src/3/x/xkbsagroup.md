---
title: "xkbsagroup(3)"
name: "xkbsagroup"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsagroup/"
description: "XkbSAGroup – Returns the group_XXX field of act converted to a signed int"
---

<p>XkbSAGroup &#8211; Returns the group_XXX field of act converted to a signed int </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>int XkbSAGroup</code> <code>(XkbAction </code><i>act</i><code>);</code></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; act</i></p>
<dd>
<dd>action from which to extract group</dl>
<h2>Description</h2>
<p><i>XkbSAGroup </i> returns the <i>group_XXX </i> field of <i>act </i> converted to a signed int.</p>
<h2>Structure</h2>
<p>Actions associated with the XkbGroupAction structure change the current group state when keys are pressed and released: </p>
<pre> typedef struct _XkbGroupAction {
 unsigned char type; /* XkbSA_{Set|Latch|Lock}Group */
 unsigned char flags; /* with type, controls the effect on groups 
*/
 char group_XXX; /* represents a group index or delta */
 } XkbGroupAction;</pre>
<h2>Warning</h2>
<p>This manpage seems to be incomplete</p>
