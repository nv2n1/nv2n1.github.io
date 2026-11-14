---
title: "xkbsasetgroup(3)"
name: "xkbsasetgroup"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsasetgroup/"
description: "XkbSASetGroup – Sets the group_XXX field of act from the group index grp"
---

<p>XkbSASetGroup &#8211; Sets the group_XXX field of act from the group index grp </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbSASetGroup</code> <code>(XkbAction </code><i>act</i><code>,</code> <code>int </code><i>grp</i><code>);</code></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; act</i></p>
<dd>
<dd>action from which to set group</p>
<dt><i>&#8211; grp</i></p>
<dd>group index to set in group_XXX</dl>
<h2>Description</h2>
<p><i>XkbSASetGroup </i> sets the <i>group_XXX </i> field of <i>act </i> from the group index <i>grp. </i></p>
<h2>Structure</h2>
<p>Actions associated with the XkbGroupAction structure change the current group state when keys are pressed and released: </p>
<pre> typedef struct _XkbGroupAction {
 unsigned char type; /* XkbSA_{Set|Latch|Lock}Group */
 unsigned char flags; /* with type, controls the effect on groups */
 char group_XXX; /* represents a group index or delta */
 } XkbGroupAction;</pre>
<h2>Warning</h2>
<p>This manpage seems to be incomplete</p>
