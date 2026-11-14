---
title: "xkblookupkeysym(3)"
name: "xkblookupkeysym"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkblookupkeysym/"
description: "XkbLookupKeySym – Find the symbol associated with a key for a particular state"
---

<p>XkbLookupKeySym &#8211; Find the symbol associated with a key for a particular state </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbLookupKeySym</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>KeyCode </code><i>key</i><code>,</code> <code>unsigned int </code><i>state</i><code>,</code> <code>unsigned int *</code><i>mods_rtrn</i><code>,</code> <code>KeySym *</code><i>sym_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; key</i></p>
<dd>key for which symbols are to be found</p>
<dt><i>&#8211; state</i></p>
<dd>state for which symbol should be found</p>
<dt><i>&#8211; mods_rtrn</i></p>
<dd>backfilled with consumed modifiers</p>
<dt><i>&#8211; sym_rtrn</i></p>
<dd>backfilled with symbol associated with key + state</dl>
<h2>Description</h2>
<p><i>XkbLookupKeySym </i> is the equivalent of the core <i>XLookupKeySym </i> function. For the core keyboard, given a keycode <i>key </i> and an Xkb state <i>state, XkbLookupKeySym </i> returns the symbol associated with the key in <i>sym_rtrn </i> and the list of modifiers that should still be applied in <i>mods_rtrn. </i> The <i>state </i> parameter is the state from a KeyPress or KeyRelease event. <i>XkbLookupKeySym </i> returns True if it succeeds.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xlookupkeysym/">XLookupKeySym</a></code>(3)</p>
