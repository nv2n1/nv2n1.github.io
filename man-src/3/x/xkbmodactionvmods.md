---
title: "xkbmodactionvmods(3)"
name: "xkbmodactionvmods"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbmodactionvmods/"
description: "XkbModActionVMods – Returns the vmods1 and vmods2 fields of act converted to the vmods format of an Xkb modifier description"
---

<p>XkbModActionVMods &#8211; Returns the vmods1 and vmods2 fields of act converted to the vmods format of an Xkb modifier description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>unsigned short XkbModActionVMods</code> <code>(XkbAction </code><i>act</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; act</i></p>
<dd>
<dd>action from which to extract virtual mods</dl>
<h2>Description</h2>
<p><i>XkbModActionVMods </i> returns the <i>vmods1 </i> and <i>vmods2 </i> fields of <i>act </i> converted to the <i>vmods </i> format of an Xkb modifier description.</p>
