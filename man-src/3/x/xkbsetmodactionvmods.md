---
title: "xkbsetmodactionvmods(3)"
name: "xkbsetmodactionvmods"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetmodactionvmods/"
description: "XkbSetModActionVMods – Sets the vmods1 and vmods2 fields of act using the vmods format of an Xkb modifier description"
---

<p>XkbSetModActionVMods &#8211; Sets the vmods1 and vmods2 fields of act using the vmods format of an Xkb modifier description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbSetModActionVMods</code> <code>(XkbAction </code><i>act</i><code>,</code> <code>unsigned short </code><i>vmods</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; act</i></p>
<dd>
<dd>action in which to set vmods</p>
<dt><i>&#8211; vmods</i></p>
<dd>virtual mods to set</dl>
<h2>Description</h2>
<p><i>XkbSetModActionVMods </i> sets the <i>vmods1 </i> and <i>vmods2 </i> fields of <i>act </i> using the <i>vmods </i> format of an Xkb modifier description.</p>
<h2>Notes</h2>
<p>Despite the fact that the first parameter of these two macros is of type XkbAction, these macros may be used only with Actions of type XkbModAction and XkbISOAction.</p>
