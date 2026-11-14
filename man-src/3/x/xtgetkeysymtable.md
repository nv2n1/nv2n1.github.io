---
title: "xtgetkeysymtable(3)"
name: "xtgetkeysymtable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetkeysymtable/"
description: "XtGetKeysymTable, XtKeysymToKeycodeList – query keysyms and keycodes"
---

<p>XtGetKeysymTable, XtKeysymToKeycodeList &#8211; query keysyms and keycodes </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>KeySym* XtGetKeysymTable(Display* <i>display</i>, KeyCode* <i>min_keycode_return</i>, int *<i>keysyms_per_keycode_return</i>);</p>
<dd>void XtKeysymToKeycodeList(Display* <i>display</i>, KeySym <i>keysym</i>, KeyCode** <i>keycodes_return</i>, Cardinal* <i>keycount_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display whose table is required.</dl>
<dl COMPACT>
<dt><i>min_keycode_return</i></p>
<dd>Returns the minimum KeyCode valid for the display.</dl>
<dl COMPACT>
<dt><i>keysyms_per_keycode_return</i></p>
<dd>Returns the number of KeySyms stored for each KeyCode.</dl>
<dl COMPACT>
<dt><i>keysym</i></p>
<dd>Specifies the KeySym for which to search.</dl>
<dl COMPACT>
<dt><i>keycodes_return</i></p>
<dd>Returns a list of KeyCodes that have <i>keysym</i> associated with them, or NULL if <i>keycount_return</i> is 0.</dl>
<dl COMPACT>
<dt><i>keycount_return</i></p>
<dd>Returns the number of KeyCodes in the keycode list.</dl>
<h2>Description</h2>
<p><code>XtGetKeysymTable</code> returns a pointer to the Intrinsics&#8217; copy of the server&#8217;s KeyCode-to-KeySym table. This table must not be modified. </p>
<p> The <code>XtKeysymToKeycodeList</code> procedure returns all the KeyCodes that have <i>keysym</i> in their entry for the keyboard mapping table associated with <i>display</i>. The caller should free the storage pointed to by <i>keycodes_return</i> using <code>XtFree</code> when it is no longer useful.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
