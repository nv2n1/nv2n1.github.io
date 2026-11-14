---
title: "xkbkeysymtomodifiers(3)"
name: "xkbkeysymtomodifiers"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbkeysymtomodifiers/"
description: "XkbKeysymToModifiers – Finds the set of modifiers bound to a particular keysym on the core keyboard"
---

<p>XkbKeysymToModifiers &#8211; Finds the set of modifiers bound to a particular keysym on the core keyboard </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>unsigned int XkbKeysymToModifiers</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>KeySym </code><i>ks</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; ks</i></p>
<dd>keysym of interest</dl>
<h2>Description</h2>
<p><i>XkbKeysymToModifiers </i> finds the set of modifiers currently bound to the keysym <i>ks </i> on the core keyboard. The value returned is the mask of modifiers bound to the keysym <i>ks. </i> If no modifiers are bound to the keysym, <i>XkbKeysymToModifiers </i> returns zero; otherwise, it returns the inclusive OR of zero or more of the following: ShiftMask, ControlMask, LockMask, Mod1Mask, Mod2Mask, Mod3Mask, Mod4Mask, and Mod5Mask.</p>
